"""
TASK: 03 Contact Book

# Store contacts in a text file, each line containing
name,phone,email
Program must allow:
- Add contact
- Search contact (sequential search)
- Display all

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
   file = open("contacts.txt", "a+")
   file.seek(0)
   def addcontact(file):
      name = input("name: ")
      phone = input("number: ")#
      email = input("email: ")
      contact = name + "," + phone + "," + email
      file.write(contact + "\n")

   def searchcontact(file):
      line = file.readline()
      name,phone,email = line.strip(",").split(",")
      search = input("what name?")
      found = False
      while line != "" and found == False:
         if search == name:
            found = True
            print("contact found")


   def display(file):
      line = file.readline()
      while line != "":
         print(line)
         line = file.readline()

   choice = input("add / search / display? ")
   if choice == "add":
      addcontact(file)
   elif choice == "search":
      searchcontact(file)
   elif choice == "display":
      display(file)
   pass


if __name__ == "__main__":
    main()
