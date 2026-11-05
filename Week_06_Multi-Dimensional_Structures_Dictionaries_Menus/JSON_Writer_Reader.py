"""
TASK: 05 Json Writer Reader

# Do some research into JSON
Prompt user for:
- Name
- Price
- Quantity
Store items into a JSON file with proper formatting
Then allow the user to open and convert to list of dictionaries and output the summary with averages.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""
import json
def main():
    file = open("writeread.json", "a")
    name = input("Name? ")
    price = input("Price? ")
    Quantity = input("Quantity? ")
    pass


if __name__ == "__main__":
    main()
