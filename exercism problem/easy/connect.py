#copy-pasted from ai...

def get_neighbors(r, c, n, m):
    # 6 possible moves in hex grid
    directions = [(-1, 0), (-1, 1), (0, -1),
                  (0, 1), (1, -1), (1, 0)]
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < m:
            yield nr, nc


def dfs(board, visited, stack, target_check, player):
    n, m = len(board), len(board[0])

    while stack:
        r, c = stack.pop()
        if (r, c) in visited:
            continue
        visited.add((r, c))

        if target_check(r, c):
            return True

        for nr, nc in get_neighbors(r, c, n, m):
            if board[nr][nc] == player and (nr, nc) not in visited:
                stack.append((nr, nc))

    return False


def check_winner(board):
    n, m = len(board), len(board[0])

    # Check O (top → bottom)
    visited = set()
    stack = [(0, c) for c in range(m) if board[0][c] == 'O']
    if dfs(board, visited, stack, lambda r, c: r == n - 1, 'O'):
        return 'O'

    # Check X (left → right)
    visited = set()
    stack = [(r, 0) for r in range(n) if board[r][0] == 'X']
    if dfs(board, visited, stack, lambda r, c: c == m - 1, 'X'):
        return 'X'

    return None


def main():
    print("Enter board dimensions:")
    n = int(input("Rows: "))
    m = int(input("Columns: "))

    print("\nEnter the board row by row (use '.', 'O', 'X'):")
    board = []
    for i in range(n):
        row = input(f"Row {i+1}: ").strip().split()
        if len(row) != m:
            print("Invalid row length. Try again.")
            return
        board.append(row)

    winner = check_winner(board)

    print("\nBoard:")
    for i, row in enumerate(board):
        print(" " * i + " ".join(row))  # formatting like hex board

    if winner:
        print(f"\nWinner: Player {winner}")
    else:
        print("\nNo winner")


if __name__ == "__main__":
    main()

#solution...



class ConnectGame:
    def __init__(self, board):
        self.board = [[stone for stone in row] for row in board.replace(' ', '').splitlines()]  # Generate 2d array
        self.neighbours = [(0, 1), (1, 0), (1, -1), (0, -1), (-1, 0), (-1, 1)]  # hex neighbours relative pos in array

    def get_winner(self):  # check player 0, then X, if neither win output ' '
        for player in ['O', 'X']:
            result = self.checker(player)
            if result is True:
                return player
        return ''

    def checker(self, player):
        if player == 'O':  # set parameters for player O
            array = self.board
        if player == 'X':  # set parameters for player X
            array = list(zip(*self.board))  # transpose the board, so X becomes top to down
        # get player first and last row stones
        stones = [(index, 0) for index, stone in enumerate(array[0]) if stone == player]
        ends = [(index, len(array) - 1) for index, stone in enumerate(array[-1]) if stone == player]
        for stone in stones:  # search for stones connected to first row stones, loop till exhaustion
            for neighbour in self.neighbours:
                row = stone[1] + neighbour[1]
                col = stone[0] + neighbour[0]
                if row >= 0 and col >= 0:
                    try:
                        if array[row][col] == player and (col, row) not in stones:
                            stones.append((col, row))  # append stone to end of list so it will be looped over
                    except IndexError:
                        continue
        for end in ends:  # return true if one of the end stones is connected to first row stones
            if end in stones:
                return True
