total_student = int(input("Enter total number of student: "))
total_subject = int(input("Enter total number of subject: "))
student = [[total_student],[total_subject]]


for index in range(0, total_student):
	for element in range(0, total_subject):	
		print('Entering score for student',index + 1)
		student[index][element] = int(input('Enter score for subject'))
	