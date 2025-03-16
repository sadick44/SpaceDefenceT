class Atm:
    def __init__(self, balance):
        self.balance = balance
    

    def services(self):

        list_services = {
            1: "Check Balance",
            2: "Deposit",
            3: "Withdraw",
            4: "Exit"
            }
        
        print('Welcome to the ATM!')
        
        for key, value in list_services.items():
            print(f'{key}. {value}')


    def get_user_input(self):
    
        while True:
            try:
                user_input = int(input("Please choose an option "))
                if user_input not in [1, 2, 3, 4]:
                    raise ValueError
                
                return user_input
        
            except ValueError:
                print('Please enter a valid number (1-4)')

    def check_balance(self):
        print(f'Your current balace is: ${self.balance}')


    def deposit(self):
        while True:
            try:
                deposit_value = float(input("Enter the amount to deposit "))

                if deposit_value <= 0:
                    print('Deposit amount must be positive')
                    continue

                self.balance = self.balance + deposit_value

                return self.balance
            except ValueError:
                print("Please enter a valid amount")


    def withdraw(self):
        
        while True:
            try:
                amount_to_withdraw = input('Please the amount to withdraw ')

                if not amount_to_withdraw.isnumeric():
                    print('Enter a valid amount to withdraw ')
                    continue

                if float(amount_to_withdraw) <= self.balance:
                    self.balance = self.balance - float(amount_to_withdraw)
                    print(f'You have withdrew ${amount_to_withdraw}.')
                    self.check_balance()

                elif float(amount_to_withdraw) > self.balance:
                    print("You don't have this much amount in your balance")
                    continue

                return self.balance
            
            except ValueError:
                print("Please enter a valid amount")


    def match_cases(self, user_choice):

        match user_choice:
                case 1:
                    self.check_balance()
                case 2:
                    self.deposit()
                case 3:
                    self.withdraw()


def main():
    atm = Atm(0)
    while True:
        print()
        atm.services()
        user_choice = atm.get_user_input()
        if user_choice in [1, 2, 3]:
            atm.match_cases(user_choice)
        else: break
        
       
    
if __name__== "__main__":
    main()