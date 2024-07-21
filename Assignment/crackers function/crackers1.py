def my_discount(price, discount):
	result = (price / 100) * discount
	result = price - result 
	return print('The discount on this product is', result) 
	


my_discount(150, 15)
my_discount(200, 5)
