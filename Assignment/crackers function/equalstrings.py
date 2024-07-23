def equal_string (first_string, second_string):
	
	if sorted(first_string) == sorted(second_string):
		return True
	else: 
		return False
 
equal_string('femi', 'fmei')
equal_string('olve', 'love')