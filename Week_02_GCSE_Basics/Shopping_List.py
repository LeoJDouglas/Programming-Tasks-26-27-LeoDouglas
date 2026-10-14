"""
TASK: 05 Shopping List

# Skills: Loops, lists
Allow the user to add items to a shopping list until they type DONE
When they type DONE, print the list and ask if they want to edit any item.
They should select an item by number and allow them to ammend the item.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
    list = []
    stop = input("Enter food for list: ")

    while stop.lower() != "done":
        print(list)
        list.append(stop)
        stop = input()
        
    edit = input("Would you like to change any of your list? ")
    if edit.lower() == "yes":
        print(list)
        num = int(input())
        
        change = input()
        list[num - 1] = change
        print(list)
        
    pass


if __name__ == "__main__":

    main()
