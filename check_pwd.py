# Author:  Aaron Nesbit
# Date:    2/13/2021
# Course:  CS362-400-W2021
# Program: Activity 2 - TDD

def check_pwd(password):
    # Check if password meets minimum length of 8 requirement
    if len(password) < 8:
        return False
    
    return True
