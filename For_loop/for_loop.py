# ========================================================
# 1) WAP to grat all person names stored in a list l1 and 
# which starts with S.
# l1=["Pooja","Jeel","Megha","Shraddha","Shobha"]
# ========================================================
# for name in l1:
#     if name.startswith("S"):
#         print("Hello  " + name)

# ========================================================
# 2) WAP to grat all person names stored in a list l1 and
# which end with a.
# l1=["Pooja","Jeel","Megha","Shraddha","Shobha"]
# ========================================================
# l1=["Pooja","Jeel","Megha","Shraddha","Shobha"]
# for name in l1:
#     if name.endswith("a"):
#         print("Hello "+ name)

# ========================================================
# 3) WAP to grat all person names stored in a set S1 and 
# which start with M and end with a.
# S1=("Mayank","Pooja","Megha","Shraddha","Jeel")
# ========================================================
# S1=("Mayank","Pooja","Megha","Shraddha","Jeel")
# for name in S1:
#     if name.startswith("M"):
#         print("Hii "+ name)
# for name in S1:
#     if name.endswith("a"):
#         print("Hello "+ name)

# ========================================================
# 4) WAP to grat all person names stored in a truple t1 and 
# which start with M and end with a.
# t1={"Mubai","Puna","Rajkot","Surat","Ahmedabad"}
# ========================================================
# t1={"Mubai","Puna","Rajkot","Surat","Ahmedabad"}
# for name in t1:
#     if name.startswith("M"):
#         print("Hello "+name)
# for name in t1:
#     if name.endswith("a"):
#         print("Hii "+ name)

# ========================================================
# 5) WAP check entered number is prime or not Prime number
#    is number only divide by 1 and itself only
#    for ex 2,3,5,7,11,13,17, etc,...
# ========================================================  
# num=int(input("Enter the number: "))
# if num ==1 or num == 2:
#     print ("Enter num is prime num ")
# y=False
# for x in range(2,num):
#     if num % x==0:
#         print("Entered number is not prime")
#         y=True
#         break
# if y==False:
#     print("Eented number is prime")

# ========================================================
# 6)WAP to check a character is vowel or not.
# ========================================================
# Num=input("Enter the Vowel Character: ")
# con = True
# list=["a","e","i","o","u"]
# for x in list:
#     if x==Num:
#         print("Character is vowel ")
#         con = False
#         break
# if con==True:
#     print("Character is consonantas")

# ========================================================
# 7)WAP to check a number is in below list or not.
# list=[3,5,7,10,11]
# ========================================================
# list=[3,5,7,10,11]
# num=int(input("Enter the number: "))
# y=False
# for x in list:
#     if x==num:
#         print("Entered number is in list")
#         y=True
#         break
# if y==False
#     print("Entered number is not in list")

# ========================================================
# 8)WAP to check a number is in below set or not.
# S1=("Mubai","Rajkot","Gandhinagar","Surat","Ahmedabad")
# ========================================================
# S1=("Mubai","Rajkot","Gandhinagar","Surat","Ahmedabad")
# name=input("Enter the name: ")
# y=True
# for x in S1:
#     if x==name:
#         print("Entered name is in set")
#         y=False
#         break
# if y==True:
#     print("Entered name is not in set")

# ========================================================
#9)Nested for loops in Python (one loop inside another loop)
#    list1 = [5,10,15,20]
#    list2 = ['Tomatoes','Potatoes','Carrots','Cucumbers']
# ========================================================
# list1 = [5,10,15,20]
# list2 = ['Tomatoes','Potatoes','Carrots','Cucumbers']
    
# for x in list1:
#     for y in list2:
#         print(x,y)

# ========================================================
# 10) Python for loop to count the number of elements in a list
# list=[10,20,30,40]
# ========================================================
# list=[10,20,30,40]
# count=0
# for n in list:
#     count += 1
# print(count)

# ========================================================
# 11)Python for loop to find the sum of all numbers in a list
# list=[10,20,30,40]
# ========================================================
# list=[10,20,30,40]
# sum=0
# for n in list:
#     sum += n
# print(sum)

# l1=[155,45,56,78]
# sum=0
# for n in l1:
#     sum+=n
# print(sum)

# ========================================================
# 12)Python for loop to find the multiples of 5 in a list
# ========================================================
# l1=[10,20,30,40]
# for n in l1:
#     if n%5==0:
#         print(n)

# l1=[5,3,4,7,9,8]
# for n in l1:
#     if n%3==0:
#         print(n)

# ========================================================
# 13) WAP to print multiplication table of a given using 
#     for loop.  
# ========================================================
# num=int(input("Enter the number:  "))
# for i in range (1,11):
#     print(str(num)+"x" + str(i)+"="+str(i*num))

