
Val1 = int(input("Enter the First Number :  "))
Val2 = int(input("Enter the Second Number: "))
Val3 = int(input("Enter the Third Number: "))

class Calculator:

    def __init__(self, Val1, Val2, Val3):
        self.a = Val1
        self.b = Val2
        self.c = Val3
        
    def add(self):
        print(self.a + self.b + self.c)

    def sub(self):
        print(self.a -self.b - self.c)

    def mul(self):
        print(self.a * self.b * self.c)

    def div(self):
        print(self.a // self.b // self.c)

    def moduls(self):
        print(self.a % self.b % self.c)

    def power(self):
        print(self.a ** self.b ** self.c)

Cal = Calculator(Val1, Val2, Val3)
Cal.add()
Cal.sub()
Cal.mul()
Cal.div()
Cal.moduls()
Cal.power()

    