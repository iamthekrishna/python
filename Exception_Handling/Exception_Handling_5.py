# User defined exception
# Step -1 : Create exception calss and inherit it from Base Exception class.i.e Exception.

# class InvalidAge(Exception):
#     pass

# Step-2:Raise InvalidAge exception for particulat condition(age<0) inside try block.Block.Block.
    
# try:
#    If age<0:
#    raise InvalidAge("message")

# Step -3 : handle the exception using except block.

# except Exception as obj:
#        print(obj)

################################################################################################
# write a python program for FiveDivisionError Exception
'''
class FiveDivisionError(Exception):
    "this is exception class when five division Error happens"
    pass

try:
    n1 = int(input("Enter First number: "))
    n2 = int(input("Enter Second Number: "))

    if n2==5:
        raise FiveDivisionError("can not divided five")
    div = n1/n2
    print("Division is:",div)

except(FiveDivisionError,ZeroDivisionError) as var:
    print(var)

print("Rest of code")

################################################################################################

class FiveDivisionError (Exception):                            # Step - 1
    "this is exception class when five division Error happens"
    def __init__(self):
        print("can not divided by five")

try:
    n1 = int(input("Enter first Number: "))
    n2 = int(input("Enter Second Number: "))

    if n2 == 5:
        raise FiveDivisionError                                  # Step -2
    div = n1/n2
    print("Division is: ", div)

except (FiveDivisionError,ZeroDivisionError) as var:              # Step -3
    print(var, end = "")

print("Rest of code")
'''
################################################################################################