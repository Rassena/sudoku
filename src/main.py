from sudoku import Sudoku
from interface import print_board


def training_board(board):
    board[0] = [0, 0, 0, 8, 0, 0, 3, 0, 0]
    board[1] = [0, 0, 0, 0, 3, 0, 5, 0, 0]
    board[2] = [0, 8, 3, 0, 4, 0, 0, 0, 0]

    board[3] = [0, 0, 2, 0, 0, 0, 0, 0, 0]
    board[4] = [0, 9, 0, 6, 2, 1, 0, 3, 4]
    board[5] = [0, 0, 0, 3, 0, 0, 2, 0, 0]

    board[6] = [0, 0, 0, 9, 0, 8, 0, 0, 3]
    board[7] = [0, 0, 9, 0, 6, 7, 0, 0, 0]
    board[8] = [0, 0, 0, 4, 5, 0, 0, 2, 6]


def training_board_2(board):

    board[0] = [2, 0, 0, 5, 0, 7, 0, 0, 0]
    board[1] = [0, 0, 6, 2, 3, 0, 1, 0, 0]
    board[2] = [7, 5, 3, 6, 0, 0, 0, 4, 8]

    board[3] = [0, 0, 0, 8, 0, 0, 4, 5, 1]
    board[4] = [3, 0, 0, 0, 6, 0, 9, 0, 2]
    board[5] = [0, 8, 5, 0, 2, 0, 0, 3, 0]

    board[6] = [5, 0, 1, 0, 0, 9, 6, 0, 0]
    board[7] = [0, 4, 9, 7, 0, 0, 0, 0, 3]
    board[8] = [8, 2, 7, 0, 0, 6, 0, 9, 0]


if __name__ == "__main__":
    sudoku = Sudoku()
    training_board_2(sudoku.board)
    print_board(sudoku.board)

    while sudoku.make_trivial_move():
        print()
        print_board(sudoku.board)
        print()
    print("No trivial Moves")
