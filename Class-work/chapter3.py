name = "oluwafemi"
print(id(name))

name = name + " victor"
print(id(name))
print(name)

number = 3
print(id(number)) 

number = number + 6
print(id(number))

# append means to add a number to a set of numbers


# augumented assignment

number = 6
number **= 6
print(number)

number = 10
number += 12
print (number)

# for loop
for oluwafemi in 'techblazer':
	print("you are great")

for number in range(10):
	print(number) 

for number in range(1, 11):
	print(number)

# odd number
# by default steps is 1 but u can change the step
total = 0
for number in range(1, 11, 2):
	total += number
print(total)

# decreasing order
total = 0
for number in range(101, 1, -2):
	total += number
print(total)

femi = 89
result = 'true' if femi < 40 else 'false'
print(result)