#copy-pasted code from ai...

def count_rectangles(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    for top in range(rows):
        for bottom in range(top + 1, rows):

            valid_columns = []

            for col in range(cols):
                if grid[top][col] == '+' and grid[bottom][col] == '+':

                    valid = True
                    for r in range(top + 1, bottom):
                        if grid[r][col] not in ['|', '+']:
                            valid = False
                            break

                    if valid:
                        valid_columns.append(col)

            for i in range(len(valid_columns)):
                for j in range(i + 1, len(valid_columns)):
                    left = valid_columns[i]
                    right = valid_columns[j]

                    top_valid = all(grid[top][c] in ['-', '+'] for c in range(left + 1, right))
                    bottom_valid = all(grid[bottom][c] in ['-', '+'] for c in range(left + 1, right))

                    if top_valid and bottom_valid:
                        count += 1

    return count


# Interactive input
n = int(input("Enter number of rows: "))

grid = []
print("Enter the diagram line by line:")

for _ in range(n):
    line = input()
    grid.append(line)

# Run and print result
result = count_rectangles(grid)
print("Number of rectangles:", result)




#solution...




from itertools import combinations

def rectangles(strings):
    return sum(1
        for vs in combinations(vertices(strings), 4)
        if is_rectangle(strings, vs)
    )

def vertices(strings):
    return [(i,j)
        for j,row in enumerate(strings)
        for i,ch in enumerate(row)
        if ch == '+'
    ]

def is_rectangle(strings, verts):
    top_left, bottom_left, top_right, bottom_right = sorted(verts)
    return all([
        h_edge(strings, top_left,    top_right),
        h_edge(strings, bottom_left, bottom_right),
        v_edge(strings, top_left,    bottom_left),
        v_edge(strings, top_right,   bottom_right),
    ])

def v_edge(strings, v1, v2):
    x1, y1 = v1
    x2, y2 = v2

    return x1 == x2 and y1 < y2 and all([
        strings[j][x1] in "+|"
        for j in range(y1, y2+1)
    ])

def h_edge(strings, v1, v2):
    x1, y1 = v1
    x2, y2 = v2

    return y1 == y2 and x1 < x2 and all([
        strings[y1][i] in "+-"
        for i in range(x1, x2+1)
    ])