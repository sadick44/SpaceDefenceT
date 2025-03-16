import string, sys

def services():

    list_services = {
        1: "Check Balance",
        2: "Deposit",
        3: "Withdraw",
        4: "Exit"
        }
    
    print('Welcome to the ATM!')
    
    for key, value in list_services.items():
        print(f'{key}. {value}')

def get_user_input():
    
    while True:
        try:
            user_input = int(input("Please choose an option "))
            if user_input not in [1, 2, 3, 4]:
                raise ValueError
            
            return user_input
    
        except ValueError:
            print('Please enter a valid number (1-4)')


def check_balance(balance):
    print(f'Your current balace is: ${balance}')


def deposit(balance):
    while True:
        try:
            deposit_value = float(input("Enter the amount to deposit "))

            if deposit_value <= 0:
                print('Deposit amount be positive')
                continue
            balance = balance + deposit_value

            return balance
        
        except ValueError:
            print('Please enter a valid number ')


def withdraw(balance):
    while True:
        try:
            amount_to_withdraw = input('Please the amount to withdraw ')

            if not amount_to_withdraw.isnumeric():
                print('Enter a valid amount to withdraw ')
                continue

            if float(amount_to_withdraw) <= balance:
                balance = balance - float(amount_to_withdraw)
                print(f'You have withdrew ${amount_to_withdraw}.')
                check_balance(balance)

            elif float(amount_to_withdraw) > balance:
                print("You don't have this much amount in your balance")
                continue

            return balance
        
        except ValueError:
            print("Please enter a valid amount")

def match_cases(user_choice):
     balance = 0
     match user_choice:
            case 1:
                check_balance(balance)
            case 2:
                balance = deposit(balance)
            case 3:
                balance = withdraw(balance)

def main():
    
    while True:
        print()
        services()
        user_choice = get_user_input()
        if user_choice in [1, 2, 3]:
            match_cases(user_choice)
        else: break
        
       
    
if __name__== "__main__":
    main()