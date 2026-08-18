#my code...done some silly mistake tho...

user=[]
user=input("1 2 3 4;number2 : ").split(";")
matrix=list()
for i in range(len(user)):
    clean=user[i].split()# it does not mean 12 to split it means 1 2 to split
    matrix.append([int(x) for x in clean])#i forgot the bracket
for row_index in range(len(matrix)):#copy paste this part from gemini
    current_row = matrix[row_index]
    maxi = max(current_row)
    maxi_index = current_row.index(maxi)
    column = []
    for check_row in matrix:
        column.append(check_row[maxi_index])
    if maxi == min(column):
        print("Saddle Point found at Row:", row_index+1, "Column:", maxi_index+1)
        print("saddle point is",maxi)

#solution...

def saddle_points(matrix):
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise ValueError('irregular matrix')

    row_maxima = list(map(max, matrix))
    col_minima = list(map(min, list(zip(*matrix))))

    return [
        {'row': r+1, 'column': c+1}
        for r, row_max in enumerate(row_maxima)
        for c, col_min in enumerate(col_minima)
        if row_max == col_min
    ]