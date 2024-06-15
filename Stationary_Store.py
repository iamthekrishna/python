print("=============== MENU ===============")
print("1) Pencil Box --------------> 60 Rs.")
print("2) Eraser Box --------------> 50 Rs.")
print("3) Sharpner Box ------------> 30 Rs.")
print("4) Pen Box -----------------> 45 Rs.")
print("5) Color Box ---------------> 65 Rs.")
 
print("Welcom to the store, please add items into cart by giving the choice from 1-5 !")
Total = 0
cart = {1:0, 2:0, 3:0, 4:0, 5:0}
while True:
    item = int(input("Enter the item you want to add into cart: "))
    quantity = int(input("Enter the quantity you want to add: "))
    if item == 1:
        cart[1] = cart[1] + quantity
        Total = Total + (60 * quantity)
    elif item == 2:
        cart[2] = cart[2] + quantity
        Total = Total + (50 * quantity)
    elif item == 3:
        cart[3] = cart[3] + quantity
        Total = Total + (30 * quantity)
    elif item == 4:
        cart[4] = cart[4] + quantity
        Total = Total + (45 * quantity)
    elif item == 5:
        cart[5] = cart[5] + quantity
        Total = Total + (65 * quantity)
    else:
        print("Enter valid item from 1-5, Thank you!")
 
    choice = input("You want to add other item into cart? Press 'Y' for continue and press 'N' for exit.")
    if choice == 'N' or choice == 'n':
        break
print("Summary            : Quantity x Price = Total ")
print("==============================")
print("Pencil Box         : " + str(cart[1]) + " x 60 = " + str(cart[1] * 60) )
print("Eraser Box         : " + str(cart[2]) + " x 60 = " + str(cart[2] * 50) )
print("Sharpner Box       : " + str(cart[3]) + " x 60 = " + str(cart[3] * 30) )
print("Pen Box            : " + str(cart[4]) + " x 60 = " + str(cart[4] * 45) )
print("Color Box          : " + str(cart[5]) + " x 60 = " + str(cart[5] * 65) )
print("==============================")
print("Your total bill is : ", Total)

print("")
print("Thanks you visit again!")
#print(cart)