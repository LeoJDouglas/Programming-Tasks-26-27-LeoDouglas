"""
TASK: 03 Multi-Dimension Array Rotation

# Rotate a 2D matrix 90 degrees clockwise
Good luck

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""
import numpy as np
def main():

    matrix = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]

    # Rotate 90 degrees Clockwise
    # 1. matrix[::-1] reverses the rows
    # 2. zip(*...) transposes rows into columns
    cw_matrix = [list(row) for row in zip(*matrix[::-1])]

    # Rotate 90 degrees Counterclockwise
    ccw_matrix = [list(row) for row in zip(*matrix)][::-1]



if __name__ == "__main__":
    main()
