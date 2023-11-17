def print_board(board):
    print("+-+-+-+-+-+-+-+-+-+")
    for row in range(8):
        print("|", end=" |")
        for col in range(8):
            if board[row][col] == 0:
                print(" ", end="|")
            else:
                print(board[row][col], end="|")
        print("\n+-+-+-+-+-+-+-+-+-+")
