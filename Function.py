
#===============================================================
#1)Write a function that take user input in integer and return it.
#===============================================================
def takeinput():
    num=int(input("Enter the any number you wish: "))
    return num
def printoutput():
    res=takeinput()
    print(res)
printoutput()

#===============================================================
#2)Write a function that take user input in string and return it.
#===============================================================
def userinput():
    user=input("Enter the any character you wish: ")
    return user
def printoutput():
    char=userinput()
    print(char)
printoutput()

#===============================================================
#3)Write a function that take user input in string and return integer.
#===============================================================
def userinput():
    user=input("Enter the any number: ")
    return user
def returnoutput():
    num=int(userinput())
    print(num)
    print(type(num))
returnoutput()

#====================================================================
#4)Write a function that take user input in integer and return string.
#====================================================================
def userinput():
    user=int(input("Enter the any number you wish: "))
    return user
def stringoutput():
    string=str(userinput())
    print(string)
    print(type(string))
stringoutput()

#====================================================================
#5)Write a function that take user input in integer and return float.
#====================================================================
def userinput():
    user=int(input("Enter the any number you wish: "))
    return user
def floatoutput():
    res=float(userinput())
    print(res)
    print(type(res))
floatoutput()

#====================================================================
#6)Write a function to concat two srings
#====================================================================
char1= input("Enter the first character you wish: ")
char2=input("Enter the second character you wish: ")
def concat():
    res=char1+" "+char2
    print(res)
    print(type(res))
concat()

#====================================================================
# 7)WAP to find the greatest number
#====================================================================
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))

def greatest():
    if num1>num2:
        print("Greatest number is ",num1)
    elif num2>num1:
        print("Greatest number is ",num2)
greatest()

#====================================================================
# 8)WAP to find the smallest number
#====================================================================
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))

def smallest():
    if num1<num2:
        print("Smallest number is ", num1)
    elif num2<num1:
        print("Smallest number is ", num2)
smallest()

#====================================================================
# 9)WAP to find the greatest number
#====================================================================
# size=int(input("Enter the size of list: "))
mylist=[]
for a in range(size):
    num=int(input("Enter the number:"))
    mylist.append(num)
print(mylist)
# Method 1:
def greatest():
    greatest=mylist[0]
    for x in mylist:
        if greatest < x:
            greatest = x
    print(greatest)
greatest()

# Method 2:
greatest=mylist[0]
for x in range(1,len(mylist)):
    if greatest<mylist[x]:
        greatest=mylist[x]
print(greatest)

#====================================================================
# 10)WAP to find the smallest number & greatest number
#====================================================================
size = int(input("Enter the sizeof list:"))
mylist = []
for x in range(size):
    num = int(input("Enter the number:"))
    mylist.append(num)
print(mylist)
# Method 1.
def smallest():
    smallest = mylist[0]
    greatest = mylist[0]
    for y in range(1, len(mylist)):
        if smallest > mylist[y]:
            smallest = mylist[y]
        if greatest < mylist[y]:
            greatest = mylist[y]
print(smallest)
print(greatest)
smallest()

#Method 2.
greatest=mylist[0]
smallest=mylist[0]

for x in mylist:
    if smallest > x:
        smallest=x
    if greatest < x:
        greatest=x
print(smallest)
print(greatest)

