import random


def get_starting_balance():
    while True:
        try:
            starting_balance = int(input('Enter your starting balance: $'))

            if starting_balance <= 0:
                print('Balance must a positive number and greather than zero')
                continue
            else:
                return starting_balance

        except ValueError:
            print('Please enter a valid amount ')

def get_bet_balance(starting_balance):
    while True:
        try:
            bet_balance = int(input('Enter your bet balance: $'))
            if bet_balance < 0:
                print(f'Invalid bet amount: You can bet between $1 and ${starting_balance}')

            elif bet_balance > starting_balance:
                print(f'You bet balance should be less than your starting balance. Your starting balance is {starting_balance}')

            else:
                return bet_balance
            
        except ValueError:
            print('Please enter a valid amount')


def simulate_bet():
    bet_elements = ['🍒', '🍉', '🍋', '🌽', '🍔', '🍆']
   
    return [ ''.join(random.choices(bet_elements)) for i in range(3) ]




def display_bet(bet):
    
    return ' | '.join(bet)


def main():

    starting_balance = get_starting_balance()
    print()
    print('Welcome to the Slot MAchine Game !')
    print(f'You start with a balance of ${starting_balance}.')

    while True:
        print()
        print(f'Your current balance is ${starting_balance}')
        bet_balance = get_bet_balance(starting_balance)
        simulate = simulate_bet()
        print(display_bet(simulate))

        simulate_set = set(simulate)

        if len(simulate_set) == 1:
            print(f' Congratulations! You won {bet_balance * len(simulate_set)} ')
            starting_balance = starting_balance +  len(simulate_set) * 10

        elif len(simulate_set) == 3:
            print(f'You lost ${bet_balance}')
            starting_balance = starting_balance - bet_balance

        else:
            print(f' Congratulations! You won {bet_balance * len(simulate_set)} ')
            starting_balance = starting_balance + len(simulate_set) * bet_balance - bet_balance

        checker = input('Do you want to continue ? (y/n): ')

        if checker != 'y':
            break


if __name__=='__main__':
    main()