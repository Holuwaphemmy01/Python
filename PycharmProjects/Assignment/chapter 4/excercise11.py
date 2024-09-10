from random import randint
guess = randint(1,1000)
user_decision = 0
counter = 0
user_input = (input('Do you want to play game (Yes or No): '))
if (user_input == 'Yes' or user_input == 'yes'):

    while user_decision != 'no' and user_decision != 'No':
        user_input = int(input("Guess my number between 1 and 1000: "))
        counter += 1
        if user_input < guess:
            print('"Too low. Try again."')
        elif user_input > guess:
            print('"Too high. Try again"')
        elif user_input == guess:
            print('"Congratulations. You guessed the number!"')
            if counter < 10:
                    print('Either you know the secret or you got lucky')
            elif counter > 10:
                    print('"You should be able to do better"')
            user_decision = str(input("Enter any key to continue or 'no' to end: "))
            guess = randint(1,10)
            
            
           
        
