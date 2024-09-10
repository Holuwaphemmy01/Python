age = int(input("Enter your age: "))

if age > 19 and age <= 45:
	print("You're eligble to make your decision")
	print("Hello")
	print("Welcome")
elif    age >= 13 and age <= 19:
	print("You're still a teenager")
	print("Hello")
elif    age >= 0 and age < 13:
	print("You're still my child")
else:
	print("You does not exist")