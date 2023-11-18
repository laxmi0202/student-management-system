import mysql.connector
mydb=mysql.connector.connect(host="localhost",password="indu@123",user="root",database="newstudent",auth_plugin="mysql_native_password")
#if conn.is_connected():
    #print("conn is established...")
#c=conn.cursor()
#c.execute("create database vijaya")
#for i in c:
class Student:
    def __init__(self):
        self.name = input("\n\tEnter student name: ")
        self.rollno = input("\n\tEnter roll number: ")
        self.phonenum = input("\tEnter phone num: ")
        self.m2 = input("\tEnter marks for subject 2: ")
        data1=(self.name,self.rollno,self.phonenum,self.m2)
        sql='insert into students values(%s,%s,%s,%s)'
        x=mydb.cursor()
        x.execute(sql,data1)
        mydb.commit()
        x.close()


    def display(self):
        print(self.name)
        print(self.rollno)
        print(self.phonenum)
        print(self.m2)

class Option:
    def __init__(self):
        self.students = []

    def opns(self):
        print("-->WELCOME TO JNTUHCEJ-->\n")
        print("WELCOME TO STUDENT MANAGEMENT SYSTEM")
        print("\t 1)to get student details")
        print("\t 2)to add new student")
        print("\t 3)to update student details")
        print("\t 4)to get number of students")
        print("\t 5)to get all student details")
        print("\t 6)to remove any student")
        print("\t 7)to exit")


    def add_student(self):
        student = Student()
        self.students.append(student)
        print("Student added successfully")

    def getdetails(self, rollno):
        for student in self.students:
            if student.rollno == rollno:
                return f"Name: {student.name}\nRoll No.: {student.rollno}\nPhone Num.: {student.phonenum}\nMarks for Subject 2: {student.m2}"
        return "Student not found"

    def update_student(self, rollno):
        for student in self.students:
            if student.rollno == rollno:
                student.name = input("\nEnter new name: ")
                student.phonenum = input("\nEnter new phone number: ")
                student.m2 = input("\nEnter new marks for subject 2: ")
                print("Student details updated successfully")
                return
        print("Student not found")

    def remove_student(self, rollno):
        for student in self.students:
            if student.rollno == rollno:
                self.students.remove(student)
                print("Student removed successfully")
                return
        print("Student not found")

obj = Option()

while True:
    obj.opns()
    opns = int(input("\nEnter the option: "))

    if opns == 1:
        rollno = input("\nEnter the roll number: ")
        print(obj.getdetails(rollno))

    elif opns == 2:
        obj.add_student()

    elif opns == 3:
        rollno = input("\nEnter the roll number: ")
        obj.update_student(rollno)

    elif opns == 4:
        print( len(obj.students))

    elif opns == 5:
        for student in obj.students:
            student.display()
            print()

    elif opns == 6:
        rollno = input("\nEnter the roll number: ")
        obj.remove_student(rollno)

    elif opns == 7:
        print("Exiting program...")
        print("thankyou from jntuhcej")
        break
