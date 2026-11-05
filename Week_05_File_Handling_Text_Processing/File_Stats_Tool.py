"""
TASK: 01 File Stats Tool

# Read a .txt file and compute:
Task:
- Number of lines
- Number of words
- Number of characters
- Most frequent word

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
    lines = 0
    words = 0
    char = 0
    freq = ""
    frequency = 0
    file = open("cano.txt", "r")
    record = file.readline()
    while record != "":
        tempwords = []
        lines += 1
        temp = record.strip(" ").split(" ")
        frequent(temp)
        for i in range(len(temp)):
            count = len(temp[i])
            char += count
        length = len(temp)
        words += length
        record = file.readline()

    def frequent(temp):
        word = [["",0]]
        for i in range(len(word)):
            if temp[i] == word [i][0]:
                word[i][0] += 1
            else:
                word.append([[temp[i], 0]])
        num = 0
        for i in range(len(word)):
            if word[i]


    print("characters = " + str(char))
    print("lines = " + str(lines))
    print("words = " + str(words))
    pass


if __name__ == "__main__":
    main()
