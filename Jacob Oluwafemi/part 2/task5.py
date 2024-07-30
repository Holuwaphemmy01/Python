def reverse(number):
	value1 = number % 10
	value2 = number // 10
	value3 = value2 % 10
	value4 = value2 // 10
	result = str(value1)+ str(value3) + str(value4)
	return result




def is_palindrome(number):
	value1 = number % 10
	value2 = number // 10
	value3 = value2 % 10
	value4 = value2 // 10
	if value4 == value1:	
		result = "True"
	if value4 != value1:
		result = "False"
	return result

print(reverse(656))
print(is_palindrome(656))