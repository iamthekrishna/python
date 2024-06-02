 # ========================================================
# 1) WAP to check whether a person is eligible for
#    voating or not. (accept age is 18)
# ========================================================
age=int(input("Enter the age:  "))
if age>=18:
    print(age, "is eligible for vote")
else:
    print(age,"is not eligible for vote")

# ========================================================
# 2) WAP to check whether a number enterd by user is
#    even or odd.
# ========================================================   
n= int(input("Enter the the number: "))
if n % 2 ==0:
    print(n, "is even number")
else:
    print(n, "is odd number")

# ========================================================
# 3) WAP to check whether a number is divisible by 7 or not.
# ======================================================== 
n=int(input("Enter your number: "))
if n % 7==0:
    print(n, " is divisible ")
else:
    print(n, "is not divisible")

# ========================================================
# 4) wap to check whether a number is divisible by 5 or not.
# ========================================================
if n % 5 ==0:
    print(n,"is divisible")
else:
    print(n, "is not divisible")

# ========================================================
# 4) WAP to display "Hello" if number enter by useris 
#    multiple of five, otherwise print "Bye"
# ========================================================
n=int(input('Enterthe number: '))

if n % 5 ==0:
    print("Hello")
else:
    print("Bye")

# ========================================================
# 5) WAP to calculate the electricity bill(accept number of 
#    unit for user)acoording to the following criteria.

#  UNIT                 PRICE
# First 100 unit   ==>  No charge
# NEXT 100 UNIT    ==> Rs 5 per Unit
# After 200 Unit   ==> Rs. 10 per Unit
# ========================================================
n=int(input("Enter the Unit:  "))
if n <= 100:
  charge=0
elif n >= 100 and n <=200:
  charge=(n-100)*5
else:
  charge=(100*5)+(200-n)
  print("Amount to pay :",  charge)

# ========================================================
# 6) WAP to check whether the last digit of number is 
#    divisible by 3 or not.
# 1%10 : 1
# 11%10: 1
# 111%10: 1
# 123%10:3
# ========================================================
n=int(input("Enter the number"))
n=n%10
if n % 3 ==0:
    print("Last digit of number is divisible by 3")
else:
    print("Last digit of number is not divisibile by 3")

# ========================================================
# 7) WAP to display the last digit of a number.
# ========================================================
n=int(input("Enter the number: "))
if n>=0:
    x=n % 10
    print(x)
else:
    print("your number is negative please enter positive number")

# ========================================================
# 8) WAP to accept percentage from the user and display 
#    the grade according to the following critea:
#          Marks                         Grade
#     >90                   =====>>  A 
#     >80 and <=90          =====>>  B
#     >= 60 and<=80         =====>>  C 
#     below 60              =====>>  D
# ========================================================
Persentage = int(input("User Enter Marks: "))
if Persentage > 90 :
    print("Grade is A")
elif Persentage > 80 and Persentage <= 90:
    print("Grade is B")
elif Persentage >= 60 and Persentage <= 80:
    print("Grade is C")
else:
    print("Grade is D")

# ========================================================
# 9) WAP to accept the cost price of a bike and display the 
#   road tax to be paid acoording to following criteria:
#   Cost Price (In Rs.)          Tax
#   > 100000                 ======>> 15%
#   >50000 and <= 100000     ======>> 10%
#   <= 50000                 ======>> 5%
# ========================================================
Tax=int(input("User Enter the cost Price:  "))
Method : 1

if Tax > 100000:
    result= Tax *15 /100
    print("Road tax to be paid",result)
if Tax > 50000 and TaX <= 100000:
    result= Tax*10/100
    print("Road tax to be paid",result)
if Tax <= 50000:
    result= Tax*5/100
    print("Road tax to be paid",result)

Method : 2
if Tax > 100000:
    result=Tax*15/100
    print("Road tax to be paid",result)
elif Tax > 50000 and Tax <= 100000:
    result=Tax*10/100
    print("Road tax to be paid",result)
else:
    result=Tax*5/100
    print("Road tax to be paid",result)

# ========================================================
# 10) WAP to check whether an years is leap year or not.
# ========================================================
Year=int(input("Enter the Year"))
if Year % 4 ==0:  # likely a leap year:- number is evenly divisible by 4
    print("Entered Year is Leap year ")
else:
    print("Entered year is not leap year")

# ========================================================
# 11) WAP to accept number from 1 to 7 and display the name
#     the day  like 1 for Sunady,2 for Monday and so on.
# ========================================================   
num=int(input("Enter the number between 1 to 7: "))

if num==1:
    print("Sunday")
elif num==2:
    print("Monday")
elif num==3:
    print("Tuesday")
elif num==4:
    print("Wednesday")
elif num==5:
    print("Thursday")
elif num==6:
    print("Friday")
elif num==7:
    print("Saturday")
