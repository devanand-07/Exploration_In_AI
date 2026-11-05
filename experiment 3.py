students = {}

def add_student():
    roll = input("Enter Roll No: ")
    name = input("Enter Name: ")
    dept = input("Enter Department: ")
    students[roll] = {"Name": name, "Department": dept}
    print("Student added successfully.")

def view_students():
    if not students:
        print("No student records found.")
        return
    for roll, data in students.items():
        print("",roll, 
        "|",data["Name"], 
        "|",data["Department"])

def search_student():
    roll = input("Enter Roll No to search: ")
    if roll in students:
        print(student[roll])
    else:
        print("student not found")

def delete_student():
    roll = input("Enter Roll No to delete: ")
    if roll in students:
        del students[roll]
        print("Student deleted successfully.")
    else:
        print("Student not found.")

while True:
    print("\n1. Add Student")
    print("2.View Student")
    print("3.Search student")
    print("4.Delete Studenet")
    print("5.Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Existing...")
        break
    else:
        print("Invalid choice.")