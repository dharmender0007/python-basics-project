def load_students(filename="students.txt"):
    students = {}
    try:
        with open(filename, "r") as file:
            for line in file:
                if ":" in line:
                    name, marks = line.strip().split(":")
                    students[name.strip()] = int(marks.strip())
    except FileNotFoundError:
        open(filename, "w").close()  # Create the file if it doesn't exist
    return students

def save_students(students, filename="students.txt"):
    with open(filename, "w") as file:
        for name, marks in students.items():
            file.write(f"{name}: {marks}\n")

def add_student(students):
    name = input("Enter student name: ").strip()
    if name in students:
        print("Student already exists.")
    else:
        try:
            marks = int(input("Enter marks: "))
            students[name] = marks
            print("Student added.")
        except ValueError:
            print("Please enter valid numeric marks.")

def remove_student(students):
    name = input("Enter student name to remove: ").strip()
    if name in students:
        del students[name]
        print("Student removed.")
    else:
        print("Student not found.")

def search_student(students):
    name = input("Enter student name to search: ").strip()
    if name in students:
        print(f"{name}'s marks: {students[name]}")
    else:
        print("Student not found.")

def display_all(students):
    if not students:
        print("No student data found.")
    else:
        for name, marks in students.items():
            print(f"{name}: {marks}")


def main():
    students = load_students()

    while True:
        print("\n--- Student Marks Manager ---")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. Search Student")
        print("4. Display All")
        print("5. Exit/n")

        choice = input("Enter choice (1-5): ").strip()

        if choice == '1':
            add_student(students)
        elif choice == '2':
            remove_student(students)
        elif choice == '3':
            search_student(students)
        elif choice == '4':
            display_all(students)
        elif choice == '5':
            print("File saved as student.txt       Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
   
