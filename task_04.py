# исправил

def sort_list(lst):
    if not lst:
        return []
    
    min_val = min(lst)
    max_val = max(lst)
    
    # Заменяем минимумы на максимумы и наоборот
    swapped = [
        max_val if x == min_val else
        min_val if x == max_val else x
        for x in lst
    ]
    
    # Добавляем одно минимальное значение в конец (старое, до замены)
    swapped.append(min_val)
    
    return swapped

print(sort_list([]))
print(sort_list([2, 4, 6, 8]))
print(sort_list([1]))
print(sort_list([1, 2, 1, 3]))