# for i in range(1,11):
#     print(str(i)+"x"+str(num)+"="+str(i*num))

# for i in range(1,11):
#     print(f"{num}X{i}={i*num}")

# ========================================================
# 14) WAP to calculte the factorial of given number 
#     using for loop.
# ========================================================
#  n!=1 X 2 X 3 X 4 X......X n
# 51=1 x 2 x 3 x 3 x 4 x 5
# num=int(input("Enter the number: "))
# factorial=1
# for i in range (1,num+1):
#     factorial=factorial*i
# print(f"the factorial of {num} is {factorial}")
# print("The factoriyal of " +str(num)+"  is "+str(factorial))

# ========================================================
#15) WAP to printthe following star patten.
# *
# * *
# * * *
# ========================================================
# n=4
# for x in range(n):
#     print("*" * (x+1))

# ========================================================
# 16) WAP to printthe following star patten.
#        *
#      * * *
#    * * * * *
# ========================================================
# n=3
# for i in range(n):
#     print("  "*(n-i-1),end="")
#     print("x "*(2*i+1),end="")
#     print(" "* (n-i-1))

# ========================================================
# 17) WAP to printthe following star patten.
# B
# B B
# B B B
# B B B B
# ========================================================
# n=int(input("Enter the number: "))
# char=input("Enter the letter:")
# for i in range(n):
#     print((char+" ") *(i+1))

# for i in range(n):
#     print("B " *(i+1))

# ========================================================
# 18) WAP to printthe following star patten.
# B B B B
# B B B
# B B
# B
# ========================================================
# n=int(input("Eenter the naumber: "))
# for i in range(n):
#     print((n-i)*"B ")

# ========================================================
# 19) WAP to printthe following star patten.
#       B
#      BB
#     BBB
#    BBBB
# ========================================================
# n=int(input("Enter the number: "))
# for i in range(n):
#     print((" ")*(n-1-i)+(i+1)*"B")

# ========================================================
# 20) WAP to printthe following star patten.
#       B
#      B B
#     B B B
#    B B B B
# ========================================================
# n=int(input("Enter the number: "))
# for i in range (n):
#     print(" "*(n-1-i)+(i+1)*(" B"))

# ========================================================
# 21) WAP to printthe following star patten.
#  B B B B
#  B B B
#  B B
#  B
# ========================================================
# n=int(input("Enter the number: "))
# for i in range(n):
#     print("B "*(n-i))

# ========================================================
# 22) WAP to printthe following star patten.
# 1 1 1 1
# 0 1 1 1
# 0 0 1 1
# 0 0 0 1
# ========================================================
# n=int(input("Enter the number: "))  
# for i in range(n):
#     print(("0 ")*i+("1 ")*(n-i))

# ========================================================
# 23) WAP to printthe following star patten.
# 1 B
# 2 B B
# 3 B B B
# 4 B B B B
# ========================================================
# n=int(input("Enter the number: "))
# for i in range(n):
#     print(str(i+1)+(i+1)*" B")

# ========================================================
# 24) WAP to printthe following star patten.
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# ========================================================
# n=int(input("Enter the name: "))
# count=0
# for i in range(n):
#     for j in range(i+1):
#         count=count+1
#         print(count," ", end="")
#     print(" ")

# ========================================================
# 25) WAP to printthe following star patten.
# 1
# 22
# 333
# 4444
# ========================================================
# n=int(input("Enter the number: "))
# for i in range(n):
#     print(str(i+1 )*(i+1))

# ========================================================
# 26)Python for loop to find the sum of all numbers in a set.
# set=(10,20,30,40)
# ========================================================
# set=(10,20,30,40)
# sum=0
# for x in set:
#     sum+=x
# print(sum)

# ========================================================
# 27)Python for loop to find the multiple of all numbers
#  in a set. set=(10,20,30,40)
# ========================================================
# set=(10,20,30,40)
# mul=1
# for x in set:
#     mul*=x
# print(mul)

# ========================================================
# 28)Python for loop to find the divided of all numbers
#  in a set. set=(10,20,30,40)
# ========================================================
# set=(40,30,20,10)
# div=1000
# for x in set:
#     div//=x
# print(div)

# ========================================================
# 29)WAP to find the greatest number
# ========================================================
# size=int(input("Enter the any size of number:"))
# mylist=[]
# for x in range (size):
#     num=int(input("Enter the any number you wish: "))
#     mylist.append(num)
# print(mylist)
# greatest=mylist[0]
# for y in mylist:
#     if greatest < y:
#         greatest = y 
# print(greatest)

