userinput = int(input("Enter 5 digit number: "))
number = 0
counter = 0
while number != 5:
    number += 1
    if number == 1:
        number1 = userinput // 10000 % 10
    elif number == 2:
        number2 = userinput // 1000 % 10
    elif number == 3:
        number3 = userinput // 100 % 10
    elif number == 4:
        number4 = userinput // 10 % 10
    elif number == 5:
        number5 = userinput // 1 % 10
        
print (number1 , number2 , number3 , number4 , number5)
        
    
