
def connect_dicts(dict1, dict2):
    connected_dict = {}
    sorted_dict = {}

    dict1_sum = sum(dict1.values())
    dict2_sum = sum(dict2.values())

    # по дефолту приоритет у второго словаря
    enableReplacement = False

    if dict1_sum > dict2_sum:
        enableReplacement = True

    # сначала заполняем новый словарь первым
    for key, value in dict1.items():
        if value >= 10:
            connected_dict.update({key: value})

    # потом выполянем заполнение с проверкой приоритета
    for key, value in dict2.items():
        if value >= 10:
            if key in connected_dict:
                if enableReplacement:
                    continue
                else:
                    # заменяем 
                    connected_dict[key] = value
            else:
                # просто добавляем новую пару
                connected_dict.update({key: value})
                
    for key in sorted(connected_dict, key=connected_dict.get):
        sorted_dict[key] = connected_dict[key]

    return sorted_dict


print(connect_dicts({"a":2, "b": 12}, {"c": 11, "e": 5}))
print(connect_dicts({"a" : 13, "b" : 9, "d": 11}, {"c": 12, "a": 15}))
print(connect_dicts({"a" : 14, "b": 12}, {"c": 11, "a": 15}))