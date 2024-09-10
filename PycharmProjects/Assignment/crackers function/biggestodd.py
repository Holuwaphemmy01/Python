def biggest_odd (numbers):
	biggest = None
	for digit in numbers:
		num = int(digit)
		if num % 2 != 0:
			if biggest is None or num > biggest:
				biggest = num

	return biggest


		
result = biggest_odd("23569")
print(result)