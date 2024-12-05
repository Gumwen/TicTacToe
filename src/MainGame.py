from HumanTurn import human_turn
from ComputerTurn import computer_turn
from WinOrLose import check_win_or_draw

def initialize_board():
    return [[" " for _ in range(3)] for _ in range(3)]

def display_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def main():
    board = initialize_board()
    while True:
        first_player = input("Are you 'X' or 'O'?")
        if first_player in ["X", "O"]:
            break
        print("Invalid symbol! you have to choose either 'X' or 'O'.")
    human_symbol = first_player
    computer_symbol = "O" if human_symbol = "X" else "X"
    
    current_player = "Human"

    while True:
        display_board(board)
        if current_player == "Human":
            human_turn(board, human_symbol)
        else:
            computer_turn(board, computer_symbol)
        
        result = check_win_or_draw(board)
        if result:
            print(result)
            break
        
        current_player = "Computer" if current_player == "Human" else "Human"

if __name__ == "__main__":
    main()
