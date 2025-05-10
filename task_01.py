
def is_palindrome(data):
    if data == None:
        #print("is none")
        #print("----------------")
        return False
    
    # преобразуем в строку
    typed_data = str(data).lower()
    input_data = ''
    
    for c in typed_data:
        if c.isalnum():
            input_data += c

    #print(f'original - {input_data}')
    reversed_text = input_data[::-1].lower()
    #print(f'reversed - {reversed_text}')

    #print(reversed_text == input_data)
    #print("----------------")
    return reversed_text == input_data

# for test
test_1 = "A man, a plan, a canal -- Panama"
test_2 = "Madam, I'm Adam!"
test_3 = 333
test_4 = None
test_5 = "Abracadabra"

is_palindrome(test_1)
is_palindrome(test_2)
is_palindrome(test_3)
is_palindrome(test_4)
is_palindrome(test_5)