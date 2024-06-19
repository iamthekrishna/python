#============================ Price Game ===============================#

import random

class Game:
    def __init__(self):
        self.Mayank = 0
        self.Pooja = 0
        self.Shraddha = 0

    def gamewin(self,a):
        for x in range(a):
            MorP = input("Who is going play: 'M' OR 'P' OR 'S': \n")
            WORL = random.choice(["W","L"])
            print(WORL)

            if WORL == "W":
                if MorP == "M":
                    self.Mayank = self.Mayank + 10000
                elif MorP == "P":
                    self.Pooja = self.Pooja + 10000
                elif MorP == "S":
                    self.Shraddha = self.Shraddha + 10000

            else:
                if MorP == "M":
                    self.Mayank = self.Mayank - 5000
                elif MorP == "P":
                    self.Pooja = self.Pooja - 5000              
                elif MorP == "S":
                    self.Shraddha = self.Shraddha - 5000

###########################################################  
            # if WORL == "W" and MorP =="M":
            #     self.Mayank = self.Mayank + 10000

            # elif WORL == "L" and MorP =="M":
            #     self.Mayank = self.Mayank - 5000
        
            # elif WORL == "W" and MorP == "P":
            #     self.Pooja = self.Pooja + 10000

            # elif WORL == "L" and MorP == "P":
            #     self.Pooja = self.Pooja - 5000
            
            # elif WORL == "W" and MorP == "S":
            #     self.Shraddha = self.Shraddha + 10000

            # elif WORL == "L" and MorP == "S":
            #     self.Shraddha = self.Shraddha - 5000
###########################################################

    def display(self):
        print(f"Price of Mayank {self.Mayank}")
        print(f"Price of Pooja {self.Pooja}")
        print(f"Price of Shraddha {self.Shraddha}")


Game = Game()
Game.gamewin(9)
Game.display()

    
    


        