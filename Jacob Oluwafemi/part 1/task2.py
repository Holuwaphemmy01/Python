# prompt the user to enter number in feet
# one foot is 0.305 multpily by the user input and assign it to a variable.
#print the variable.




user_input = float(input('Enter length in feet: '))

one_foot = 0.305

meters = one_foot * user_input
print(f'{user_input} feet is {meters} meters.')