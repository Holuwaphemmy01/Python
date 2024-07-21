priceofcar = int (input("Enter price of your car: "))

if priceofcar < 1_000_000:
	tax = priceofcar / 100
	roadtax = tax * 10
	print(f'Your road tax is {roadtax}')
    
elif priceofcar >= 1_000_000 and  3_000_000:
	tax = priceofcar / 100
	roadtax = tax * 15
	print(f'Your road tax is {roadtax}')
    
elif priceofcar > 3_000_000 and 5_000_000:
	tax = priceofcar / 100
	roadtax = tax * 20
	print(f'Your road tax is {roadtax}')
     
elif priceofcar > 5_000_000:
	tax = priceofcar / 100
	roadtax = tax * 25
	print(f'Your road tax is {roadtax}')

    


