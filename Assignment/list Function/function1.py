def largest_element (largest = []):
	length = len(largest)
	largest_number = 0
	for number in range(1, length):
		if largest[number] > largest_number:
			largest_number = largest[number]
	return largest_number




result = largest_element(largest = [46, 4, 56, 76, 34, 67, 67, 34, 790, 645, 678, 342,])
print(result)