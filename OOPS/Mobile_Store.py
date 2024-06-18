# =================================Mobile Store ===============================#
print("============================Menu=============================")
print("1).Apple ==================================Rs.1,00,000")
print("2).Samsung ================================Rs.75,000 ")
print("3).Vivo ===================================Rs.30,000 ")
print("4).Oppo ===================================RS.40,000 ")
print("5).Redmi ==================================Rs.20,000 ")

class MobileStore:
    def __init__(self):
        self.Total = 0
        self.cart = {1:0, 2:0, 3:0, 4:0, 5:0}

    def MobileBrand(self):
        while True:
            item = int(input("1).Apple, 2).Samsung, 3).Vivo, 4).Oppo, 5).Redmi: \n"))
            Qty = int(input("Enter the quantity: \n"))

            if item == 1:
                self.cart[1] = self.cart[1] + Qty
                self.Total = self.Total + (100000 * Qty)

            elif item == 2:
                self.cart[2] = self.cart[2] + Qty
                self.Total = self.Total + (75000 * Qty)

            elif item == 3:
                self.cart[3] = self.cart[3] + Qty
                self.Total = self.Total + (30000 * Qty)

            elif item == 4:
                self.cart[4] = self.cart[4] + Qty
                self.Total = self.Total + (40000 * Qty)
            
            elif item == 5:
                self.cart[5] = self.cart[5] + Qty
                self.Total = self.Total + (20000 * Qty)

            else:
                print("Enter the 1-5")
        
            choice = input("continue = Y, Exit = N  \n")
            if choice == "N" or choice == "n":
                break

        print("Summary===================Item X QTY    = Total")
        print(f"Apple ===================100000 x {self.cart[1]}= {100000 * self.cart[1]} ")
        print(f"Apple ===================75000 x {self.cart[2]} = {75000 * self.cart[2]} ")
        print(f"Apple ===================30000 x {self.cart[3]} = {30000 * self.cart[3]} ")
        print(f"Apple ===================40000 x {self.cart[4]} = {40000 * self.cart[4]} ")
        print(f"Apple ===================20000 x {self.cart[5]} = {20000 * self.cart[5]} ")
        print("Total                                   =", self.Total)

Mob = MobileStore()
Mob.MobileBrand()
