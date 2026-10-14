"""
TASK: 06 Simple Login

# Skills: Selection, string comparison
Start with a correct username/password (extend if saved in a text file separately):
- Ask for login
- Print "Welcome" or "Access Denied {number} attempts remaining"
Only allow 3 attempts and close the file

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
    user = "chris"
    password = "beer" 
    attempts = 1
    while attempts < 3:
        userenter = input("Username: ")
        passenter = input("Password: ")
        if userenter == user and passenter == password:
            print("Welcome")
            attempts = 50
        else:
            attemptsleft = 3 - attempts
            print("Access denied, you have", attemptsleft, "left.")
            attempts = attempts + 1
            print()


if __name__ == "__main__":
    main()
