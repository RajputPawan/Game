# tic_tac_toe.py

def print_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def check_winner(board, player):
    win_positions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # cols
        (0, 4, 8), (2, 4, 6)              # diagonals
    ]
    for a, b, c in win_positions:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

def board_full(board):
    return all(cell in ("X", "O") for cell in board)

def get_move(board, player):
    while True:
        try:
            pos = int(input(f"Player {player}, enter position (1-9): ")) - 1
            if pos < 0 or pos > 8:
                print("Position must be between 1 and 9.")
                continue
            if board[pos] in ("X", "O"):
                print("That position is already taken.")
                continue
            return pos
        except ValueError:
            print("Please enter a valid number.")

def play_game():
    board = [str(i) for i in range(1, 10)]
    current_player = "X"

    print("Welcome to Tic-Tac-Toe!")
    print("Positions are numbered as follows:")
    print_board([str(i) for i in range(1, 10)])

    while True:
        print_board(board)
        move = get_move(board, current_player)
        board[move] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    play_game()
