factorial = int(input('Enter a number'))
number1 = 1
for number in range(factorial):
    number += 1
    number1 *= number
print (number1)