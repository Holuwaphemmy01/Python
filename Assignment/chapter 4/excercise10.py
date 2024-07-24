from random import randint
guess = randint(1,10)
user_decision = 0
counter = 0
user_input = (input('Do you want to play game (Yes or No): '))
if (user_input == 'Yes' or user_input == 'yes'):

    while user_decision != 'no' and user_decision != 'No':
        user_input = int(input("Guess my number between 1 and 10: "))
        counter += 1
        if user_input < guess:
            print('"Too low. Try again."')
        elif user_input > guess:
            print('"Too high. Try again"')
        elif user_input == guess:
            print('"Congratulations. You guessed the number!"')
                        
            
           
        
