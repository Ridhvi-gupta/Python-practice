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