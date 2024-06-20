# Exception vs Error:- Error cannot be handled. Exception can be handled using exception handling syntax.

#  Exception Handle is 4 Blocks : !)try block 2). except block 3). else block 4). finally block

# syntex: 
# try:
#     code containing exceptions (suspicious code)

# except [ExceptionName] : ===> ExceptionName is optional
#                         Code to handle exceptions(if ocurred)

# else:      ===> optional block
#      code to execute if no exceptions occured.

# finally:   ===> optional block
#         Always exceuted  

# else block and finally block are optional
# we can have multiple except block for one try block
# finally block is always executed
# except block :- if exception
# else block :- if no exception
#####################################################################################################

a = int(input("Enter the number: "))
print(f"Multiplication table of {a} is : ")

for i in range(1,11):
    print(f"{a} x {i} = {int(a) * i}")

print("Some lines of code")
print("End of Program")

##############################################################

a = (input("Enter the Number: "))
print(f"Multiphication table of {a} is: ")

try: 
    for i in range (1,11):
        print(f"{a} X {1} = {int(a) * 1}")
except Exception as e:
    print(e)

print("Some lines of code:")
print("End of program")

#############################################################
a = input("Enter the Number: ")
print(f"Multiphiction table of {a} is : ")

try:
    for i in range (1,11):
        print(f"{a} x {i} = {int(a) * i}")
except Exception as a:
    print("Sorry some error occurred")

print("Some lines of code")
print("End of Program")

#############################################################
a = input("Entre the the number: ")
print(f"Multiphication table of {a} is : ")

try:
    for i in range(1,11):
        print(f"{a} X {i} = {int(a) * i}")
except:
    print("Invalid Input!")

print("some lines of code")
print("End of Program")

##############################################################
try:
    num = int(input("Enter the integer: "))
    a =[6,4]
    print(a[num])
except ValueError:
    print("Number entered is not an integer")
except IndexError:
    print("Index Error")

####################################################################################################
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number:"))
div = num1/num2
print(div)
print("rest of code")

####################################################################################################
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number:"))

try:
    div = num1/num2
    print(div)
except  ZeroDivisionError:
    print("divided by zero is not possible")
print("rest of code")

####################################################################################################
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number:"))

try:
    div = num1//num2
    print(di)
except Exception as e:
    print(e)
print("rest of code")

####################################################################################################
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number:"))

try:
    sum = num1 + num2
    print(sub)
except NameError:
    print(" variable name is wrong")
print("rest of code")

####################################################################################################
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number:"))

try:
    div = num1/num2
    print(di)
except  ZeroDivisionError:
    print("divided by zero is not possible")
except NameError:
    print("Name Error")
print("rest of code")

####################################################################################################
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number:"))

try:
    div = num1/num2
    print(di)
except (ZeroDivisionError, NameError) as obj:
    print(obj)
print("rest of code")

####################################################################################################
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number:"))

try:
    div = num1/num2
    print(div)
except:
    print("Somthing went wrong")
else:
    print("an exception didn't occur")
finally:
    print("always Executed")
print("rest of code")
