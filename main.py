print("Running main.py from", __file__)
from file_handling import save_to_file, load_from_file

students = {}

def add_student():
    student_id = input("Enter student ID: ")
    if student_id in students:
        print("Student already exists.")
        return
    name = input("Enter name: ")
    age = input("Enter age: ")
    grades_input = input("Enter grades separated by spaces: ")
    grades = list(map(int, grades_input.split()))
    students[student_id] = {"name": name, "age": int(age), "grades": grades}
    print(f"Student {name} added.")

def display_students(students):
    for student_id, info in students.items():
        print(f"ID: {student_id}")
        print(f"Name: {info['name']}")
        print(f"Age: {info['age']}")
        print(f"Grades: {' '.join(map(str, info['grades']))}")
        print()

def update_student():
    student_id = input("Enter student ID to update: ")
    if student_id not in students:
        print("Student not found.")
        return
    print("What do you want to update?")
    print("1. Name")
    print("2. Age")
    print("3. Grades")
    choice = input("Enter choice: ")
    if choice == "1":
        new_name = input("Enter new name: ")
        students[student_id]["name"] = new_name
        print("Name updated.")
    elif choice == "2":
        new_age = input("Enter new age: ")
        students[student_id]["age"] = int(new_age)
        print("Age updated.")
    elif choice == "3":
        new_grades = list(map(int, input("Enter new grades separated by spaces: ").split()))
        students[student_id]["grades"] = new_grades
        print("Grades updated.")
    else:
        print("Invalid choice.")

def delete_student():
    student_id = input("Enter student ID to delete: ")
    if student_id in students:
        del students[student_id]
        print("Student deleted.")
    else:
        print("Student not found.")

def menu():
    global students  # Declare global here, at the start of the function

    while True:
        print("\n===== Student Information System =====")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Save to File")
        print("6. Load from File")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "7":
            print("Exiting program.")
            break
        elif choice == "1":
            add_student()
        elif choice == "2":
            display_students(students)
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            save_to_file(students)
        elif choice == "6":
            students = load_from_file()  
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    menu()