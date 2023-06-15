import ai, time
import move as mov
import global_vars as G


# Function to control flow, return a move
def control_flow(mode):
    # Get player
    player = "X" if G.BOARD.X_turn else "O"
    # Human or AI
    if mode == 0:
        # Get human move
        print("Player ", player, " your turn.")
        while True:
            move_str = input("Please type row and col separated by a space: ")
            row = int(move_str[0])
            col = int(move_str[2])
            if G.BOARD.check_valid(row, col):
                break
            else:
                print("Invalid move, try again")
        move = mov.Move(row, col)
    else:
        time.sleep(G.AI_DELAY)
        move = ai.choose_move(mode)
    # Print confirmation
    message = "(Human) " if mode == 0 else "(AI) "
    message += "Player " + player + " "
    message += str(move.row) + " " + str(move.col)
    print(message)
    # Return move
    return move


# Start the game
print("Let's start the board:")
print("Player X level: ", G.PLAYER_X_MODE)
print("Player O level: ", G.PLAYER_O_MODE)
print(G.BOARD)

# Loop until either draw or someone wins
while G.BOARD.check_win() == " " and not G.BOARD.check_draw():
    # Control Flow
    new_move = control_flow(G.PLAYER_X_MODE) if G.BOARD.X_turn else control_flow(G.PLAYER_O_MODE)

    # Push in the move from control flow
    G.BOARD.push_move(new_move)

    # Print updated board
    print(G.BOARD)

# Print win message
if G.BOARD.check_win() == "X":
    print("Player X wins!")
elif G.BOARD.check_win() == "O":
    print("Player O wins!")
else:
    print("It is a draw!")
