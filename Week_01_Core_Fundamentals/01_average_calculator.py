"""
TASK: 01 Average Calculator

# Average Calculator
Write a Python program that:
- Prompts the user for a list of numbers.
- Stores them in a 1D list.
- Calculates the mean *without using built-in statistics libraries*.
- Includes input validation.
- Implements a reusable function: `calculate_average(values)`.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
    pass



if __name__ == "__main__":
    number = 0
    total = 0
    mean = 0
    num = []
    addit = input("Enter a list of numbers. ")
    num = addit.split()
    lengthnum = len(num)
    for i in range(lengthnum):
        total = total + int(num[number])
        number = number + 1
    mean = total / len(num)
    print("The average is: " + str(mean))
main()
