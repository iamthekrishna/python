# oops : oops stand for Object Oriented Programming system 
#   - Abstration
#   - Encapsulation
#   - Inheritance
#   - Polymorphism

# ============== class ===================
# class is a collection of object, and classs is a blueprint or prototype from object is being created.
'''
class class_name:
    statement..1
    .
    .
    statement..2  
'''

# ========== Empty class ========== 
#no definiton or no variableor nothing inside the class

class empty_class:
    pass

# =========== Object =============
# object is a instance of a class 

emptyObj1 = empty_class()           # <---- obj1 is a object of empty_class. 

# ============= class and object example =============
# class can have multiple object.
'''
class Employee:
    companyName = ""
    def printEmpName(a):
        print("adam joshef")
    
    def printEmpAge(a):
        print("34")
    
    def printEmpDesignation(a):
        print("Software Developer")

emp1 = Employee()
print("value of companyName: ", emp1.companyName)
emp1.printEmpName()
emp1.printEmpAge()
emp1.printEmpDesignation()

emp1.companyName = "Tata Consultancy Service"
print(emp1.companyName)

# ===============================================================
# __init__ 
#   : is a speacial method which automatically called when object is created from class.

class InitClassTest:
    def __init__(self):
        print("Inside __init__ method")

inclass = InitClassTest()

class TestClass:
    def __init__(self, data):
        self.member = data
    
tClass = TestClass(123)
print(tClass.member)

class TestClass1:
    def __init__(self, val1, val2, val3, val4, val5):
        self.mem1 = val1
        self.mem2 = val2
        self.mem3 = val3
        self.mem4 = val4
        self.mem5 = val5
    
    def printMember(self):
        print(self.mem1)
        print(self.mem2)
        print(self.mem3)
        print(self.mem4)
        print(self.mem5)

obj1 = TestClass1(1,2,3,4,5)
obj2 = TestClass1(6,7,8,9,10)
obj3 = TestClass1(11,12,13,14,15)
obj4 = TestClass1(16,17,18,19,20)
obj5 = TestClass1(21,22,23,24,25)

obj1.printMember()
obj2.printMember()
obj3.printMember()
obj4.printMember()
obj5.printMember()

# ============================================

class TestAddress:
    def __init__(self):
        print("Inside test Address class")

tAdd1 = TestAddress()
tAdd2 = TestAddress()

print("address of tAdd1: ", id(tAdd1))
print("Address of tAdd2: ", id(tAdd2))        

#====================================================================
# creat calculator
#==================================================================== 

class Calculator:
    def __init__(self, Val1, Val2):
        self.a = Val1
        self.b = Val2

    def add(self):
        print(self.a + self.b)
    def sub(self):
        print(self.a - self.b)
    def mul(self):
        print(self.a * self.b)
    def div(self):
        print(self.a //self.b)

Cal = Calculator(15, 30)
Cal.add()
Cal.sub()
Cal.mul()
Cal.div()

#====================================================================
#  creat Scicalculator
#====================================================================

Val1 = int(input("enter the First Value: "))
Val2 = int(input("Enter the Second Value: "))

class Scical:
    def __init__(self, Val1, Val2):
        self.a = Val1
        self.b = Val2

    def add(self):
        print(self.a + self.b)
    
    def sub(self):
        print(self.a - self.b)

    def mul(self):
        print(self.a * self.b)

    def div(self):
        print(self.a // self.b)

    def module(self):
        print(self.a % self.b)

    def power(self):
        print(self.a ** self.b)

Sci = Scical(Val1, Val2)
Sci.add()
Sci.sub()
Sci.mul()
Sci.div()
Sci.module()
Sci.power()

# =========================================================================
# WAP to define class called Car
# car : Tata Nexon, 1500000, Volvo X6, 6500000 , Hyundai verna 2000000

# Method 1
class Car():
    def __init__(self, CarPrice1, CarPrice2, CarPrice3):
        self.price1 = CarPrice1
        self.Price2 = CarPrice2
        self.Price3 = CarPrice3
    
    def Tata(self):
        print("Tata Nexon price is ", self.price1)

    def Volvo(self):
        print("Volvo X6 price is ", self.Price2)

    def Hyundai(self):
        print("Hyundai Verna price is ", self.Price3)

Car = Car(1500000,6500000,2000000)
Car.Tata()
Car.Volvo()
Car.Hyundai()

# Method 2

class Car():
    def __init__(self):
        pass
        
    
    def Tata(self,a):
        print("Tata Nexon price is ", a)

    def Volvo(self,b):
        print("Volvo X6 price is ", b)

    def Hyundai(self,c):
        print("Hyundai Verna price is ", c)


Car = Car()
Car.Tata(1500000)
Car.Volvo(6500000)
Car.Hyundai(2000000)


#=============================================================================
# WAP to define class called Mobile
# mobile : apple , samsun, Vivo, readme , Oppo
#============================================================================
class MobileStore:
    def __init__(self):
        pass

    def Apple(self, a):
        print("Apple Mobile price is ", a)

    def Samsung(self, b):
        print("Samsung Mobile price is ", b )

    def Vivo(self, c):
        print("Vivo Mobile Price is ", c)

    def Readme(self, d):
        print("Readme Mobile Price is ",d)

    def Oppo(self, e):
        print("Oppo Mobile price is ", e)

a = int(input("Enter the Apple Mobile Price"))
b = int(input("Enter the Samsung Mobile Price"))
c = int(input("Enter the Vivo Mobile Price"))
d = int(input("Enter the Readme Mobile Price"))
e = int(input("Enter the Oppo Mobile Price"))

Mobile = MobileStore()
Mobile.Apple(a)
Mobile.Samsung(b)
Mobile.Vivo(c)
Mobile.Readme(d)
Mobile.Oppo(e)

# Method 2:
class Mobilestore:
    def __init__(self):
        pass

    def Brandname(self):
        choice =int(input("1) Apple, 2) Samsung, 3) Vivo, 4) Redme, 5) Oppo "))
        a = int(input("Enter the Model price"))
        if choice == 1:
            print("Apple Mobile Price is ", a)

        elif choice == 2:
            print("Samsung Mobile Price is ", a)

        elif choice == 3 :
            print("Vivo Mobile price is ", a)

        elif choice == 4:
            print("Readme mobile Price is ", a)

        elif choice == 5:
            print("Oppo Mobile price is ",a )

        else: 
            print("Enter valid Mobile Brand")

Mobile = Mobilestore()
Mobile.Brandname()

'''

