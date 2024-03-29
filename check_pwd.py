# Author:  Aaron Nesbit
# Date:    2/13/2021

def check_pwd(password):
    # Check if password meets minimum length of 8 requirement
    if len(password) < 8:
        return False

    # Check if password meets maximum length of 20 requirement
    if len(password) > 20:
        return False

    # Check if password contains at least 1 lowercase letter
    lowercase_check = False
    for char in password:
        if char.islower():
            lowercase_check = True
    if not lowercase_check:
        return False

    # Check if password contains at least 1 uppercase letter
    uppercase_check = False
    for char in password:
        if char.isupper():
            uppercase_check = True
    if not uppercase_check:
        return False

    # Check if password contains at least 1 digit
    digit_check = False
    for char in password:
        if char.isdigit():
            digit_check = True
    if not digit_check:
        return False

    # Check if password contains at least 1 of the permitted symbols
    permitted_symbols = ['~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(',
                         ')', '_', '+', '-', '=']
    permitted_symbol_check = False
    for char in password:
        if char in permitted_symbols:
            permitted_symbol_check = True
    if not permitted_symbol_check:
        return False

    return True
