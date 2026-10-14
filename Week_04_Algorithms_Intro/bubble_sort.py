"""
TASK: 01 Bubble Sort

# Bubble Sort
Implement Bubble Sort on any size list:
- Do not use built-in sort()
- Count swaps
- Extend by

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""
import random
def main():
    nums = []
    swap = 0

    for i in range(50):
        nums.append(random.randint(1, 100))
    print(nums)
    for i in range(50):    
        leftnum = 0
        rightnum = 1
        while rightnum < 50:
            left = nums[leftnum]
            right = nums[rightnum]
            if left > right:
                nums[rightnum] = left
                nums[leftnum] = right
                swap += 1
            leftnum += 1
            rightnum += 1

    print(nums)
    print(swap)
    pass


if __name__ == "__main__":
    main()
