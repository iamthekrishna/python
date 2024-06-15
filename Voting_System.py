#Voting system
# Parties: BJP, INC, AAP, TMC, DMK, Other, NOTA
# B - BJP
# I - INC
# A - AAP
# T - TMC
# D - DMK
# O - Other
# N - NOTA
# Result : BJP ? INC ? ...
# Winner : highest result will be the winner of election
#===========================================================================

print("==============Voting System=============")
print("1)B==================BJP")
print("2)I==================INC")
print("3)A==================AAP")
print("4)T==================TMC")
print("5)D==================DMK")
print("6)O=================OTHER")
print("7)N==================NOTA")
print("8)End of voting======= ==")

print("Welcome to the Voting, please add vote the choice from 1-8 !")
Total=0
Party = {"B":0, "I":0, "A":0, "T":0, "D":0, "O":0,"N":0,}

greatest=0
winner = ""
while True:
    id=input("Enter the parties Id: ")
    if id == "B":
        Party["B"] = Party["B"] + 1
        Total = Total + 1      
    elif id=="I":
        Party["I"]=Party["I"]+1
        Total=Total+1
    elif id=="A":
        Party["A"]=Party["A"]+1
        Total=Total+1
    elif id=="T":
        Party["T"]=Party["T"]+1
        Total=Total+1
    elif id=="D":
        Party["D"]=Party["D"]+1
        Total=Total+1
    elif id=="O":
        Party["O"]=Party["O"]+1
        Total=Total+1
    elif id=="N":
        Party["N"]=Party["N"]+1
        Total=Total+1
    elif id=="E":
        break

print("BJP: "+ str(Party["B"])+ " vote")
print("INC: "+ str(Party["N"])+ " vote")
print("AAP: "+ str(Party["A"])+ " vote")
print("TMC: "+ str(Party["T"])+ " vote")
print("DMC: "+ str(Party["D"])+ " vote")
print("OTHER: "+ str(Party["O"])+ " vote")
print("NOTA: "+ str(Party["N"])+ " vote")
print("Total Voting: ", Total)

print(Party)
print("")
for PName, PVote in Party.items():
    if greatest < PVote:
        greatest = PVote
        winner = PName

print("Winner of Election 2024 is : ", winner)