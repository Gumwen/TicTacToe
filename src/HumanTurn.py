def human_turn(board, symbol):
    while True:
        move = input("Enter your move (row and column): ")
        row, col = map(int, move.split())
        if board[row][col] == " ":
            board[row][col] = symbol
            break
        else:
            print("Cell is already occupied. Choose another cell.")
