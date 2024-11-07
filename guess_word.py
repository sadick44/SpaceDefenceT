import random
import string


def choose_random_word(lines):
    return random.choice(lines)


def user_input():

       while True:
           try:
                guess = input('Guess: ')
                if len(guess) != 1:
                    raise
                if guess.lower() not in list(string.ascii_lowercase):
                    print('Enter only letters from A to Z')

                return guess
           except:
                print('Enter just a letter')


def display_word(generated_word, empty_word, guess):
    if guess in generated_word:
        empty_word.replace('-', guess.lower())

    return empty_word
            


def main():

    lines = []
    counter = 0

    with open ('dosh1.txt') as filename:
        for line in filename:
            lines.append(line.strip())


    generated_word = choose_random_word(lines)

    print(f'The word is: {generated_word}')

    empty_word = ''.join(['-' for word in generated_word])

    print(empty_word)


    while True:
        guess = user_input()

        print(display_word(generated_word, empty_word, guess))

        counter = counter + 1
        

if __name__== '__main__':
    main()