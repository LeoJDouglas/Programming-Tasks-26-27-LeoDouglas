"""
TASK: 04 Linear Search

# Linear Search
Implement a linear search algorithm:
- Ask the user for a target value.
- Search a generated random list.
- Return the index or -1.
- Include `linear_search(values, target)`.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
    # TODO: Write demonstration/testing code
    # If you want to delete all the code here and work just with a blank file go ahead, remember anything under the if __name__=="__main__":
    # will only run if this module is being run directly. So used this subprocedure to carry out testing if it is going to be an imported file.
    pass
import string
import random
if __name__ == "__main__":
    num = []
    list = ''.join(random.choices(string.ascii_lowercase, k=10))
    target = input("Enter the value to search for: ")
    for i in range(len(list)):
        if list[i] == target:
            num.append(i)
    print("The target value is found at index: " + str(num))

    main()