# Abstraction: Abstraction means provide essential or necessary details and hiding background details.
#              Hiding internal details and show only funtionality.
# For example, print() function is prniting or showing the data into console but we don't know how it is doing
#               internally, it is hiding the internal details.

'''
class MathClass:
    def __init__(self):
        pass

    def PowerOf(self, number, power):
        temp = power
        res = 1
        while temp > 0:
            res = res* number
            temp = temp - 1
        
        return res

m = MathClass()
res = m.PowerOf(3,0)
print(res)
'''

# Encapsulation: Encapsulation means building the data and member function in single unit. also we can provide 
#                the access of using access specifier.

# Access Specifier: public, privte, protected
# public : Member of a class that declare public are easily accessible from any part of programm.
#          - All data member and member function are by default public.
#          - access from inside the class, outside the class as well
# private: Member function of a class that are decalred private are accessible within the class only.
#          - Inside class only have access
#          - To make the member private we can use '__' (double underscore)prefix.
# protected : Member of class decalared protected are accessible to a class derived from it.
#          - Inherit class can only access
#          - To make the member protected we can use '_' (single underscore)prefix.

'''
class TestClass:
    def __init__(self):
        self.mem1 = 100     # public member 
        self.__mem2 = 200   # private member 
        self._mem3 = 300    # protected member

    def getMem2(self):      # public get method
        return self.__mem2
    
    def setMem2(self, val): # public set method
        self.__mem2 = val
    
    def display(self):  # public method
        print("Mem1:", self.mem1)
        print("Mem2:", self.__mem2)
        print("Mem3:", self._mem3)

    def __printMem(self):   # private method
        print("Mem1:", self.mem1)
        print("Mem2:", self.__mem2)
        print("Mem3:", self._mem3)

    def _printMem(self):   # protected method
        print("Mem1:", self.mem1)
        print("Mem2:", self.__mem2)
        print("Mem3:", self._mem3)

tc = TestClass()
#tc.__printMem()
tc.display()

tc.__testPrivate = 123456
tc.mem1 = 123
tc.__mem2 = 999
tc._mem3 = 333
print("After change the data member value")
tc.display()

tc.mem1 = 145
tc.setMem2(999)
# tc.__printMem()
tc.display()
'''

# Inheritance: It is the powerful concept of oops. Once class can inherit the property and behaviour of another
#               class called inheritance.
# single Inheritance:
# multilevel Inheritance:
# Hierarchical Inheritance:
# Multiple Inheritance:

'''
class Parent:
    Name = "Parent Class"

class Child(Parent):
    CName = "Child Class"

cObj = Child()
print(cObj.CName)
print(cObj.Name)

# super() function is used to give access to methods and properties of a parent class
class Parent:
    def __init__(self):
        self.Name = "Parent class"

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.CName = "Child Class"

cObj = Child()
print(cObj.CName)
print(cObj.Name)
'''

