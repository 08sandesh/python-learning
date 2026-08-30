#  The game() function in a program lets a user play a game and returns the score as an integer.
#  You need to read a file "Hi-score.txt" which is either blank or contains the previous Hi-score.
#  You need to write a program to update the Hi-score whenever the game() function breaks the Hi-score. 

import random

def game():
    print("You are playing a game..")
    score = random.randint(1,100)

    with open("Hi-score.txt") as f:
        hscore = f.read()
    
    if hscore == "":
        hscore == 0
    else:
        hscore = int(hscore)

    print(f"Your score is {score}")

    if score>hscore:
        with open("Hi-score.txt","w") as f:
            f.write(str(score))

game()