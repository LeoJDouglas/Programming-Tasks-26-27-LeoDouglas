"""
TASK: 01 Bankaccount Class

# Skills - https://www.w3schools.com/python/python_oop.asp Highly recommend you visit this site.
Create class with the following attributes:
- Owner
- Balance
- Log
With the following methods:
- deposit()
- withdraw() with validation or an overdraft validation
- get_balance()
- get_log() of all transactions

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
    class bankacc:
        def __init__(self, name, balance):
            self.name = name
            self.balance = balance
            self.log = []

        def getName(self):
            return self.name
    leo = bankacc("leo", 0)
    print(leo.getName())
    
    
    pass


if __name__ == "__main__":
    main()
