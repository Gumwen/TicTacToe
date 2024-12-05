def human_turn(board, symbol):
    while True:
        move = input("Enter your move (row column e.g., 0 0 for first cell): ")
        try:
            row, col = map(int, move.split())
            if row not in [0, 1, 2] or col not in [0, 1, 2]:
                print("Invalid input! Please enter numbers between 0 and 2 for both row and column.")
                continue
            if board[row][col] == " ":
                board[row][col] = symbol
                break
            else:
                print("Cell is already occupied. Choose another cell.")
        except ValueError:
            print("Invalid input! Please enter two numbers separated by a space.")
