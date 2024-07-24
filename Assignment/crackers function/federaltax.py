filing = int( input('Enter 0 for single.\nEnter 1 for married jointly.\nEnter 2 for married filing separately.\nEnter 3 for Head of Household.\n  '))


if filing == 0:
	taxable_income = float(input("Enter your income: "))
	if taxable_income <= 8350:
		result = (taxable_income / 100) * 10 
		print(f'Your tax is ${result:.2f}')
	elif taxable_income > 8350 and taxable_income <= 33950:
		tax = taxable_income - 8350
		result = (tax / 100) * 15 + 835
		print(f'Your tax is ${result:.2f}')
	elif taxable_income > 33950 and taxable_income <= 82250:
		tax = (8350 / 100) * 10
		tax1 = (33950 - 8350) * (15/100)
		tax2 = (taxable_income - 33950) * (25/100)
		result = tax + tax1 + tax2
		print(f'Your tax is ${result:.2f}')
	elif taxable_income > 82250 and taxable_income <= 171550:
		tax = (8350 / 100) * 10
		tax1 = (33950 - 8350) * (15/100)
		tax2 = (82250 - 33950) * (25/100)
		tax3 = (taxable_income - 82250) * (28/100)
		result = tax + tax1 + tax2 + tax3
		print(f'Your tax is ${result:.2f}')
	elif taxable_income > 171550 and taxable_income <= 372950:
		tax = (8350 / 100) * 10
		tax1 = (33950 - 8350) * (15/100)
		tax2 = (82250 - 33950) * (25/100)
		tax3 = (171550 - 82250) * (28/100)
		tax4 = (taxable_income - 171550) * (33/100)
		result = tax + tax1 + tax2 + tax3 + tax4
		print(f'Your tax is ${result:.2f}')
	else:
		tax = (8350 / 100) * 10
		tax1 = (33950 - 8350) * (15/100)
		tax2 = (82250 - 33950) * (25/100)
		tax3 = (171550 - 82250) * (28/100)
		tax4 = (372950 - 171550) * (33/100)
		tax5 = (taxable_income - 372950) * (35/100)
		result = tax + tax1 + tax2 + tax3 + tax4 + tax5
		print(f'Your tax is ${result:.2f}')


if filing == 1:
	taxable_income = float(input("Enter your income: "))
	if taxable_income <= 16700:
		result = (taxable_income / 100) * 10 
		print(f'Your tax is ${result:.2f}')
	elif taxable_income > 16700 and taxable_income <= 67900:
		tax = taxable_income - 16700
		result = (tax / 100) * 15 + 1670
		print(f'Your tax is ${result:.2f}')
	elif taxable_income > 67900 and taxable_income <= 137050:
		tax = (16700 / 100) * 10
		tax1 = (67900 - 16700) * (15/100)
		tax2 = (taxable_income - 67900) * (25/100)
		result = tax + tax1 + tax2
		print(f'Your tax is ${result:.2f}')
	elif taxable_income > 137050 and taxable_income <= 208850:
		tax = (16700 / 100) * 10
		tax1 = (67900 - 16700) * (15/100)
		tax2 = (137050 - 67900) * (25/100)
		tax3 = (taxable_income - 137050) * (28/100)
		result = tax + tax1 + tax2 + tax3
		print(f'Your tax is ${result:.2f}')
	elif taxable_income > 171550 and taxable_income <= 372950:
		tax = (16700 / 100) * 10
		tax1 = (67900 - 16700) * (15/100)
		tax2 = (137050 - 67900) * (25/100)
		tax3 = (208850 - 137050) * (28/100)
		tax4 = (taxable_income - 208850) * (33/100)
		result = tax + tax1 + tax2 + tax3 + tax4
		print(f'Your tax is ${result:.2f}')
	else:
		tax = (16700 / 100) * 10
		tax1 = (67900 - 16700) * (15/100)
		tax2 = (137050 - 67900) * (25/100)
		tax3 = (208850 - 137050) * (28/100)
		tax4 = (372950 - 208850) * (33/100)
		tax5 = (taxable_income - 372950) * (35/100)
		result = tax + tax1 + tax2 + tax3 + tax4 + tax5
		print(f'Your tax is ${result:.2f}')
