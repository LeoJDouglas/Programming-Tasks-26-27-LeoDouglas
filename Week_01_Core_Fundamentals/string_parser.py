"""
TASK: 05 String Parser

# String Parser
Write a parser that:
- Accepts a sentence from the user.
- Splits it into words manually (not using split()).
- Outputs number of words + list of words.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
    sentence = input("Enter a sentence: ")
        word = []
        currentword = ""
        for i in sentence:
            if i == " ":
                word.append(currentword)
                currentword = ""
            else:
                currentword += i
        print("The number of words is: " + str(len(word)))
        print("The list of words is: " + str(word))
    pass


if __name__ == "__main__":
    





    main()
