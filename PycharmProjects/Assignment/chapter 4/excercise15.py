def multiplication_result():
	
	from random import randint
	number_one = randint(1, 9)
	number_two = randint(1, 9)
	question = 0
	correct_answer = 1
	comment = randstr("No. Please try again", "Wrong. Try once more.", "No. Keep trying.")
	 

	while (question != correct_answer):
		
		question = int(input(f"How much is {number_one} times {number_two}?\n"))
		correct_answer = number_one * number_two
	
		if correct_answer == question:
		  	result = ("Very good!")
		else:
			print (comment)
	return result



result = multiplication_result()
print(result)