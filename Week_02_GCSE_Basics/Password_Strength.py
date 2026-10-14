"""
TASK: 04 Password Strength

# Skills: Strings, loops, selection
Ask the user to enter a password, and check that they meet these conditions:
- At least 8 characters
- Contains a number
- Contains a captial and lower cased letter
- Extend for one special character
Print a response of weak, medium or strong for how many they pass.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
    length = False
    number = False
    capital = False
    lower = False
    special = False
    password = input("Enter a password: ")
    if len(password) >= 8 :
        length = True
    for i in range(len(password)):
        if password[i] == "0" or password[i] == "1" or password[i] == "2" or password[i] == "3" or password[i] == "4" or password[i] == "5" or password[i] == "6" or password[i] == "7" or password[i] == "8" or password[i] == "9":
            number = True
        if password[i] != password[i].lower():
            capital = True
        if password[i] != password[i].upper():
            lower = True
        if password[i] == "!" or password[i] == "@" or password[i] == "#" or password[i] == "$" or password[i] == "%" or password[i] == "^" or password[i] == "&" or password[i] == "*" or password[i] == "(" or password[i] == ")" or password[i] == "-" or password[i] == "+":
            special = True
    if length == True and number == True and capital == True and lower == True and special == True:
        print("Strong")
    elif length == True and number == True and capital == True and lower == True:
        print("Medium")
    pass
if __name__ == "__main__":
    main()
