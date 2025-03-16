import re
# very weak if the password is less 8 characters
# weak if password has more 8 characters
# medium if len(password) >= 8 and has an uppercase character
# Strong: if len(password) >= 8 and has an uppercase letter and has as well a lower case letter
# Very strong: Strong + special character(!, ? @,# ....)

LENGHT = 0

def password_checker(password):
    size = len(password)
    is_upper = True if sum([1 for i in password if i.isupper()]) > 0 else False
    is_lower = True if sum([1 for i in password if i.lower()]) > 0 else False
    has_special_character = bool(re.search(r'[^a-zA-Z0-9]', password))

    if size < 8:
        LENGHT = 0
        print("Password Strength: Very Weak")

    elif size >= 8 and not is_lower and not is_upper and not has_special_character :
        LENGHT = 1
        print("Password Strength: Weak")
    
    elif size >= 8 and is_upper and not is_lower and not has_special_character:
        LENGHT = 2
        print("Password Strength: Medium")

    elif size >= 8 and is_upper and is_lower and not has_special_character:
        LENGHT = 3
        print("Password Strength: Strong")

    elif size >= 8 and is_upper and is_lower and has_special_character:
        LENGHT = 4
        print("Password Strength: Very Strong")


def main():
    password = input('Enter password: ').strip()
    password_checker(password)


if __name__== '__main__':
    main()