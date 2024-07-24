def argument_lists(*numbers):
	product = 1
	for num in numbers:
		product *= num
	return product


print(argument_lists(5, 6))
print(argument_lists(2, 2, 6, 2))