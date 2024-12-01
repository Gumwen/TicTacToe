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
    current_player = "Human"

    while True:
        display_board(board)
        if current_player == "Human":
            human_turn(board)
        else:
            computer_turn(board)
        
        result = check_win_or_draw(board)
        if result:
            print(result)
            break
        
        current_player = "Computer" if current_player == "Human" else "Human"

if __name__ == "__main__":
    main()
