"""
TASK: 02 Simple Logger System

# Create a script that appends time-stamped log entries to a file.
Menu:
- Add Log
- View Log
- Clear Log

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():


    def add():
        file = open("logs.txt", "a+")
        text = input("what would you like to add")
        time = input("what is the time")
        log = text + "," + time
        file.write(log + "\n")
        file.close()

    def view():
        file = open("logs.txt", "r")
        record = file.readline()
        print(record)
        while record != "":
            print(record)
            record = file.readline()
        file.close()

    def clear():
        file = open("logs.txt", "w")
        file.close()

    choice = input("add / view / clear? ")
    while choice != "":
        if choice == "add":
            add()
        elif choice == "view":
            view()
        elif choice == "clear":
            clear()
        choice = input("add / view / clear? ")

    pass


if __name__ == "__main__":
    main()