# ========================================================
# 30)WAP to find the greatest number
# ========================================================
# size=int(input("Enter the any number of size:"))
# mylist=[]
# for x in range (size):
#     num=int(input("Enter the any number you wish: "))
#     mylist.append(num)
# print(mylist)

# smallest=mylist[0]
# for y in mylist:
#     if smallest > y:
#        smallest = y
# print(smallest)
    
# ==============================================================
# list = ['A', 'B', 'B', 'D', 'E', 'F']
# count=0
# ASCII_Val = 65
# pos=[]

# for x in list:
#     count=count + 1
#     if ord(x) != ASCII_Val:
#         pos.append(count)
#     ASCII_Val = ASCII_Val + 1
    
# print(pos)

# ======================================================
# list = [0, 1, 2, 2, 4, 5, 6, 6, 8, 9, 10]
# count=0
# pos = []

# for x in list:
#     if x != count:
#         pos.append(count+1)
#     count = count + 1
# print(pos)

# ============================================================================
# list = [1, 28, 4, 56, 67, 0, 78, 89, 95, 0, 12]
# count = 0
# position = []

# for x in list:
#     count=count+1
#     if x == 0:
#         position.append(count)
        
# print(position)

# ==========================================================================
# count=0
# list =["banana","pineapple","Orange","apple","Mango"]
# for x in list:
#     count=count+1    
#     if x == "apple":
#         break
# print(count)

# ==========================================================================

# prime

# num=int(input("enter the number"))
# prime=True
# if num==0 and num==1:
#     print(num,"is in prime number")
# for i in range (2,num):
#     if num% i==0:
#         prime=False
#         break
# if prime:
#     print("This number is prime ")
# else:
#     print("this number is not prime")

# ==========================================================================
# list=[12,-7,20,-59,67,13,-2,10,5,-14, 23, -5, -1, -9, 113, 234, -456, -78, 234, -45, 676, -90]

# positive=[]
# negative=[]

# for x in list:
#     if x>0:
#         positive.append(x)

#     else:
#         negative.append(x)

# print(positive)
# print(negative)

# ==========================================================================
# WAP to printthe following star patten.
# WW BB WW BB
# BB WW BB WW
# WW BB WW BB
# BB WW BB WW

# n1=int(input("Enter the raw size: "))
# n2=int(input("Enter the colum size: "))

# for r in range(n1):
#      for c in range(n2):
#           if c % 2==0:
#             if r % 2==0:
#                 print("BB  ",end="")
#             else:
#                 print("WW  ",end="")
#           else:
#             if r % 2==0:
#                 print("WW  ",end="")
#             else:
#                 print("BB  ",end="")
#      print("\n")

# ==========================================================================
# WAP to printthe following star patten.
# B W B W
# W B W B
# B W B W

# for r in range(3):
#     for c in range(4):
#         if c %2==0:
#             if r %2==0:
#                 print("B  ",end="")
#             else:
#                 print("W  ",end="")
#         else:
#             if r %2==0:
#                 print("w  ",end="")
#             else:
#                 print("B  ",end="")
#     print("")
            
# ==========================================================================
# WAP to printthe following star patten.
# B W B W

# for c in range(4):
#     if c % 2==0:
#         print("B  ",end="")
#     else:
#         print("w  ",end="")
# print("")

# ==========================================================================
# list=[-1,-17,18,0,50,15,48,92,-360]
# greatest_num1=list[0]
# for x in list:
#     if greatest_num1 < x:
#         greatest_num1 = x
# print(greatest_num1)

# greatest_num1=list[0]
# for x in range(1,len(list)):
#     if greatest_num1 < list[x]:
#         greatest_num1 = list[x]
# print(greatest_num1)

# smallest_num1= list[0]
# for x in list:
#     if smallest_num1 > x:
#         smallest_num1 = x
# print(smallest_num1)

# smallest_num1 =list[0]
# for x in range(1,len(list)):
#     if smallest_num1 > list[x]:
#         smallest_num1 = list[x]
# print(smallest_num1)

# ==========================================================================
# age=int(input("Enter your age"))

# if age  >= 18:
#     print("person is eligible to vote", end="")
# else:
#     print(" person is not eligible to vote", end="")
# print("")

# ==========================================================================
# a="Pooja"
# b="Pooja"

# if a == b:
#     print("both strings are same ")
# else:
#     print("both string are not same")

# ==========================================================================
# a=14
# b=14
# if a==b:
#     print("both integes are same" )
# else:
#     print("both integer are not same")

# ==========================================================================
# AB=3
# BC=7
# AC=9
# karn = AC*AC
# fisr_side = BC*BC
# second_Side= AB*AB
# sum = fisr_side + second_Side
# if karn == sum:
#     print("triange is right angle")
# else:
#     print("triange is not right angle")

# ==========================================================================