#====================================================================
# 11) creat calculator
#====================================================================
def cal():
    a=int(input("Enter the first number:"))
    b=int(input("Enter the second number:"))
    choice=int(input("1 add. 2 sub. 3 mul. 4 div.: "))
    if choice==1:
        print(a+b)
    elif choice==2:
        print(a-b)
    elif choice==3:
        print(a*b)
    elif choice==4:
        print(a//b)
    else:
        print("Invalid Choice")
cal() 

#====================================================================
# 12) creat calculator
#====================================================================
def scical():
    a=int(input("Enter the first number: "))
    b=int(input("Enter the second number: "))
    choice=int(input("1 add. 2 sub. 3 mul. 4 div. 5 power.: "))
    if choice==1:
        print(a,b)
    elif choice==2:
        print(a-b)
    elif choice==3:
        print(a*b)
    elif choice==4:
        print(a//b)
    elif choice==5:
        print(a**b)
    else:
        print("Invalid choice")
scical()

#====================================================================
# 13) creat calculator
#====================================================================
def takeinput():
    c=int(input("Enter the first number: "))
    d=int(input("Enter the second number: "))
    return c,d

def scical():
    choice=int(input("1 add. 2 sub. 3 mul. 4 div. 5.powe.: "))
    a,b=takeinput()
    if choice==1:
        print(a+b)
    elif choice==2:
        print(a-b)
    elif choice==3:
        print(a*b)
    elif choice==4:
        print(a//b)
    elif choice==5:
        print(a**b)
    else:
        print("Invalid Choice")
scical()
    
#====================================================================
# 14) creat calculator
#====================================================================
def takeinput():
    c=int(input("Enter the first number: "))
    d=int(input("Enter the second number: "))
    return c,d

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a//b
def power(a,b):
    return a**b

def scical():
    res=0
    choice=int(input("1 add. 2 sub. 3 mul. 4 div. 5 power.: "))
    x,y=takeinput()
    if choice==1:
        res=add(x,y)
    elif choice==2:
        res=sub(x,y)
    elif choice==3:
        res=mul(x,y)
    elif choice==4:
        res=div(x,y)
    elif choice==5:
        res=power(x,y)
    else:
        print("Invalid choice")
    print(res)
scical()
#====================================================================
# 15) print a,b,c
#====================================================================  

a=100
def add():
    a=300
    b=200
    print(b)
    print(a)
    def sub():
        c=600
        print(c)
add()
print(a)

#====================================================================
# 16) WAP to greet a user with "Good day" using function.
#====================================================================  

name=input("Enter your good name: ")
def greet(name):
    print("Good Day! "+ name)
greet(name)

#====================================================================
# 17) Default Parameter value
#====================================================================  
name=input("Enter your good name: ")
def greet(name="Pooja"):
    print("Good Day! "+name)
greet()
greet(name)

#====================================================================
# 17)WAP to factorial 5 value using function
#====================================================================
n=int(input("Enter the number: "))
def factorial_iter(n):
    product=1
    for i in range(n):
        product=product*(i+1)
    return product
f=factorial_iter(n)
print(f)

#====================================================================
# 18)WAP to recursive function
#====================================================================
# n! = 1 * 2 * 3 * 4 *....................n!
# n! = [ 1 * 2 * 3 * 4 *.................*n-1]*n!
# n!=n*(n-1)!
# factorial(n) = n * factorial(n-1)

n=int(input("Enter the number: "))

def function_recursive(n): # it is used to directly use a mathematical formula as a function 
    if n==0 or n==1 :   # Based condition which doesn't call the function any further
        return 1
    return n*(function_recursive(n-1))  # function calling itself

f=function_recursive(n)
print(f)

#====================================================================
# 19)WAP using the function to convert celcius to farenheit
#====================================================================
cell=int(input("Enter the Celcius: "))
def farh(cel):
    return(cel*(9/5)) + 32

f=farh(cell)
print("Farenheit Temperature is " + str(f))

#====================================================================
# 20) How do ou prevent a python print() function to print a new
#     line at rhe end
#====================================================================
print("Hello", end=" ")
print("How", end=" ")
print("are", end=" ")
print("you?", end=" ")

#====================================================================
# 21) Type of function in python
#====================================================================

# There are two type of functions in python.
# 1) Built in function ===> Alreaady Present in python
# 2) User defined function ===> Defined by User 
'
#====================================================================
# 22) Write a recursive function to calculate the sum of first n
#     natural numbers
#====================================================================
n=int(input("Enter the numer: "))
# sum(n) = sum(n-1) + n

def function_recursive(n):
    if n==1:
        return 1
    return (function_recursive (n-1)) + n

f=function_recursive(n)
print(f)

#====================================================================
# 22) Write a function to print first n line of the following pattern
#  * * *
#  * *
#  *     ===> for n=3
#====================================================================
n=int(input("Enter the number: "))
for i in range(n):
    print("* " * (n-i)) # prints * n-i times

#====================================================================
# 23) Write a python function which converts inches in to cms.  
#====================================================================
inch=int(input("Enter the inch: "))

def convet_cms(inch):
    return (inch * 2.54)

c=convet_cms(inch)
print("Cms is :"+ str(c))

#====================================================================
# 24) Write a python function to remove a given word from a string
#     and strip it at the same time.
#====================================================================
# this="   jeel is good boy         "
# print(this)
# print(this.strip())

def remove_and_strip (string,word):
    newstr=string.replace(word,"")
    return newstr.strip()
this="   jeel is good   "
n=remove_and_strip(this,"jeel")
print(n)

#====================================================================
# 25) Write a python function to remove a given word from a string 
#     and stplit it at the same time.
#====================================================================

def remove_and_split(string,word):
    newstr=string.replace(word,"")
    return newstr.split()
str="    jeel is good boy   "
n=remove_and_split(str,"jeel")
print(n)

#====================================================================
# 26) Write a python function to remove a given word from a string 
#     and stplit it at the same time.
#====================================================================

def remove_and_strip(string,word):
    newstr=string.replace(word,"Mayank")
    return newstr

str="jeel is good boy"
n=remove_and_strip(str,"jeel")
print(n)