# Single inheritance and override method
'''
class Parent:
    Name = "Parent Class"
    def __init__(self):
        print("Inside Parent Class")
    
    def Method(self):
        print("Inside Parent Method")

class Child(Parent):
    CName = "Child Class"
    def __init__(self):
        super().__init__()
        print("Inside Child class")
    
    def Method(self):
        print("Inside child Method")
    
cObj = Child()
cObj.Method()
'''
'''
#multiple Inheritance
class Base:
    def __init__(self, val):
        print("inside base")
    def BaseMethod(self):
        print("base method")

class Base1:
    def __init__(self):
        print("inside base one")
    def Base1Method(self):
        print("base method one")

class Derived(Base, Base1):
    def __init__(self):
        super().__init__(self)
        print("inside derived")

dObj = Derived()
dObj.BaseMethod()
dObj.Base1Method()
'''
#Diamond 
'''
class Base:
    def __init__(self, val):
        print("inside base")
    def Method(self):
        print("base method")

class Base1:
    def __init__(self):
        print("inside base one")
    def Method(self):
        print("base method one")

class Derived(Base, Base1):
    def __init__(self):
        super().__init__(self)
        print("inside derived")

dObj = Derived()
dObj.Method()
'''

# Multilevel Inheritance
'''
class Base:
    def __init__(self):
        print("Base")
    def Method(self):
        print("Base metohd")

class Derived(Base):
    def __init__(self):
        super().__init__()
        print("Derived")
    def Method(self):
        print("Derived metohd")

class Derived1(Derived):
    def __init__(self):
        super().__init__()
        print("Derived1")
    # def Method(self):
    #     print("Derived1 metohd")

obj = Derived1()
obj.Method()
'''


# Python Program to depict multiple inheritance
# when every class defines the same method
 
# class Class1:
#     def m(self):
#         print("In Class1") 
 
# obj = Class1()
# Class1.m(obj)

# Python Program to depict multiple inheritance
# when every class defines the same method
''' 
class Class1:
    def m(self):
        print("In Class1") 
       
class Class2(Class1):
    def m(self):
        print("In Class2")
 
class Class3(Class1):
    def m(self):
         print("In Class3")     
     
class Class4(Class2, Class3):
    def m(self):
        print("In Class4")   
 
obj = Class4()
obj.m()
 
Class2.m(obj)
Class3.m(obj)
Class1.m(obj)
'''
# Python Program to depict multiple inheritance 
# when we try to call the method m for Class1, 
# Class2, Class3 from the method m of Class4 
'''
class Class1:
    def m(self):
        print("In Class1")  
      
class Class2(Class1):
    def m(self):
        print("In Class2")
 
class Class3(Class1):
    def m(self):
        print("In Class3")     
     
class Class4(Class2, Class3):
    def m(self):
        print("In Class4")   
        Class2.m(self)
        Class3.m(self)
        Class1.m(self)
 
obj = Class4()
obj.m()
'''

# Method resolution order: (MRO)
# In Python, every class whether built-in or user-defined is derived from the object class 
# and all the objects are instances of the class object.
# Hence, the object class is the base class for all the other classes.
# In the case of multiple inheritance, a given attribute is first searched in the current class
# if it’s not found then it’s searched in the parent classes. The parent classes are searched in a left-right 
# fashion and each class is searched once.
# If we see the below example then the order of search for the attributes will be Derived, Base1, Base2, object. The order that is followed is known as a linearization of the class Derived and this order is found out using a set of rules called Method Resolution Order (MRO).
# To view the MRO of a class: 
 
# Use the mro() method, it returns a list 
# Eg. Class4.mro()
# Use the _mro_ attribute, it returns a tuple 
# Eg. Class4.__mro__
''' 
class Class1:
    def m(self):
        print("In Class1")
 
class Class2(Class1):
    def m(self):
        print("In Class2")
        super().m()
 
class Class3(Class1):
    def m(self):
        print("In Class3")
        super().m()
 
class Class4(Class2, Class3):
    def m(self):
        print("In Class4")   
        super().m()
      
print(Class4.mro())         #This will print list
print(Class4.__mro__)        #This will print tuple
'''

# Polymorphism: polymorphism means one name many form, it refers to the use of the same function name,
#               but with different signatures.
# 2) polymorphism means the same function name (but different signatures) being used for different types.
# Example: len("greeks"), len([1,2,3,4])

class vehicle:
    def __init__(self, b, m):
        self.brand = b
        self.modal = m
    
    def move(self):
        print("Move")

class car(vehicle):
    pass

class boat(vehicle):
    def move(self):
        print("sail!")

class plane(vehicle):
    def move(self):
        print("fly")

c = car("Tata", "Nexon")
b = boat("India", "In 1")
p = plane("Air india", "boeing")

for x in (c, b, p):
    print(x.brand)
    print(x.modal)
    x.move()

