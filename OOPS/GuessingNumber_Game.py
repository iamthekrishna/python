import random

class Guess_Number:
    def __init__(self):
        pass

    def Game(self,round):
      
        for x in range(round):
            num=int(input("guess the number between 1-10:\n"))
            guess = random.randint(1,10)
            score = 0

            if num > guess and num <=10:
                print("Your guess number is higher,try guess number is lower")

            elif num < guess and num > 0:
                print("Your guess number is lower,try guess number is higher")

            elif num==guess:
                print("BRINGO !!!!")
                score=100-(x*20)
                print(f"your score is {score}")
                break

            else:
                print("Invalid Number")

        if score==0:
            print("Game Over")
            print("number is",guess)
            

Game = Guess_Number()
Game.Game(5)

