import random

def sort_list(array = []):

    if len(array) == 0:
        return []
    
    min_num = min(array)

    random.shuffle(array)
    array.append(min_num)
    return array


print(sort_list([]))
print(sort_list([2, 4, 6, 8]))
print(sort_list([1]))
print(sort_list([1, 2, 1, 3]))