#print the head as it is stated in the question.
#assign each row to variable
#itearate to get your calculation for the second row and the last row.
#print each iteration according to the head of the table.



print('a\t b\t a**b')
first_digit = 1
second_digit = 1
product = 1

for first_digit in range (1, 6):
	second_digit += 1
	product = first_digit ** second_digit
	print(first_digit,'\t',second_digit,'\t',product)
	
	
