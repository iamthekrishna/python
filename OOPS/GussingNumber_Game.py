import random

class Guess_Number:
    def __init__(f):
        pass

    def Game(self,round):
        for x in range(round):

            num = int(input("Guess the Number between 1 to 10: \n"))
            guess = random.randint(1,10)

            if num > guess and num <= 10:
                print("You Guess number is highrer,try to guess lower number")

            elif num < guess and num > 0:
                print("Your selected number is lower, try to hoghrt number")

            else:
                num == guess
                print("bringo")
                break
            

Game = Guess_Number()
Game.Game(6)

