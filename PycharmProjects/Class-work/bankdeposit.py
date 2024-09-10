withdraw = 0
accountbalance = 0
prompt = 0
deposit = 0


while prompt != -1:
	prompt = int(input('Enter 1 to deposit or enter 2 to withdraw or enter 3 to check balance or -1 to end: '))
	if prompt == 1: 
		deposit = int(input('Enter amount to deposit: '))
		if deposit < 0:
			print('invalid amount')
		else:
			accountbalance += deposit

	elif prompt == 2:
		withdraw = int(input('Enter amount to withdraw: '))
		if withdraw > accountbalance:
			print('invalid amount')
		elif withdraw < 0:
			print('invalid amount')
		else:
			accountbalance -= withdraw
	elif prompt == 3:
		print(accountbalance)

	elif prompt == -1:
		break
	else:
		break


