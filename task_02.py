
def coincidence(array = [], diap = range(0, 0)):
    # проверяем наличие введенных аргументов по их значению
    if (array == []) or (diap == range(0, 0)):
        return []
    
    # set для исключения повторок
    num_collection = set()

    for el in array:
        try:
            typed_el = float(el)

            if type(typed_el) is float:
                num_collection.add(float(typed_el))

        except:
            continue

    digit_array = list(num_collection)
    # создаем из диапозона список с чиселками | как один из вариантов решения алгоритма
    range_list = list(diap)
    result = []

    for i in digit_array:
        if (i >= min(range_list)) and (i <= max(range_list)):
            result.append(i)

    return result
      

# for tests
print(coincidence([1, 2, 3, 4, 5], range(3, 6)))
print(coincidence())
print(coincidence([None, 1, "foo", 4, 2, 2.5], range(1, 4)))