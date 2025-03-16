import random
import string

def password_generator(password):
    password = int(password)
    generated_password = []

    while True:

        uppercase = input('Include uppercase letters (y/n) ?').lower()

        if uppercase == 'y':
            generated_password.append(random.choice(string.ascii_uppercase))
        
        lowercase = input('Include lowercase letters (y/n) ?').lower()

        if lowercase == 'y':
            generated_password.append(random.choice(string.ascii_lowercase))

        digits = input('Include special character (y/n) ?').lower()

        if digits == 'y':
            generated_password.append(random.choice(string.digits))


def main():
    password = input('Enter password length: ')

if __name__== "__main__":
    main()