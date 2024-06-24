# Guessing the number

# chances -6
# random number 1-20
# score calculation
# play again
# hint
# game over scenario


import random

for x in range (6):
    score=0
    guess=random.randint(1,10)
    for x in range(6):
        num=int(input("guess the number between 1-10:"))
        if num > guess and num<=10:
            print("Your guess number is higher,try guess number is lower")
        elif num < guess and num > 0:
            print("Your guess number is lower,try guess number is higher")
        elif num==guess:
            print("BRINGO !!!!")
            score=100-(x*15)
            print(score)
            break
        else:
            print("Invalid Number")
    if score==0:
        print("Game Over")
        print("number is",guess)






        