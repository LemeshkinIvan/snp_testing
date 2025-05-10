def multiply_numbers(inputs = None):
    if inputs == None:
        # print("1 None")
        return inputs

    # инициировал бы нулем, было бы бессмысленно 
    result = 1
    str_value = str(inputs)
    filtered_values = []

    for el in str_value:
        if el.isnumeric():
            filtered_values.append(el)

    if len(filtered_values) == 0:
        # print("2 None")
        return None
    
    for num in filtered_values:
        result *= int(num)


    # print(result)
    return result


multiply_numbers()
multiply_numbers('ss')
multiply_numbers('1234')
multiply_numbers('sssdd34')
multiply_numbers(2.3)
multiply_numbers([5,6,4])