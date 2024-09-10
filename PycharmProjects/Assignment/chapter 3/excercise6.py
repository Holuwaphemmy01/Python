print("What is your problem: ")
	
userinput = (str(input("Have you had this problem before (yes or no): ")))

correct = 'yes'
incorrect = 'no'
	
if userinput == 'yes':
	print("Well you have it again.")
		
elif userinput == 'no':
	print("Well, you have it now")
	
else:
	print("Invalid input")
