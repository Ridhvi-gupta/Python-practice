import random # Importing the random module to generate random numbers

def game():
    print("you are playing the game")
    score = random.randint(1, 62)
    # Fetch the hiscore
    with open("hiscore.txt") as f:
        hiscore = f.read()
        if(hiscore!=""):
            hiscore = int(hiscore)
        else:
            hiscore = 0

     
    print(f"your score is {score}")
    if(score>hiscore):
        # write this high score to the file
        with open("hiscore.txt", "w") as f:
            f.write(str(score))
# It will get replace and not append
            
    return score # Returns a random integer between 1 and 62

game() 