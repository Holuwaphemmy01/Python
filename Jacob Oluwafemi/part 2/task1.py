index = 1000
count = 0
for number in range(index, 3000):
	if number % 2 == 0:
		value1 = number % 10
		value2 = number // 10
		value3 = value2 % 10 
		value4 = value2 // 10
		value5 = value4 % 10
		value6 = value4 // 10
		if value1 % 2 == 0 and value3 % 2 == 0 and value5 % 2 == 0 and value6 % 2 == 0:
			
			print(number, end=', ')

		
	
