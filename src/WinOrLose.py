def check_win_or_draw(board):
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return f"{board[i][0]} wins!"
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return f"{board[0][i]} wins!"

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return f"{board[0][0]} wins!"
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return f"{board[0][2]} wins!"

    # Check for draw
    if all(board[row][col] != " " for row in range(3) for col in range(3)):
        return "It's a draw!"

    return None
