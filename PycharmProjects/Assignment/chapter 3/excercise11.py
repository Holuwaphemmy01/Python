gallon_used = 0
while gallon_used != -1:
    
    gallon_used = int(input('Enter the gallons used (-1 to end): '))
    if gallon_used == -1:
        break
    miles_driven = int (input('Enter the miles driven: '))
    miles_gallon = miles_driven / gallon_used
    print ('The miles/gallon for this tank was', miles_gallon)