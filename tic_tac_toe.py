# Initialize the board
board = [" " for _ in range(9)]

# Display the board
def print_board():
    print("\n")
    for i in range(3):
        print(" | ".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("--+---+--")
    print("\n")

# Check for a win
def check_winner(player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8], # rows
        [0,3,6], [1,4,7], [2,5,8], # columns
        [0,4,8], [2,4,6]           # diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

# Check if board is full
def is_draw():
    return " " not in board

# Main game loop6

def play_game():
    current_player = "X"
    while True:
        print_board()
        try:
            move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
            if move < 0 or move > 8 or board[move] != " ":
                print("Invalid move, try again.")
                continue
            board[move] = current_player
            if check_winner(current_player):
                print_board()
                print(f"🎉 Player {current_player} wins!")
                break
            elif is_draw():
                print_board()
                print("It's a draw!")
                break
            current_player = "O" if current_player == "X" else "X"
        except ValueError:
            print("Please enter a number between 1 and 9.")

# Start the game
play_game()
