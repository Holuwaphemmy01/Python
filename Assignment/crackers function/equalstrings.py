




def equal_strings(first_string, second_string):
	import re
	first_compare = re.compile('first_string')
	if re.search(second_string, first_compare) is True:
		return (second_string, first_compare)
	else:
		return print('False')
	

equal_strings('femi', 'femi')
