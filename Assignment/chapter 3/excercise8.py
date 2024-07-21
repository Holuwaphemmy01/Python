
largest = None
smallest = None
sum1 = 0
product = 1


for number in range(3):
    userinput= int(input('Enter a number: '))
    if largest is None or userinput > largest:
        largest = userinput
        
    if smallest is None or userinput < smallest:
        smallest = userinput
        
    sum1 += userinput 
    product *= userinput
average = sum1 / 3
    
        
print('The largest number is', largest)
print('The smallest number is', smallest)

print ('The total addition of the number is', sum1)
print ('The product of the numbers is', product)
        