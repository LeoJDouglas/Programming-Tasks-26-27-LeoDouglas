"""
TASK: 02 Binary Search Tester

# Binary Search Tester
Generate a sorted list. Implement:
- iterative binary search
- recursive binary search
Then benchmark them with random inputs.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""
import random
def main():
    nums = []
    for i in range(50):
        nums.append(random.randint(1, 100))
    nums.sort()

    origin = nums
    search = int(input("Enter a number to search for: "))

    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = (start + end) // 2

        if nums[mid] == search:
            print(f"Found {search} in the list.")
            break

        if search < nums[mid]:
            end = mid - 1
        else:
            start = mid + 1
    else:
        print(f"{search} not found.")

    pass


if __name__ == "__main__":
    main()
