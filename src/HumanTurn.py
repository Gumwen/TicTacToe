def human_turn(board):
    while True:
        move = input("Enter your move (row and column): ")
        row, col = map(int, move.split())
        if board[row][col] == " ":
            board[row][col] = "X"
            break
        else:
            print("Cell is already occupied. Try again.")
