
def max_odd(array = []):
    new_array = []

    for el in array:
        if (isinstance(el, float)) or (isinstance(el, int)):
            new_array.append(el)

    # я не стал париться с алгоритмами
    new_array.sort(reverse=True)
    
    for el in new_array:
        if el % 2 != 0:
            return el

    return None

print(max_odd([1, 2, 3, 4 ,4]))
print(max_odd([2,2]))
print(max_odd([21.0, 2, 3, 4, 4]))
print(max_odd(['oollo', 'uefuebf']))
print(max_odd(['oollo', 4, 2, 5]))