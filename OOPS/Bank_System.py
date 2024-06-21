class Bank:

    def __init__(self):
        self.AccountName = {1111 : "A", 1112 : "B", 1113 : "C" }
        self.AccountBalance = {1111 : 10000, 1112 : 10000, 1113 : 10000 }
        self.AccountPin = {1111 : 1234, 1112 : 3456, 1113 : 5678 }

    def validateAccount(self):
        Result = False
        Attempt = 0
        AccountNo = int(input("Enter the Account No."))
        while Attempt < 3:
            Pin = int(input("Enter the Security PIN."))
            if self.AccountPin[AccountNo] == Pin:
                Result = True
                break
            else:
                print("Invalied PIN!")
            Attempt = Attempt + 1
        if Attempt >= 3:
            print("Your Account temporary block, visit the branch customer care!")
            return Result, AccountNo
        return Result, AccountNo

    def withdraw(self):
        Access, AccNo = self.validateAccount()
        if Access:
            Ammount = int(input("Enter the ammount you wish to withdraw!\nRs."))
            # Check Account has sufficient balance
            if(Ammount <= self.AccountBalance[AccNo]):
                self.AccountBalance[AccNo] = self.AccountBalance[AccNo] - Ammount
                print("{0} Debited successfully!".format(Ammount))
                print("Total balance in your account is {0}".format(self.AccountBalance[AccNo]))
            else:
                print("Insufficient Balance")
 
    def credit(self):
        Access, AccNo = self.validateAccount()
        if Access:
            Ammount = int(input("Enter the ammount you wish to credit!\nRs."))
            self.AccountBalance[AccNo] = self.AccountBalance[AccNo] + Ammount
            print("{0} Credited successfully!".format(Ammount))
            print("Total balance in your account is {0}".format(self.AccountBalance[AccNo]))
 
    def start(self):
        print("Welcome to the HDFC Bank!")
        while True:
            C_OR_W = input("Enter the choice \n1) Withdraw money press 'W'\n2) Credit the account press 'C'\n3) Exit from the system press 'E'\n ")
            if C_OR_W == 'C':
                self.credit()
            elif C_OR_W == 'W':
                self.withdraw()
            elif C_OR_W == 'E':
                print("Thanks you, Visit again!")
                break
            else:
                print("Invalid choice!")
 
bank = Bank()
bank.start()