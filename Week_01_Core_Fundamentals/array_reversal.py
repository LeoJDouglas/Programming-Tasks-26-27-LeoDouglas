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
    import random
    new = []
    num = random.sample(range(1, 100), 10)
    print(num)
    for i in range(len(num)):
        new.append(num[9-i])
    print(new)
    pass

if __name__ == "__main__":
    main()
