import time
import collections
from functools import wraps

def cached(max_size=None, seconds=None):
    # Приводим max_size и seconds к целым числам, иначе делаем None
    try:
        max_size = int(max_size)
    except (ValueError, TypeError):
        max_size = None

    try:
        seconds = int(seconds)
    except (ValueError, TypeError):
        seconds = None

    def decorator(func):
        cache = collections.OrderedDict()

        @wraps(func)
        def wrapper(*args, **kwargs):
            # хэш
            key = (args, frozenset(kwargs.items()))
            current_time = time.time()

            if seconds is not None:
                keys_to_delete = [k for k, (_, ts) in cache.items() if current_time - ts > seconds]
                for k in keys_to_delete:
                    cache.pop(k, None)

            if key in cache:
                result, timestamp = cache[key]
            
                if seconds is None or current_time - timestamp <= seconds:
                    return result
                else:
                    del cache[key]  

  
            result = func(*args, **kwargs)
            cache[key] = (result, current_time)

            if max_size is not None:
                while len(cache) > max_size:
                    cache.popitem(last=False) 

            return result

        return wrapper

    return decorator