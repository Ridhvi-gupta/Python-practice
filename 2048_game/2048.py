# This is the main driver file to run the game.
# 2048 is a single-player puzzle game in which tiles with the same value are combined to create a tile with the value 2048.
# The game can be implemented in Python using a 4×4 matrix,with all game operations performed through the console without requiring a graphical user interface (GUI)

import logic

if __name__ == '__main__':
        mat = logic.start_game()

while(True):
    x = input("Press the command : ")
    if(x == 'W' or x == 'w'):
        mat, flag = logic.move_up(mat)
        status = logic.get_current_state(mat)
        print(status)

        if(status == 'GAME NOT OVER'):
            logic.add_new_2(mat)
        else:
            break

    elif(x == 'S' or x == 's'):
        mat, flag = logic.move_down(mat)
        status = logic.get_current_state(mat)
        print(status)

        if(status == 'GAME NOT OVER'):
            logic.add_new_2(mat)
        else:
            break 

    elif(x == 'S' or x == 's'):
        mat, flag = logic.move_down(mat)
        status = logic.get_current_state(mat)
        print(status)

        if(status == 'GAME NOT OVER'):
            logic.add_new_2(mat)
        else:
            break

    elif(x == 'A' or x == 'a'):
        mat, flag = logic.move_left(mat)
        status = logic.get_current_state(mat)
        print(status)

    elif(x == 'D' or x == 'd'):
        mat, flag = logic.move_right(mat)
        status = logic.get_current_state(mat)
        print(status)

        if(status == 'GAME NOT OVER'):
            logic.add_new_2(mat)
        else:
            break

    else:
        print("Invalid Key Pressed")

    print(mat)


