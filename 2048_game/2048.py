# This is the main driver file to run the game.

import logic

if __name__ == '__main__':
        mat = logic.start_game()

while(True):
    x = input("Press the command : ")
    if(x == 'W' or x == 'w'):
        mat, flag = logic.move_up(mat)
        status = logic.get_current_state(mat)
        print(status)

        if