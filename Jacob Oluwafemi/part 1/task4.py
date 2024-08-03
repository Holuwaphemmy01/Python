#prompt the user to input the value for subtotal and gravity.
#divide the gravity value by 10 and assign it to a variable name by itself.
#add subtotal value with the gravity.
#print subtotal and subtotal.



sub_total = int(input("Enter value for total: "))
grativity_rate = int(input("Enter value for gravity rate: "))

grativity_rate = grativity_rate / 10
sub_total = sub_total + grativity_rate

print(f'New value gravity rate is {grativity_rate}.\nNew value for total is {sub_total}.')