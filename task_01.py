
def is_palindrome(data):
    if data == None:
        return False
    
    typed_data = str(data).lower()
    input_data = ''
    
    for c in typed_data:
        if c.isalnum():
            input_data += c

    reversed_text = input_data[::-1].lower()
    return reversed_text == input_data

# for test
test_1 = "A man, a plan, a canal -- Panama"
test_2 = "Madam, I'm Adam!"
test_3 = 333
test_4 = None
test_5 = "Abracadabra"

print(is_palindrome(test_1))
print(is_palindrome(test_2))
print(is_palindrome(test_3))
print(is_palindrome(test_4))
print(is_palindrome(test_5))