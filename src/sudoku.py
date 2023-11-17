
class Sudoku:

    vertical_length = 9
    horizontal_length = 9
    square_vertical_length = 3
    square_horizontal_length = 3

    def __init__(self):
        self.board = [[0] * self.vertical_length for _ in range(self.horizontal_length)]

    def is_valid_horizontal(self, row, number):
        for d_col in range(self.horizontal_length):
            if self.board[row][d_col] == number:
                return False
        return True

    def is_valid_vertical(self, col,  number):
        for d_row in range(self.vertical_length):
            if self.board[d_row][col] == number:
                return False
        return True

    def is_valid_square(self, row, col, number):
        square_vertical = col//self.square_vertical_length
        square_horizontal = row//self.square_horizontal_length
        for d_row in range(square_horizontal*self.square_horizontal_length,square_horizontal*self.square_horizontal_length+3):
            for d_col in range(square_vertical*self.square_vertical_length,square_vertical*self.square_vertical_length+3):
                if self.board[d_row][d_col] == number:
                    return False
        return True

    def is_valid_move(self, row, col, number):
        if self.board[row][col] == 0:
            return self.is_valid_horizontal(row, number) and self.is_valid_vertical(col, number) and self.is_valid_square(row, col, number)
        return False

    def make_move(self, row, col, number):
        self.board[row][col] = number
