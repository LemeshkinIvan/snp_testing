def multiply_numbers(inputs = None):
    if inputs == None: 
        return inputs

    # инициировал бы нулем, было бы бессмысленно 
    result = 1
    str_value = str(inputs)
    filtered_values = []

    for el in str_value:
        if el.isnumeric():
            filtered_values.append(el)

    if len(filtered_values) == 0:
        return None
    
    for num in filtered_values:
        result *= int(num)

    return result


print(multiply_numbers())
print(multiply_numbers('ss'))
print(multiply_numbers('1234'))
print(multiply_numbers('sssdd34'))
print(multiply_numbers(2.3))
print(multiply_numbers([5,6,4]))