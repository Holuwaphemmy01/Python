user_input = int(input('Enter a five digits number: '))

value1 = user_input % 10
value2 = user_input // 10
value3 = value2 % 10
value4 = value2 // 10
value5 = value4 % 10
value6 = value4 // 10
value7 = value6 % 10
value8 = value6 // 10


if value1 == value8 and value3 == value7:
    print(user_input,'is a palindrome')
else:
    print(user_input, 'is not a palindrome')
