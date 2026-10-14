"""
TASK: 05 File Word Search

# Skills: File reading, loops, Data mining
Ask user for a filename and a search term. https://sherlock-holm.es/ascii/ is a site that has the entire collection of Sherlock Holmes
Load the file and count how many lines contain the search term

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
    recording = []
    file = open("cano.txt", "r")    
    num = 0
    word = input()
    for i in range(985):
        record = file.readline()
        recording = record.split()
        for i in range(len(recording)):
            if recording[i] == word:
                num = num + 1
    file.close() 
    print(num)

    pass

if __name__ == "__main__":
    main()