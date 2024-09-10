counter = 0
largest = 0
second_largest = 0

for number in range(10):
    counter += 1
    user_input = int(input('Enter number: '))
    
    if user_input > largest:
        second_largest = largest
        largest = user_input
    elif user_input < largest and user_input > second_largest:
        second_largest = user_input
        
print ('The largest number is', largest)
print ('The second largest is', second_largest)
        
    