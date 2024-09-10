passes = 0
fails = 0
userinput = 0
while userinput != 1 and userinput != 2:
    userinput = int(input('Enter a number 1 or number 2: '))
    if userinput != 1 and userinput != 2:
        passes += 1
    else:
        fails += 1
        
print(passes)
print(fails)