#prompt the user to enter number not less than zero and not greater than 1000.

# check if the user input is is not less than zero and and not greater than 1000.
# use palindrome to seperate the digit one by one.
#create a variable called total and sum up the digit.
#print.   

user_input = int(input("Enter number from 0 to 1000: "))

if user_input >= 0 and user_input <= 1000:
	value_one = user_input % 10
	value_two = user_input // 10
	value_three = value_two % 10
	value_four = value_two // 10
	total = value_one + value_three + value_four
	print(f'Total sum of the digits is {total}.')
else:
	print("Invalid number")