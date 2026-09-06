# Implements the game logic, including tile movement, merging, random tile generation, and game state checks.

import random

def start_game():
    mat =[]
    for i in range(4):
        mat.append([0] * 4)

    print("Commands are as follows : ")
    print("'W' or 'w' : Move Up")
    print("'S' or 's' : Move Down")
    print("'A' or 'a' : Move Left")
    print("'D' or 'd' : Move Right")

    add_new_2(mat)
    return mat

def findemoty(mat):
    """Finds the first empty (0) cell in the grid."""
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 0:
                return (i, j)
    return None, None

def add_new_2(mat):
    """Adds a new '2' in a random empty cell in the grid."""
    if all(all(cell != 0 for cell in row) for row in mat):
        return
    tries = 0
    while tries < 30:
        r = random.randint(0, 3)
        c = random.randint(0, 3)
        if mat[r][c] == 0:
            mat[r][c] = 2
            return
        tries += 1
    r, c = findEmpty(mat)
    if r is not None and c is not None:
        mat[r][c] = 2