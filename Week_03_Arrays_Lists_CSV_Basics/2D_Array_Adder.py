"""
TASK: 03 2D Array Adder

# 2D Array Added
Create a 2D array and allow user to:
- Append new values in
- read all current values
- delete a chosen entry

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
    arr = [[""]*5 for _ in range(5)]
    choice = input("choice? ")
    if choice == "append":
        addition = input("")
        row = int(input("row? "))
        column = int(input("column? "))
        arr[row][column] = addition 
    elif choice == "read":
        for column in range(5):
            for i in range(5):
                print(arr[column][i])
    elif choice == "delete":
        row = int(input("Row?"))
        column = int(input("column? "))
        arr[row][column] = ""
    pass


if __name__ == "__main__":
    main()
