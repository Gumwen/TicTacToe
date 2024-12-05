import random

def computer_turn(board, symbol):
    while True:
        row, col = random.randint(0, 2), random.randint(0, 2)
        if board[row][col] == " ":
            board[row][col] = symbol 
            break
