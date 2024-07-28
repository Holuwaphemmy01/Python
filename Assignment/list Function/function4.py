def odd_position(userinput_list):
	length = len(userinput_list)
	odd_number = []
	for number in range(length-1, 0, -1):
		if number % 2 != 0:
			print(userinput_list[number])



print(odd_position([12, 3, 5, 67, 45, 36]))

			
	