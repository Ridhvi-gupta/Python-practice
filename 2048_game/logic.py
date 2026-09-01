# Implements the game logic, including tile movement, merging, random tile generation, and game state checks.

import random

def start_game():
    mat =[]
    for i in range(4):
        mat.append([0] * 4)

    print("Commands are as follows : ")