#This method is for implementing a dice roll

import random

# def getChoice():

#     tracker = 0
#     ntime = int(input("How many times you want to roll ? "))
#     while tracker < ntime:
    
#         dice1 = random.randint(1, 6)
#         dice2 = random.randint(1, 6)

#         print(f"Roll: {tracker+1}")
#         print(f"You rolled: ({dice1}, {dice2})")
#         tracker += 1


# getChoice()


""" def guessing_number():

    number_to_guess = random.randint(1, 100)
    counter = 0

    while True:

        guessing_number_entered = input("Enter a number between 1 and 100: ")

        if  not guessing_number_entered.isnumeric():
            print("Enter a valid number")

        elif int(guessing_number_entered) < number_to_guess:
            print("Too low !")

        elif int(guessing_number_entered) > number_to_guess:
            print("Too high !")
        
        elif int(guessing_number_entered) == number_to_guess:
            print(f"Wow you find it in {counter} trials !!")
            break
        
        counter = counter + 1


guessing_number() """


def get_user_choice(sequence):
        
        user_choice = input("Rock, peper, scissors? (r/p/s) ").lower()
        if user_choice  in sequence:
           return user_choice
        
        else:
             print("Invalid Choice!!")

def displaying_choices(user_choice, computer_choice):

    print(f"You chose {user_choice}")
    print(f"Computer chose {computer_choice}")


def determine_winner(user_choice, computer_choice):
    if (
            (computer_choice == 's' and user_choice == 'p') or 
             (computer_choice == 'p' and user_choice == 'r') or 
             (computer_choice == 'r' and user_choice == 's')):
             print("You lose")
        
    elif computer_choice == user_choice:
            print("It's a tie. Try again!")

    else:
            print("Congratulations! You won!")



def rock_paper_scissor():
    sequence = ("r", "p", "s")

    while True:

        user_choice = get_user_choice(sequence)

        machine_choice = random.choice(sequence)

        displaying_choices(user_choice, machine_choice)

        determine_winner(user_choice, machine_choice)

        should_continue = input('Do you want to continue ? y/n: ').lower()
        if should_continue == 'n':
            break

rock_paper_scissor()