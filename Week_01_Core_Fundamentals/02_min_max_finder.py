"""
TASK: 02 Min Max Finder

# Min/Max Finder
Write a program that:
- Accepts a list of integers.
- Manually finds the min and max (no built-in min/max).
- Includes a function `find_min_max(values)` returning `(min_value, max_value)`.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
    # TODO: Write demonstration/testing code
    # If you want to delete all the code here and work just with a blank file go ahead, remember anything under the if __name__=="__main__":
    # will only run if this module is being run directly. So used this subprocedure to carry out testing if it is going to be an imported file.
    pass


if __name__ == "__main__":
    num = []
    lis = input("Enter a list of numbers. ")
    num = lis.split()
    smlnum = int(num[0])
    number = int(num[0])
    for i in range(len(num)):
        if int(num[i]) > number:
            number = int(num[i])
    for i in range(len(num)):
        if int(num[i]) < smlnum:
            smlnum = int(num[i])
    print("The largest number is: " + str(number))
    print("The smallest number is: " + str(smlnum))

























    main()
