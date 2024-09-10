def equal_string (first_string, second_string):
	
	if sorted(first_string) == sorted(second_string):
		return True
	else: 
		return False
 
result = qual_string('femi', 'fmei')
print(result)
result = equal_string('olve', 'love') 
print(result)