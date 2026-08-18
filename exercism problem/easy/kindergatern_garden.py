#copy paste from ai...

class Garden:
    def __init__(self, diagram, students=None):
        if students is None:
            students = ["Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]
        self.students = sorted(students)
        rows = diagram.split("\n")
        self.row1 = rows[0]
        self.row2 = rows[1]
        self.plant_map = {
            "G": "Grass",
            "C": "Clover",
            "R": "Radishes",
            "V": "Violets"
        }

    def plants(self, name):
        i = self.students.index(name) * 2
        cups = [
            self.row1[i], self.row1[i+1],
            self.row2[i], self.row2[i+1]
        ]
        return [self.plant_map[c] for c in cups]


diagram = input("Enter the garden diagram (use \\n between rows): ").replace("\\n", "\n")
custom = input("Enter student names separated by space (or press Enter for default): ")

if custom.strip():
    students = custom.split()
    g = Garden(diagram, students)
else:
    g = Garden(diagram)

while True:
    name = input("Enter student name (or 'exit' to quit): ").title()
    if name.lower() == "exit":
        break
    if name not in g.students:
        print("Student not found")
    else:
        print(g.plants(name))

#solution...

DEFAULT_STUDENTS = (
    'Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred',
    'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry',
)

PLANTS = {
    'C': 'Clover',
    'G': 'Grass',
    'R': 'Radishes',
    'V': 'Violets',
}

class Garden(object):
    def __init__(self, diagram, students=DEFAULT_STUDENTS):
        self.lines = diagram.splitlines()
        self.students = sorted(students)

    def plants(self, student):
        index = self.students.index(student)*2
        return [PLANTS[p[i]] for p in self.lines for i in (index, index + 1)]