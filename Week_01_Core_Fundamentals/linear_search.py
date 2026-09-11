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
    mport string
    import random
    if __name__ == "__main__":
        num = []
        list = ''.join(random.choices(string.ascii_lowercase, k=10))
        target = input("Enter the value to search for: ")
        for i in range(len(list)):
            if list[i] == target:
                num.append(i)
        print("The target value is found at index: " + str(num))
    pass
if __name__ == "__main__":   
    main()