"""
TASK: 02 Times Tables

# Skills: Loops,input validation
Ask the user for a number, print the multiplication from 1 to 12 in a readable format:

Extend by using a function you can call for easy entry

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
    enter  = 0
    correct = 0
    num = int(input())
    def multiply(num):
        for i in range(1,13):
            print(num, "*", i)
            correct = i * num
            enter = int(input())
            if correct == enter:
                print("Correct")
            else:
                print("Wrong")

    
    multiply(num)

    pass


if __name__ == "__main__":
    main()
