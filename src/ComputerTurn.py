import random

def computer_turn(board, symbol):
    opp_symbol = "X" if symbol == "O" else "O"
    while True:
        row, col = random.randint(0, 2), random.randint(0, 2)
        if board[row][col] == " ":
            board[row][col] = symbol
            break
