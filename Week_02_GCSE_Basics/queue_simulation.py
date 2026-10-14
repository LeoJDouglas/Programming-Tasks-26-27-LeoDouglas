"""
TASK: 03 Queue Simulation

# Queue Simulation using OOP
Make a Queue class with:
- enqueue, dequeue, peek, size  
Simulate customers joining/leaving.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
    peek = 4
    length = 4
    queue = ["josh", "chris", "dan", "harry"]
    answer = input()
    while answer.lower() == "yes":
        queue.remove(queue[3])
        name = input()
        queue.insert(0, name)
        if peek < length:
            peek = length
        print(queue)
        print(peek)    
        answer = input()
    
    pass


if __name__ == "__main__":
    main()
