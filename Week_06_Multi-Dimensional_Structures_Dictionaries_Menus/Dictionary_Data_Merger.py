"""
TASK: 02 Dictionary Data Merger

# Please refer to the python file with dictionaries in
Given two dictionaries:
- Merge them by summing matching keys
- Present them to the user

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

from Dictionary_File import supermarket_stock
from Dictionary_File import furniture_stock


def main():
    super = supermarket_stock.copy()
    super.update(furniture_stock)
    print(super)
    pass


if __name__ == "__main__":
    main()
