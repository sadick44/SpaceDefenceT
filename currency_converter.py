
CURRENCIES = ('usd', 'eur', 'cad')

EXCHANGE_RATE = {
     'usd': { 'eur': 0.85, 'cad': 1.25},
     'eur': { 'usd': 1.18, 'cad': 1.47},
     'cad': { 'usd': 0.8, 'eur': 0.68},
}


def get_amount():

    while True:

        try: 
            amount = float(input('Enter the amount '))
            if amount <= 0:
                raise ValueError()
            
            else:
                 return amount
            
        except ValueError:
            print('Invalid amount ')


def get_currency(label):

    while True:
        currency = input(f'Enter {label} currency USD/EUR/CAD ').lower()
        
        if currency not in CURRENCIES:
            print('Invalid Error')

        else:
            return currency

def converting_currency(source_currency, target_currency, amount):

    if target_currency == source_currency:
        return amount

    
    return amount * EXCHANGE_RATE[source_currency][target_currency]


     
def main():
    amount = get_amount()
    source_currency = get_currency('source')  
    target_currency = get_currency('target')        
    converted_amount = converting_currency(source_currency, target_currency, amount)
    print(f'{amount} {source_currency} is equal to {converted_amount:.2f} {target_currency}')


if __name__ == '__main__': #This means that we're executing the main method only from the terminal
    main()