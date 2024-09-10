import datetime

customers_name = (input("Whats is the customer's Name: "))
 
goods = []
quantities = []
price = []
total = [] 

more_items = "yes"
while more_items.lower() == "yes":
	name_of_good = input("What did the user buy: ")
	goods.append(name_of_good)
	quantity = int(input("How many pieces: "))
	quantities.append(quantity)
	cost = int(input("How much is one unit: "))
	price.append(cost)
	total_per_total = quantity * cost
	total.append(total_per_total)
	more_items = input("Add more items(Yes or No): ")
	

discount = int(input("How much discount will "+customers_name+ " get: "))
cashier_name = input("Whats is your name: ")

address = """
SEMICOLON STORES 
MAIN BRANCH
LOCATION: 332, HERBERT MACAULAY WAY, SABO YABA, LAGOS.
TEL: 03293828343"""

current_date = datetime.datetime.now()
print (f"{address}\nDate: {current_date}\nCashier: {cashier_name}\nCustomer Name: {customers_name}")

for index in range(75):
	print("=", end="")	
print(f"\n\t\t\tITEM\t\tQTY\tPRICE\t\tTOTAL(NGN)")

for index in range(75):
	print("-", end="")
for index in range(len(goods)):
	print(f"\n\t\t\t{goods[index]}\t\t{quantities[index]}\t{price[index]}\t\t{total[index]}")

for index in range(75):
	print("-", end="")
sub_total = 0
for index in range(len(goods)):
	sub_total += total[index]

new_discount = (sub_total / 10) * discount

vat = (sub_total / 100) * 17.50

print(f"\n\t\t\t\tSub Total : \t{sub_total}\n\t\t\t\tDiscount : \t{new_discount}\n\t\t\t\tVAT @ 17.50%: \t{vat:.2f}")

for index in range(75):
	print("=", end="")	

bill_total = sub_total + vat - new_discount

print(f"\n\t\t\t\tBill Total: \t{bill_total}")

for index in range(75):
	print("=", end="")	

print(f"\nTHIS IS NOT AN RECIEPT KINDLY PAY {bill_total}")

for index in range(75):
	print("=", end="")


customer_payment = int(input("\nHow much did the customer gives you: "))

balance_payment = 0
if(customer_payment >= bill_total):
	balance_payment = customer_payment - sub_total
	print (f"{address}\nDate: {current_date}\nCashier: {cashier_name}\nCustomer Name: {customers_name}")

	for index in range(75):
		print("=", end="")	
	print(f"\n\t\t\tITEM\t\tQTY\tPRICE\t\tTOTAL(NGN)")

	for index in range(75):
		print("-", end="")
	for index in range(len(goods)):
		print(f"\n\t\t\t{goods[index]}\t\t{quantities[index]}\t{price[index]}\t\t{total[index]}")

	for index in range(75):
		print("-", end="")
	sub_total = 0
	for index in range(len(goods)):
		sub_total += total[index]

	
	print(f"\n\t\t\t\tSub Total : \t{sub_total}\n\t\t\t\tDiscount : \t{new_discount}\n\t\t\t\tVAT @ 17.50%: \t{vat:.2f}")

	for index in range(75):
		print("=", end="")	


	print(f"\n\t\t\t\tBill Total: \t{bill_total}\n\t\t\t\tAmount Paid: \t{customer_payment}\n\t\t\t\tBalance: {balance_payment}")

	for index in range(75):
		print("=", end="")	

	print("\nTHANK YOU FOR YOUR PATRONAGE.")

	for index in range(75):
		print("=", end="")
else: 
	print("\nInsufficient Amount.")




