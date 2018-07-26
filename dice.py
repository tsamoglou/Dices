import random as rm
import pandas as pd


def numInput():
    number = input("Tell me a number: ")
    if number.isdigit():
        return number
    else:
        print
        "You must enter a number (i.e. 0,1,2...)"
        numInput()


name = input("Hello! Please tell me your name?")

times_to_play = int(numInput())

labels=['Round','Winer']
round= [i for i in range(0, times_to_play)]
winner=[]
for i in range(0, times_to_play):
    print("Round:", i)
    input("Press a Key to Play:.... ")
    dice_1 = rm.randint(1, 6)
    dice_2 = rm.randint(1, 6)
    print("Your dices are %d ,%d" % (dice_1, dice_2))
    input("Press a Key to Continue:....")
    pcdice_1 = rm.randint(1, 6)
    pcdice_2 = rm.randint(1, 6)
    print("My dices are %d,%d" % (pcdice_1, pcdice_2))
    if dice_1 + dice_2 > pcdice_2 + pcdice_1:
        print("You win\n")
        winner.append(name)
    elif dice_1 + dice_2 == pcdice_2 + pcdice_1:
        print("DRAW\n")
        winner.append("draw")
    else:
        print("I win\n")
        winner.append("Computer")

zipped=list(zip(labels,[round,winner]))
win_table=pd.DataFrame(dict(zipped))
print(win_table)
