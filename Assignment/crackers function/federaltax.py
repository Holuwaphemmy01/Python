filing = print(int(input('Enter 0 for single.\nEnter 1 for married jointly.\nEnter 2 for married filing separately.\nEnter 3 for Head of Household.\n')))


if filing != (0):
	taxable_income = print(int(input("Enter your income: ")))
	if taxable_income <= 8350:
		print(taxable_income / 100) * 10 
	elif taxable_income > 8350 and taxbable_income <= 33951:
		tax = taxable_income - 8350
		print(tax / 100) * 15 + 835
	elif taxable_income > 33950 and taxable_income <= 82250:
		tax = (8350 / 100) * 10
		tax1 = (33950 - 8350) * (15/100)
		tax2 = (taxable_income - 33950) * (25/100)
		print(tax + tax1 + tax2)
	elif taxable_income > 82250 and taxable_income <= 171550:
		tax = (8350 / 100) * 10
		tax1 = (33950 - 8350) * (15/100)
		tax2 = (82250 - 33950) * (25/100)
		tax3 = (taxable_income - 82250) * (28/100)
		print (tax + tax1 + tax2 + tax3)
	elif taxable_income > 171550 and taxable_income <= 372950:
		tax = (8350 / 100) * 10
		tax1 = (33950 - 8350) * (15/100)
		tax2 = (82250 - 33950) * (25/100)
		tax3 = (171550 - 82250) * (28/100)
		tax4 = (taxable_income - 171550) * (33/100)
		print (tax + tax1 + tax2 + tax3 + tax4)
	elif taxable_income > 372950:
		tax = (8350 / 100) * 10
		tax1 = (33950 - 8350) * (15/100)
		tax2 = (82250 - 33950) * (25/100)
		tax3 = (171550 - 82250) * (28/100)
		tax4 = (372950 - 171550) * (33/100)
		tax5 = (taxable_income - 372950) * (35/100)
		print(tax + tax1 + tax2 + tax3 + tax4 + tax5)
		


		
		