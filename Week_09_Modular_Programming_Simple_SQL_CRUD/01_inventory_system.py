"""
TASK: 01 Inventory System

# This is all working around an SQLite database with a single table, all module relate to this function
Modules:
- input record module
- Caluclate averages module
- display data module
- file storage module (save as an excel file or new database)

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""
import sqlite3

def main():
    conn = sqlite3.connect("Inventory.db")
    cursor = conn.cursor()    
    #creates database file and connects to it
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS items (
            name TEXT PRIMARY KEY,
            quantity INTEGER
        )
    """)
    #creates table
    name = input()
    while name != "":
        quantity = int(input())
        cursor.execute(
        "INSERT INTO items (name, quantity) VALUES (?, ?)",
        (name, quantity)
        )
        name = input()
    #add data to table
    conn.commit()
    #saves data to the file
    cursor.execute("SELECT * FROM items")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()
    pass


if __name__ == "__main__":
    main()
