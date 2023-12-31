"""Interface of Sudoku"""


def print_board(board):
    """Print current state of sudoku board"""
    print("+-+-+-+-+-+-+-+-+-+")
    for row in range(len(board)):
        print("", end="|")
        for col in range(len(board[row])):
            if board[row][col] == 0:
                print(" ", end="|")
            else:
                print(board[row][col], end="|")
        print("\n+-+-+-+-+-+-+-+-+-+")
