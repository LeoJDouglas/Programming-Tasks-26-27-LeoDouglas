"""
TASK: 03 Array Reversal

# Array Reversal
Create a program that:
- Generates a list of random integers.
- Reverses the list manually (no slicing or .reverse).
- Includes a function `reverse_list(values)` that returns a new reversed list.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
    # TODO: Write demonstration/testing code
    # If you want to delete all the code here and work just with a blank file go ahead, remember anything under the if __name__=="__main__":
    # will only run if this module is being run directly. So used this subprocedure to carry out testing if it is going to be an imported file.
    pass

import random

if __name__ == "__main__":
    new = []
    num = random.sample(range(1, 100), 10)
    print(num)
    for i in range(len(num)):
        new.append(num[9-i])
    print(new)

    main()
