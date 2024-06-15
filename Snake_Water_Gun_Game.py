import random

def gamewin(comp,you):
    if comp==you:
        return None
    elif comp=="S":
        if you=="W" or you=="w":
            return False
        elif you=="G" or you=="g":
            return True
    elif comp=="W":
        if you=="G" or you=="g":
            return False
        elif you=="S" or you=="s":
            return True
    elif comp=="G":
        if you=="W" or you=="w":
            return False
        elif you=="S" or you=="s":
            return True
        
print("comp Trun: Sanke(S), Gun(G),Water(W): ")
randNo=random.randint(1,3)
if randNo==1:
    comp="S"
elif randNo==2:
    comp="G"
elif randNo==3:
    comp="W"

you=input("your Trun: Sanke(S),Gun(G),Water(W)?: ")
a=gamewin(comp,you)

print((f"Computer choose {comp}"))
print(f"Your choose {you})")

if a==None:
    print("Game is Tie!")
elif a:
    print("You Win!")
else:
    print("You Lose")
    
    

    
