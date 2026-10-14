
#TASK: 01 Csv Writer

# Skills: CSV writing
#- Ask the user for:
#- Name
#- age
#- favourite colour
#- anything you want
#Append this to a CSV file (Extend: allow user to choose to edit the file and read the file)

#TODO:

def main():
    name = input("name")
    age = input("age")
    favcolour = input("fav colour")
    any = input("anything you want")
    filename = input("file name")
    file = open(filename + ".csv", "a")
    file.write(name)
    file.write(" , ")
    file.write(age)
    file.write(" , ")
    file.write(favcolour)
    file.write(" , ")
    file.write(any)
    pass


if __name__ == "__main__":

        main()
