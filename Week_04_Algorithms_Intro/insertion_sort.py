"""
TASK: 03 Insertion Sort

# Insertion Sort Tester
Generate an unsorted list (maybe use RNG). Implement:
- Insertion sort without using inbuild sorts
- Count number of comparions
Then benchmark them with random inputs.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
    import random
    lst = []
    for i in range(5):
        lst.append(random.randint(1,10))
    x = 0
    digit = lst[x]
    print(lst)
    for i in range(4):
        x = 0
        digit = lst[x]
        while x < 4:    
            temp = 0
            y = 0
            if digit > lst[1]:
                temp = lst[1]
                y = 1
                if digit > lst[2]:
                    temp = lst[2]
                    y = 2
                    if digit > lst[3]:
                        temp = lst[3]
                        y = 3
                        if digit > lst[4]:
                            temp = lst[4]
                            y = 4
                
            lst[x] = temp
            lst[y] = digit
            x = x + 1
    print(lst)    
    pass


if __name__ == "__main__":
    main()