else:
    print("Enter the number between 1 to 7"
          
# ========================================================
# 12) WAP to accept number from 1 to 7 and display the name 
#     the month and day in the month like 1 for january and
#     number of days 31 and so on.
# ========================================================
num=int(input("Enter the number from 1 to 12:   "))

if num==1:
    print("January and number of the days 31")
elif num==2:
    print("February and number of days 28 or 29")
elif num==3:
    print("March and number of days 31")
elif num==4:
    print("April and number of days 30")
elif num==5:
    print("May and number of days 31")
elif num==6:
    print("June and number of days 30")
elif num==7:
    print("July and number of days 31")
elif num==8:
    print("August and number of days 31")
elif num==9:
    print("September and number of days 30")
elif num==10:
    print("October and number of days 31")
elif num==11:
    print("November and number of days 30")
elif num==12:
    print("December and number of days 31")
else:
    print("Enter the number from 1 to 12")

# ========================================================
# 13) write a logical expression for the following:
#     A is greater than B and C is greater than D  
# ========================================================
A > B and C > D

# ========================================================
# 14) Accept any city from the user and display monument of
#      the city.
#        city               Monument
#       Delhi               Read Fort
#       Agara               Taj Mahal
#       Jaipur              Jal Mahal
# ========================================================
City=input("Enter the city name: ")
if City=="Delhi":
    print("Monument name is : Read Fort")
elif City=="Agara":
    print("Monument name is : Taj Mahal")
elif City=="Jaipur":
    print("Monument name is : Jal Mahal")
else:
    print("Enter the correct city name")

# ========================================================
# 15) WAP to check wheather a person is senior citizen 
#     or not.
# ========================================================
Year=int(input("Enter the age "))

if Year>= 60:
    print(" Senior citizen")
else:
    print("Not senior citizen")

# ========================================================
# 16) WAP to check to find the lowest number out of two
#      numbers excepted from user.
# ========================================================
n1=int(input("Enter the first number: "))
n2=int(input("Enter the second number: "))

if n1>n2:
    print("smaller number is:", n2)
else:
    print("smaller number is :", n1)

# ========================================================
# 17) WAP to check to find the largest number out of two 
#     numbers excepted from user.
# ========================================================
n1=int(input("Enter the first number: "))
n2=int(input("Enter the second number: "))

if n1>n2:
    print("Largest number is:", n1)
else:
    print("Largest number is:", n2)

# ========================================================
# 18) WAP to check whether a number (accepted from user) 
#     is positive or negative.
# ========================================================
num=int(input("Enter the number: "))

if num >= 0:
    print("Positive Number")
else:
    print("Negative Number")

# ========================================================
# 19) WAP to check whether a number (accepted from user)
#      is even and odd.
# ========================================================
num=int(input("Enter the number: "))

if num % 2==0:
    print("Even Number")
else:
    print("Odd number")

# ========================================================
# 20) WAP to whether a number (accepted from user) is 
#     divisible by 2 and 3 both.
# ========================================================
num=int(input("Enter the number: "))

if num % 2==0 and num % 3==0:
    print("Number is divisible 2 and 3 both")
else:
    print("Number is not divisible 2 and 3 both")


# ========================================================
# 21) WAP to find the largest number out of three numbers
#      excepted from user.
# ========================================================
n1=int(input("Enter the first number: "))
n2=int(input("Enter the second number: "))
n3=int(input("Enter the third number: "))

if n1 > n2 and n1 > n3:
    print("largest number is", n1)
if n2 > n1 and n2 > n3:
    print("largest number is ", n2)
if n3 > n1 and n3 > n1:
    print("largest number is ",n3)

# ========================================================
22) Accept the temperature in degree celsius of water and
    check whether it is boiling or not
    (boiling point of water in 100 C).
# ========================================================
temp=int(input("Enter the tempearature: "))

if temp >= 100:
    print("Water is boiling")
else:
    print("Water is not boiling")

# ========================================================
# 23) Accept the age of 4 people and display the youngest one.
# ========================================================
n1=int(input("Enter the 1st people age: "))
n2=int(input("Enter the 2nd people age: "))
n3=int(input("Enter the 3rd people age: "))
n4=int(input("Enter the 4th People age: "))

if n1 < n2 and n1 < n3 and n1 < n4:
    print("Age of Youngest People is", n1)
if n2 < n3 and n2 < n4 and n2 < n1:
    print("Age of Youngest People is", n2)
if n3 < n4 and n3 < n1 and n3 < n2:
    print("Age of Youngest People is", n3)
if n4 < n1 and n4 < n2 and n4 < n3 :
    print("Age of Youngest People is", n4)

# ========================================================
# 24)Accept the age of 4 people and display the oldest one.
# ========================================================
n1=int(input("Enter the 1st people age: "))
n2=int(input("Enter the 2nd people age: "))
n3=int(input("Enter the 3rd people age: "))
n4=int(input("Enter the 4th People age: "))

if n1 > n2 and n1 > n3 and n1 > n4:
    print("Age of oldest People is", n1)
if n2 > n3 and n2 > n4 and n2 > n1:
    print("Age of oldest People is", n2)
if n3 > n4 and n3 > n1 and n3 > n2:
    print("Age of oldest People is", n3)
if n4 > n1 and n4 > n2 and n4 > n3 :
    print("Age of oldest People is", n4)