# Use of exception Handling
# Requirement:-
# Withdraw money from bank.
# Balance in bank should not be less than 1000.
# User account will be blocked for an hour if user put 3 times wron pin.

#####################################################################################
'''
class BalanceExceptionError(Exception):
    pass

def withdraw():
    save_pin = 1234
    balance =10000

    pin = int(input("Enter the pin:"))
    if save_pin == pin:
        try:
            amt = float(input("Enter amount to withdraw: "))
            temp_bal = balance -amt
            if temp_bal < 1000:
                raise BalanceExceptionError ("Insufficient balance")
            balance = balance - amt
            print("Remained balance is :",balance)
        except Exception as var:
            print(var)

withdraw()
'''
#####################################################################################
import time
class BalanceExceptionError(Exception):
    pass

class AttemptExceptionError(Exception):
    pass
attempts = 1

def withdraw():
    global attempts
    save_pin = 1234                      # hard-coded
    balance = 10000                      # hard-coded
    pin = int(input("Enter the pin: "))

    if save_pin == pin:

        try:
            amt = float(input("Enter amount to withdraw: "))
            temp_balance = balance - amt

            if temp_balance < 1000:
                raise BalanceExceptionError("Insufficient balance")
            balance = balance -amt
            print("Reminder amount is:",temp_balance)

        except Exception as var:
            print(var)

    else:
        ans = input("Wrong pin,Do you want to continue again:(y/n)")
        if ans == "y" or ans == "Y":
            attempts +=1
            try:
                if attempts == 4:
                    raise AttemptExceptionError("Too many attempts, your account is blocked for an hour")
            except Exception as var:
                print(var)
                time.sleep(3600)
            else:
                withdraw()

        else:
            print("Thank You!")
            return


withdraw()

     
