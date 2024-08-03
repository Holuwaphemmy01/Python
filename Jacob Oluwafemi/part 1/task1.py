# collect input of radius and of length from the user.
# to get the value for area, first of all get the value for pie which is 22 divided 7.
# mutiply the value of pie with radius and raise to the power of 2.
# to get the value for volume, multiply area by length.




radius = int(input('Enter radius:'))
length = int(input('Enter length: '))

area = ((22/7) * radius) ** 2
volume = area * length

print(f'The total area of the cylinder is {area:.2f}') 
print(f'The total volume of the cylinder is {volume:.2f}')
