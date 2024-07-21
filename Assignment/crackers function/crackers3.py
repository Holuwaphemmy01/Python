def only_floats(a, b):
	counter = 0
	if (a is float(a)):
		counter += 1
	if (b is float(b)):
		counter += 1
	if (a is not float(a) and b is not float(b)): 
		counter = 0
	return print(counter)


only_floats(10.0, 10)
only_floats(8.0, 9.8)