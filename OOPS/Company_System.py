# 
class Company:

    def __init__(self):
        self.EmployName = {1111 : "A", 1112 : "B", 1113 : "C"}
        self.Salary = {1234 : 0, 2345 : 0, 3456 : 0}
        self.AccountNo = {1111 : 1234, 1112 : 2345, 1113 : 3456}
        self.PresentDay = {1111 : 0, 1112 : 0, 1113 : 0}


    # Start
    # 1) Enter your Employee Id to enter into office.
    # 2) Present day attendance
    # 3) Salary Credit of 1 day
    # 4) Total Salary : Employee Id
    def AccessOffice(self):
        EmpId = int(input("Enter your EmpId:"))
        EmployeePresent = False

        for id, name in self.EmployName.items():
            if id == EmpId:
                self.PresentDay[EmpId] = self.PresentDay[EmpId] + 1
                AccNo = self.AccountNo[EmpId]
                self.Salary[AccNo] = self.Salary[AccNo] + 1000
                EmployeePresent = True
                break
            else:
                pass
        if not EmployeePresent:
            print("Employee not in company.")

    def ShowSalary(self):
        EmpId = int(input("Enter your EmpId"))
        EmployeePresent = False

        for id, name in self.EmployName.items():
            if id == EmpId:
                print("Employee Name: {}".format(self.EmployName[EmpId]))
                print("Employee Present Day: {}".format(self.PresentDay[EmpId]))
                AccNo = self.AccountNo[EmpId]
                print("Employee Total Salary: {}".format(self.Salary[AccNo]))
                EmployeePresent = True
                break
            else:
                pass
        if not EmployeePresent:
            print("Employee not in company.")

    def start(self):
        while True:
            choice = int(input("1) Enter your EmpId to access office\n2) Total Salary\n3) Exit."))
            if choice == 1:
                self.AccessOffice()
            elif choice == 2:
                self.ShowSalary()
            elif choice == 3:
                break
            else :
                print("Invalid choice.")
        pass

Com = Company()
Com.start()



