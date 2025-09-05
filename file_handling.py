

def save_to_file(students, filename="students.txt"):
    with open(filename, "w") as file:
        for student_id, info in students.items():
            file.write(f"ID: {student_id}\n")
            file.write(f"Name: {info['name']}\n")
            file.write(f"Age: {info['age']}\n")
            file.write(f"Grades: {' '.join(map(str, info['grades']))}\n\n")

def load_from_file(filename="students.txt"):
    students = {}
    with open(filename, "r") as file:
        lines = file.readlines()
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if line.startswith("ID:"):
            student_id = line.replace("ID: ", "")
            name = lines[i+1].strip().replace("Name: ", "")
            age = int(lines[i+2].strip().replace("Age: ", ""))
            grades_line = lines[i+3].strip().replace("Grades: ", "")
            grades = list(map(int, grades_line.split()))
            students[student_id] = {"name": name, "age": age, "grades": grades}
            i += 5  # skip to next student (including blank line)
        else:
            i += 1
    return students
