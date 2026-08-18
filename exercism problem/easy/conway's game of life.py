#copy-pasted from ai...

grid = input("Enter [1,2,3];[row2]: ").split(";")

# Step 1: Convert input into proper 2D integer grid
board = []
for row in grid:
    clean = row.replace("[", "").replace("]", "").split(",")
    board.append([int(x) for x in clean])

# Step 2: Directions for 8 neighbors
directions = [(-1,-1), (-1,0), (-1,1),
              (0,-1),         (0,1),
              (1,-1), (1,0), (1,1)]

rows = len(board)
cols = len(board[0])

# Step 3: Create new grid
new_board = [[0]*cols for _ in range(rows)]

# Step 4: Apply Game of Life rules
for r in range(rows):
    for c in range(cols):
        live_neighbors = 0
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < rows and 0 <= nc < cols:
                live_neighbors += board[nr][nc]
        
        if board[r][c] == 1:
            if live_neighbors == 2 or live_neighbors == 3:
                new_board[r][c] = 1
        else:
            if live_neighbors == 3:
                new_board[r][c] = 1

# Step 5: Output
print("Next generation:")
for row in new_board:
    print(row)

#solution...

def tick(matrix):
    if len(matrix) == 0:
        return []
    row_num = len(matrix)
    row_length = len(matrix[0])
    result = []
    for row_index in range(row_num):
        new_row = []
        result.append(new_row)
        for index in range(row_length):
            anc = count(matrix, row_num, row_length, row_index, index)
            alive = matrix[row_index][index]
            new_row.append(
                alive and (anc == 2 or anc == 3)
                or not alive and anc == 3
            )
    return result
def count(matrix, row_num, row_length, row_index, index):
    neighbors = [
        (index, row_index + 1), 
        (index + 1, row_index + 1), 
        (index + 1, row_index), 
        (index + 1, row_index - 1),
        (index, row_index - 1), 
        (index - 1, row_index - 1), 
        (index - 1, row_index), 
        (index - 1, row_index + 1) 
    ]
    return len([n
        for n in neighbors
        if (
            0 <= n[0] < row_length 
            and 0 <= n[1] < row_num
            and matrix[n[1]][n[0]]
        )
    ])