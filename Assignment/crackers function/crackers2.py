def divide_or_square(number):
	if number % 5 == 0:
		return print(f'{number ** 0.5:.2f}')
	else:
		return print(number % 5)



divide_or_square(10)
divide_or_square(13)
divide_or_square(95)