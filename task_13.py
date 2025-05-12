import time

def cached(max_size=None, seconds=None):
    if not isinstance(max_size, int):
        max_size = None
    if not isinstance(seconds, (int, float)):
        seconds = None

    def decorator(func):
        cache = {}
        id = 0

        def wrapper(*args, **kwargs):
            now = time.time()
            nonlocal id
            id += 1
            key = id

            # чистим старые записи
            if seconds is not None:
                expired_keys = [k for k, (_, t) in cache.items() if now - t > seconds]
                for k in expired_keys:
                    del cache[k]

            if key in cache:
                result, timestamp = cache[key]
                return result

            result = func(*args, **kwargs)
            cache[key] = (result, now)

            # удаляем самый старый элемент, если размер кэша превышен
            if max_size is not None and len(cache) > max_size:
                # находим ключ с минимальным временем
                oldest_key = min(cache.items(), key=lambda item: item[1][1])[0]
                del cache[oldest_key]

            return result

        return wrapper

    return decorator

@cached(max_size=3, seconds = 10)
def slow_function(x):
    print(f"Вычисляю для {x}...")
    return x ** 2


print(slow_function(5))
print(slow_function(5))
time.sleep(15)
print(slow_function(5))