#copy-paste from ai...

class School:
    def __init__(self):
        self.roster = {}

    def add_student(self, name, grade):
        if grade not in self.roster:
            self.roster[grade] = []

        if name in self.roster[grade]:
            return "Student already exists in this grade."

        self.roster[grade].append(name)
        self.roster[grade].sort()
        return "OK."

    def get_students_in_grade(self, grade):
        return self.roster.get(grade, [])

    def get_all_students(self):
        result = []
        for grade in sorted(self.roster.keys()):
            result.extend(sorted(self.roster[grade]))
        return result


# Interactive part
school = School()

while True:
    print("\n--- School Menu ---")
    print("1. Add student")
    print("2. View students in a grade")
    print("3. View all students")
    print("4. Exit")

    try:
        choice = int(input("Enter choice: "))

        if choice == 1:
            name = input("Enter student name: ")
            grade = int(input("Enter grade: "))
            print(school.add_student(name, grade))

        elif choice == 2:
            grade = int(input("Enter grade: "))
            students = school.get_students_in_grade(grade)
            if students:
                print("Students:", ", ".join(students))
            else:
                print("No students found in this grade.")

        elif choice == 3:
            students = school.get_all_students()
            if students:
                print("All students:", ", ".join(students))
            else:
                print("No students enrolled.")

        elif choice == 4:
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

    except ValueError:
        print("Please enter valid numbers.")
    except EOFError:
        print("\nExiting...")
        break

#solution...

class School:
    def __init__(self):
        self.school = {}
        self.add = []

    def add_student(self, name, grade):
        if name not in self.roster():
            self.school[grade] = self.school.get(grade, []) + [name]
            self.add.append(True)
        else:
            self.add.append(False)

    def added(self):
        return self.add
    
    def roster(self):
        return [name
                for grade in sorted(self.school.keys())
                for name in sorted(self.school[grade])]
    
    def grade(self, grade_number):
        return sorted(self.school.get(grade_number, []))