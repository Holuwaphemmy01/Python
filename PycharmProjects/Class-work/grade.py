# excercise in class

score = int(input("Enter your score: "))

if score >= 75 and score <= 100:
	print("You score A")
elif score >= 65 and score <= 74:
	print("You score B")
elif score >= 50 and score <= 64:
	print("You score C")
elif score >= 40 and score <= 49:
	print("You score D")
elif score >= 0 and score <= 39:
	print("You failed")
else:
	print("Invalid input")


#while loop examples 

count = 0
score = int(input('Enter a score'))
total = 0

while score == -1:
	count += 1
	total += score
	score = int(input('Enter a score'))

average = total // count
