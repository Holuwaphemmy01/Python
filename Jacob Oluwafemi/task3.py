#prompt the user to value to convert to kilogram
# 1 pounds is 0.454 kilograms, then calculate the user input with 0.454.
# assign your result to a variable then print.



user_input = float(input('Enter your weight in pounds: '))

kilograms = user_input * 0.454

print(f'Your weight in kilogram is {kilograms}.')


