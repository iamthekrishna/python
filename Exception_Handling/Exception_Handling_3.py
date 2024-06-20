# print Exception name : 1).using exception calss object 2). using sys module


##########################################################################################
#Example 1:
num1 = int(input("Enter first Number: "))
num2 = int(input("Enter Second number: "))

try:
    div = num1/num2
    print("Division is",div)
except Exception as obj:
    print(obj)
    print(obj.__class__)

print("Rest of code")

##########################################################################################
#Example 2:

import sys
num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

try:
    div = num1/num2
    print("Division is ", div)
except:
    print(sys.exc_info()[0])        # <class 'NameError> 0 is expection name
    print(sys.exc_info()[1])        # 1 is  xpection information

print("Rest of Code")