def check_win_or_draw(board, human_symbol):
    # Check the rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            if board[i][0] == human_symbol:
                return "Player wins!" 
            else:
                return "Computer wins!"  
        if board[0][i] == board[1][i] == board[2][i] != " ":
            if board[0][i] == human_symbol:
                return "Player wins!"
            else:
                return "Computer wins!"

    # Check the diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        if board[0][0] == human_symbol:
            return "Player wins!"
        else:
            return "Computer wins!"
    if board[0][2] == board[1][1] == board[2][0] != " ":
        if board[0][2] == human_symbol:
            return "Player wins!"
        else:
            return "Computer wins!"

    # Check for draw
    if all(board[row][col] != " " for row in range(3) for col in range(3)):
        return "It's a draw!"

    return None
