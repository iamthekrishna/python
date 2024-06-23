##################################### Student_Date####################################
student={}  # key:value id, name, age ==> key=id,  value: {"Name", "Age"}
# 1:{"Name": pooja, "Age":24}
# id, Name, Age

def add():
    id=int(input("Enter the student Id: "))
    name=input("Enter the student Name: ")
    age=int(input("Enter the student Age: "))
    student[id]={"Name":name,"Age":age}
    print("Student added sucessfully")

def display():
   for id,info in student.items():
      print("ID: "+str(id)+" Name: "+ info["Name"] + " Age: " + str(info["Age"]))

def search():
    User=int(input("Enter the student Id: "))
    for id,info in student.items():
        if User==id:
            print("Found ID: "+ str(id)+" Name "+ info["Name"]+ " Age: "+str(info["Age"]))

def update():
   User=int(input("Enter the student Id: "))
   for id,info in student.items():
       if User==id:
        name=input("Enter the new name: ")
        age=int(input("Enter the new Age: "))
        student[id]={"Name":name,"Age":age}
        print("Record updated successfully!")
        break

def delete():
    userId=int(input("Enter the student Id: "))
    del student[userId]
    print("Record deleted successfuly!")

def Menu():
    print("1) Add Student into for admission.")
    print("2) Display Students record.")
    print("3) Search Student record.")
    print("4) Update Student record.")
    print("5) Delete Student record.")
    print("6) Exit!.")
    choice = int(input("Choose one of the option from above menu."))
    if choice == 1:
        add()
    elif choice == 2:
        display()
    elif choice == 3:
        search()
    elif choice == 4:
        update()
    elif choice ==5:
        delete()
    elif choice == 6:
        return True
    else:
        print("Invalid choice man!, please select valid one from 1-6 :) ")
    print("")

while True:
    exit = Menu()
    if exit:
        break

print("")
print("Thanks you visit again!")

