"""
TASK: 02 Library Item Inheritance

# This will require you understand how inheritance works
Base class: Item
Attributes: title, year
Subclasses:
- Book - add author attribute
- DVD - add director
Demonstrate polymorphism by iterating a list of mixed objects

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
    class item:
        def __init__(self, title, year):
           self.title = title
           self.year = year
    class book(item):
        def __init__(self, title, year, author):
           self.author = author
           super().__init__(title, year)
    class dvd(item):
        def __init__(self, title, year, director):
           self.director = director
           super().__init__(title, year)

    myitem = book("Harry Potter", 2026, "JK Rowling")
    print(myitem.title)
    print(myitem.year)
    print(myitem.author)
if __name__ == "__main__":
    main()
