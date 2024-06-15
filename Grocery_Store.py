print("============Menu=============")
print("1)Rice=================100.Rs")
print("2)Flour================040.Rs")
print("3)Dal==================180.Rs")
print("4)Coffee===============600.Rs")    
print("5)Tea==================400.Rs")
print("6)Sugar================045.Rs")
print("7)Oil==================180.Rs")

print("Welcome to the store, please add items into cart by giving the choice from 1-7 !")
Total = 0
cart = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0,7:0}
while True:
    item = int(input("Enter the item you want to add into cart: "))
    quantity = int(input("Enter the quantity you want to add: "))
    if quantity < 0:
        print("Enter the valid quantity: ")
    elif item==1:
        cart[1] = cart[1] + quantity
        Total = Total + (100*quantity)
    elif item==2:
        cart[2] = cart[2] + quantity
        Total = Total + (40*quantity)
    elif item==3:
        cart[3] = cart[3] + quantity
        Total = Total + (180*quantity)
    elif item==4:
        cart[4] = cart[4] + quantity
        Total = Total + (600*quantity)
    elif item==5:
        cart[5] = cart[5] + quantity
        Total = Total + (400*quantity)
    elif item==6:
        cart[6] = cart[6] + quantity
        Total = Total + (45*quantity)
    elif item==7:
        cart[7] = cart[7] + quantity
        Total = Total + (180*quantity)
    else:
        print("Enter valid item from 1-5, Thank you!")

    choice = input("You want to add other item into cart? Press 'Y' for continue and press 'N' for exit.")
    if choice == "N" or choice == "n":
        break
print("Summary            : Quantity x Price = Total ")
print("1)Rice             :" + str(cart[1]) + " x " + "100 = " + (str(cart[1]*100)))
print("2)Flour            :" + str(cart[2]) + " x " + "040 = " + (str(cart[2]*40)))
print("3)Dal              :" + str(cart[3]) + " x " + "180 = " + (str(cart[3]*180)))
print("4)Coffee           :" + str(cart[4]) + " x " + "600 = " + (str(cart[4]*600)))
print("5)Tea              :" + str(cart[5]) + " x " + "400 = " + (str(cart[5]*400)))
print("6)Sugar            :" + str(cart[6]) + " x " + "045 = " + (str(cart[6]*45)))
print("7)Oil              :" + str(cart[7]) + " x " + "180 = " + (str(cart[7]*180)))
print("======================================")
print("Your total bill is : ", Total)

print("")
print("Thanks you visit again!")


    
        




    

