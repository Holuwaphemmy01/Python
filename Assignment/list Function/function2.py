def reverse_list (reverse = []):
	length = len(reverse)
	new_reverse =[reverse]
	count = 1;
	for number in range(length-1, 0, -1):
		new_reverse[count] = reverse[length-1]
		count += 1;
	return new_reverse



result = reverse_list(reverse = [1, 2, 3, 4, 5])
print(result)
	