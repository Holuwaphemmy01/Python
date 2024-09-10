def my_discount(price, discount):
	result = (price / 100) * discount
	result = price - result 
	return print('The discount on this product is', result) 
	
 

result = my_discount(150, 15)
print(result)
result = my_discount(200, 5)
print(result)
