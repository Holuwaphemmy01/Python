def even_and_odd(number):
	if number % 2 == 0:
		result = "it is an even number"
	if number % 2 == 1:
		result = "it is an odd number"
	return result


digit = int(input("Enter a number: "))

print(even_and_odd(digit))