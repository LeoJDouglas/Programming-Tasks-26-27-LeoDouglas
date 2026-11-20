"""
TASK: 01 Grade Writer

# Purpose is to write a grade uploading program for csv files
Ask the user for student names and ages, with a keyword to stop.
Writes all entries to a .txt file and .csv file separately

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
    txt = open("grades.txt", "w")
    csv = open("grades.csv", "w")
    name = input("what is their name? ")
    while name != "stop":
        grade = input("what is the grade? ")
        temp = name + " " + grade
        txt.write(temp + "\n")
        csv.write(temp + "\n")
        name = input("what is their name? ")
    txt.close()
    csv.close()


    pass


if __name__ == "__main__":
    main()
