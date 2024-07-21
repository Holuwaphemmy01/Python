def equal_string (first_string, second_string):
	
	if sorted(first_string) == sorted(second_string):
		return print("True")
	else:
		return print("False")


equal_string('femi', 'fmei')
