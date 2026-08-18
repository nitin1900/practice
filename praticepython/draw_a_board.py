def print_horiz_line(board_size):
    print(" --- " * board_size)

def print_vert_line(board_size):
    print("|   " * (board_size + 1))

def draw_board(board_size):
    for index in range(board_size):
        print_horiz_line(board_size)
        print_vert_line(board_size)

    print_horiz_line(board_size)

if __name__ == "__main__":
    board_size = int(input("What size of game board? "))
    draw_board(board_size)
