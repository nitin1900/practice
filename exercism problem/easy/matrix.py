#copy-paste fom ai...

def get_matrix(matrix_string: str):
    rows = [
        [int(num) for num in line.split()]
        for line in matrix_string.strip().splitlines()
    ]
    columns = [list(col) for col in zip(*rows)]
    return rows, columns

print("Enter your matrix (one row per line).")
print("Press Enter on an empty line to finish:\n")

lines = []
while True:
    line = input()
    if line.strip() == "":
        break
    lines.append(line)

matrix_input = "\n".join(lines)

rows, columns = get_matrix(matrix_input)

print("\nRows:")
for row in rows:
    print(row)

print("\nColumns:")
for col in columns:
    print(col)

#solution...

class Matrix:
    def __init__(self, matrix_string):
        self.matrix = [[int(i) for i in mat.split()] for mat in matrix_string.split("\n")]

    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        return [col[index - 1] for col in self.matrix]

