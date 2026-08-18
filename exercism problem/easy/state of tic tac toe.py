#copy paste from ai...

print("Enter the board (3 rows, each with 3 values separated by space, use X, O, or . for empty):")

board = []
for _ in range(3):
    row = input().split()
    board.append(row)

# Count X and O
x_count = sum(row.count('X') for row in board)
o_count = sum(row.count('O') for row in board)

# Function to check winner
def check_winner(player):
    # rows
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
    # columns
    for j in range(3):
        if all(board[i][j] == player for i in range(3)):
            return True
    # diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

x_win = check_winner('X')
o_win = check_winner('O')

# Step 1: Validate counts
if not (x_count == o_count or x_count == o_count + 1):
    print("Invalid")
elif x_win and o_win:
    print("Invalid")
elif x_win and x_count != o_count + 1:
    print("Invalid")
elif o_win and x_count != o_count:
    print("Invalid")
else:
    if x_win or o_win:
        print("Win")
    elif x_count + o_count == 9:
        print("Draw")
    else:
        print("Ongoing")

#solution...

"""Determine the state of Tic Tac Toe."""
WIN_PATTERNS = [
    # Columns
    tuple((x, y) for x in range(3)) for y in range(3)
] + [
    # Rows
    tuple((x, y) for y in range(3)) for x in range(3)
    # Diagonals:
] + [tuple((i, i) for i in range(3))] +  [tuple((i, 2 - i) for i in range(3))]


def gamestate(board: list[str]) -> str:
    """Return the state of a Tic Tac Toe game."""
    moves: dict[str, set[tuple[int, int]]] = {c: set() for c in "XO"}
    for y, row in enumerate(board):
        for x, char in enumerate(row):
            if char != " ":
                moves[char].add((x, y))
    counts = {player: len(m) for player, m in moves.items()}

    if counts["X"] < counts["O"]:
        raise ValueError("Wrong turn order: O started")
    if counts["X"] > counts["O"] + 1:
        raise ValueError("Wrong turn order: X went twice")

    winner = {
        player
        for pattern in WIN_PATTERNS
        for player, moved in moves.items()
        if all(p in moved for p in pattern)
    }

    if len(winner) == 2:
        raise ValueError("Impossible board: game should have ended after the game was won")
    if len(winner) == 1:
        return "win"
    if counts["X"] + counts["O"] == 9:
        return "draw"
    return "ongoing"
