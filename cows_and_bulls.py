import random

# cows if the number that are correct
# bulls if the number of digits s in the correct position

def generate_four_digits_number():

    generated_number = random.sample(range(1, 9), 4) # return a list of distinct int elements

    return int(''.join([str(x) for x in generated_number]))

def converting_number_to_list(number):
    return [int(x) for x in str(number)]


def take_guess():
    while True:
        try:
            guess_number = int(input("Guess: "))
            list_guess_number = converting_number_to_list(guess_number)

            if len(list(list_guess_number)) != 4 or len(list_guess_number) != len(set(list_guess_number)):
                raise

            return guess_number
        except:
            print('Invalid guess. Please enter a 4-digit number with unique digits.')


def bulls(user_guess, generated_number):

    counter = 0
    list_generated_number = converting_number_to_list(generated_number)
    list_user_guess = converting_number_to_list(user_guess)

    for index, value in enumerate(list_user_guess):
        if list_user_guess[index] == list_generated_number[index]:
            counter = counter + 1
    
    return counter

def cows(user_guess, generated_number):

    list_generated_number = converting_number_to_list(generated_number)
    list_user_guess = converting_number_to_list(user_guess)
    counter = 0

    for index, value in enumerate(list_user_guess):
        if value in list_generated_number:
            counter = counter + 1

    return counter


def main(): 

    generated_number = generate_four_digits_number()
    print('I have generated a 4-digit number with unique digits. Try to guess it!')
    print(f'The generated number is {generated_number} ')

    while True:

        user_guess = take_guess()
        cows_number = cows(user_guess, generated_number)
        bulls_number = bulls(user_guess, generated_number)

        if user_guess == generated_number:
            print(f'Bravo! You guessed correct!')
            break
        print(f'{cows_number} cows, {bulls_number} bulls')


if __name__=="__main__":
    main()