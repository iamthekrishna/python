# Python Raise Keyword
# User - defined Exceptions:-
# Exception created by programmer
# withdrwaing money

# Raise keyword/statement :-
# An exception can be raised forcefully by using the raise clause in python
# raise statement is used when we want to throw exception for partivular condition.
# ex. input age :-10
#     valueError : Invalid age
# syntax : raise Exception ("Exception message")

############################################################################################
try:
    age = int(input("Enter Your age: "))
    if age<0:
        raise ValueError
    print("Your age is",age)
except ValueError:
    print("Enter the valid age")

print("Rest of code")

############################################################################################
try:
    age = int(input("Enter Your age: "))
    if age < 0:
        raise ValueError("iInvalid Age")
    print("Your age is ", age)
except ValueError as var:
    print(var)

print("Rase of code")

############################################################################################



