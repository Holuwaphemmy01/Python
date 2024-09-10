
fail = 0
passmark = 0
for number in range(4):
	scores = int(input('Enter student score: '))

	if scores >= 45 and scores < 100:
		passmark += 1
	elif scores < 45:
		fail += 1
print('The total number of student that pass is', passmark)
print('The total number of student that fails is', fail)
