print("=========Electronic Items List=========")
print("1).Washing Machine           Rs.40,000")
print("2).Telivision                Rs.45,000")  
print("3).Laptop                    Rs.80,000")
print("4).Refrigerator              Rs.45,000")
print("5).Air Conditinoning         Rs.40,000")
print("6).Fan                       Rs.10,000")
print("7).Microwave                 Rs.20,000")
print("8).Electric Grinder          Rs.05,000")
print("9).Toaster                   Rs.05,000")
print("10).Iron                     Rs.02,000")

print("Welcom to the store, please add items into cart by giving the choice from 1-10 !")

class Showroom:
    def __init__(self):
        self.cart = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0}
        self.Total = 0
        
    def Electronic_item(self):
        while True:
            item = int(input("Enter the item you want to add into cart:\n "))
            Qty = int(input("Enter the quantity you want to add: \n"))

            if item == 1:
                self.cart[1] = self.cart[1] + Qty
                self.Total = self.Total + (40000 * Qty)

            elif item == 2:
                self.cart[2] = self.cart[2] + Qty
                self.Total = self.Total + (45000 * Qty)

            elif item == 3:
                self.cart[3] = self.cart[3] + Qty
                self.Total = self.Total + (80000 * Qty)

            elif item == 4:
                self.cart[4] = self.cart[4] + Qty
                self.Total = self.Total + (45000 * Qty)

            elif item == 5:
                self.cart[5] = self.cart[5] + Qty
                self.Total = self.Total + (40000 * Qty)

            elif item == 6:
                self.cart[6] = self.cart[6] + Qty
                self.Total = self.Total + (10000 * Qty)

            elif item == 7:
                self.cart[7] = self.cart[7] + Qty
                self.Total = self.Total + (20000 * Qty)

            elif item == 8:
                self.cart[8] = self.cart[8] + Qty
                self.Total = self.Total + (5000 * Qty)

            elif item == 9:
                self.cart[9] = self.cart[9] + Qty
                self.Total = self.Total + (5000 * Qty)

            elif item == 10:
                self.cart[10] = self.cart[10] + Qty
                self.Total = self.Total + (2000 * Qty)

            else:
                print("Enter valid item from 1-10, Thank you!")

            choice = input("You want to add other item into cart? Press 'Y' for continue and press 'N' for exit. \n")
            if choice == "N" or choice =="n":
                break
            print()
        print("Item Name            QTY        PRICE      AMOUNT")
        print("==================================================")
        print(f"Washing Machine       {self.cart[1]}         40000     : {40000 *self.cart[1]}")
        print(f"Telivision            {self.cart[2]}         45000     : {45000 *self.cart[2]}")
        print(f"Laptop                {self.cart[3]}         80000     : {80000 *self.cart[3]}")
        print(f"Refrigerator          {self.cart[4]}         45000     : {45000 *self.cart[4]}")
        print(f"Air Conditinoning     {self.cart[5]}         40000     : {40000 *self.cart[5]}")
        print(f"Fan                   {self.cart[6]}         10000     : {10000 *self.cart[6]}")
        print(f"Microwave             {self.cart[7]}         20000     : {20000 *self.cart[7]}")
        print(f"Electric Grinder      {self.cart[8]}         05000     : {5000 *self.cart[8]}")
        print(f"Toaster               {self.cart[9]}         05000     : {5000 *self.cart[9]}")
        print(f"Iron                  {self.cart[10]}         02000     : {2000 *self.cart[10]}")
        print("=====================================================")
        print(f"Your total bill is :                       {self.Total}")

        print("")
        print("Thanks you visit again!")

Ele = Showroom()
Ele.Electronic_item()



        














# class test:
#     mem1 = 0
#     def __init__(self):
#         print("Inside init")
        
#     def display(self):
#         print("Inside display")
#         self.mem1 = 900

# obj = test()
# obj1 = test()
# obj.display()
# print(obj.mem1)
# print(obj1.mem1)



























            
        



        