if filing == 2:
	taxable_income = float(input("Enter your income: "))
	if taxable_income <= 8350:
		result = (taxable_income / 100) * 10 
		print(f'Your tax is ${result:.2f}')
	elif taxable_income > 8350 and taxable_income <= 33950:
		tax = taxable_income - 8350
		result = (tax / 100) * 15 + 835
		print(f'Your tax is ${result:.2f}')
	elif taxable_income > 33950 and taxable_income <= 68525:
		tax = (8350 / 100) * 10
		tax1 = (33950 - 8350) * (15/100)
		tax2 = (taxable_income - 33950) * (25/100)
		result = tax + tax1 + tax2
		print(f'Your tax is ${result:.2f}')
	elif taxable_income > 68525 and taxable_income <= 104425:
		tax = (8350 / 100) * 10
		tax1 = (33950 - 8350) * (15/100)
		tax2 = (68525 - 33950) * (25/100)
		tax3 = (taxable_income - 68525) * (28/100)
		result = tax + tax1 + tax2 + tax3
		print(f'Your tax is ${result:.2f}')
	elif taxable_income > 104425 and taxable_income <= 186475:
		tax = (8350 / 100) * 10
		tax1 = (33950 - 8350) * (15/100)
		tax2 = (68525 - 33950) * (25/100)
		tax3 = (104425 - 68525) * (28/100)
		tax4 = (taxable_income - 104525) * (33/100)
		result = tax + tax1 + tax2 + tax3 + tax4
		print(f'Your tax is ${result:.2f}')
	else:
		tax = (8350 / 100) * 10
		tax1 = (33950 - 8350) * (15/100)
		tax2 = (68525 - 33950) * (25/100)
		tax3 = (104425 - 68525) * (28/100)
		tax4 = (186475 - 104525) * (33/100)
		tax5 = (taxable_income - 186475) * (35/100)
		result = tax + tax1 + tax2 + tax3 + tax4 + tax5
		print(f'Your tax is ${result:.2f}')
if  filing == 3:
	taxable_income = float(input("Enter your income: "))
	if taxable_income <= 11950:
		result = (taxable_income / 100) * 10 
		print(f'Your tax is ${result:.2f}')
	elif taxable_income > 11950 and taxable_income <= 45500:
		tax = taxable_income - 11950
		result = (tax / 100) * 15 + 119.50
		print(f'Your tax is ${result:.2f}')
	elif taxable_income > 45500 and taxable_income <= 117450:
		tax = (11950 / 100) * 10
		tax1 = (45500 - 11950) * (15/100)
		tax2 = (taxable_income - 45500) * (25/100)
		result = tax + tax1 + tax2
		print(f'Your tax is ${result:.2f}')
	elif taxable_income > 117450 and taxable_income <= 190200:
		tax = (11950 / 100) * 10
		tax1 = (45500 - 11950) * (15/100)
		tax2 = (117450 - 45500) * (25/100)
		tax3 = (taxable_income - 117450) * (28/100)
		result = tax + tax1 + tax2 + tax3
		print(f'Your tax is ${result:.2f}')
	elif taxable_income > 190200 and taxable_income <= 372950:
		tax = (11950 / 100) * 10
		tax1 = (45500 - 11950) * (15/100)
		tax2 = (117450 - 45500) * (25/100)
		tax3 = (190200 - 117450) * (28/100)
		tax4 = (taxable_income - 190200) * (33/100)
		result = tax + tax1 + tax2 + tax3 + tax4
		print(f'Your tax is ${result:.2f}')
	else:
		tax = (11950 / 100) * 10
		tax1 = (45500 - 11950) * (15/100)
		tax2 = (117450 - 45500) * (25/100)
		tax3 = (190200 - 117450) * (28/100)
		tax4 = (372950 - 190200) * (33/100)
		tax5 = (taxable_income - 372950) * (35/100)
		result = tax + tax1 + tax2 + tax3 + tax4 + tax5
		print(f'Your tax is ${result:.2f}')
