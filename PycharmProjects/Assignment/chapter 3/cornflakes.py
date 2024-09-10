number = int(input('Enter a number to check the multiples: '))
counter = 0
number2 = 0

for number1 in range(10):
    counter += 1
    number2 = number * counter
    print(number,'x', counter,'=', number2)