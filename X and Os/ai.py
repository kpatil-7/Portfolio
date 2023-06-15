import global_vars as G
import move as mov


def evaluate_file(file):
    # ___ neutral
    if file == (" ", " ", " "):
        return 0
    # XXO or OOX neutral
    non_blank = 0
    for i in range(0, 3):
        non_blank += 1 if file[i] == "X" or file[i] == "O" else 0
    if non_blank == 3:
        return 0
    # XO_ neutral
    # X__ benefit X
    # O__ benefit O
    # XX_ really benefit X
    # OO_ really benefit O
    net_X = 0
    for i in range(0, 3):
        if file[i] == "X":
            net_X += 1
        elif file[i] == "O":
            net_X -= 1
    if net_X == 0:
        return 0
    elif net_X < 0:
        return -10 ** (-net_X)
    else:
        return 10 ** net_X

def evaluate_board():
    m = G.BOARD.matrix
    # Positive for X, negative for O
    if G.BOARD.check_win() == "X":
        return 1000
    elif G.BOARD.check_win() == "O":
        return -1000
    elif G.BOARD.check_draw():
        return 0
    # Will take the simple approach, evaluate each file for score and add sum
    score = 0
    # Horizontal files
    for row in range(0, 3):
        to_test = tuple(m[row])
        score += evaluate_file(to_test)
    # Check for vertical files
    for col in range(0, 3):
        to_test = tuple([m[0][col], m[1][col], m[2][col]])
        score += evaluate_file(to_test)
    # Check for diagonal files
    first_dia = tuple([m[0][0], m[1][1], m[2][2]])
    score += evaluate_file(first_dia)
    second_dia = tuple([m[0][2], m[1][1], m[2][0]])
    score += evaluate_file(second_dia)
    # Regardless of player, the higher the better
    return score

# Adapted from this site
# https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-3-tic-tac-toe-ai-finding-optimal-move/
def choose_move(depth):
    best_score = -99999 if G.BOARD.X_turn else 99999
    best_move = None
    valid_list = list(G.BOARD.valid_set)
    for row, col in valid_list:
        move = mov.Move(row, col)
        G.BOARD.push_move(move)
        board_score = minimax(depth-1)
        G.BOARD.pop_move()

        # If maximizing player
        if G.BOARD.X_turn:
            if board_score > best_score:
                best_score = board_score
                best_move = move
        else:
            if board_score < best_score:
                best_score = board_score
                best_move = move
    return best_move


def minimax(depthleft):
    # Run out of depth
    if depthleft == 0:
        return evaluate_board()

    # Terminate condition
    if G.BOARD.check_win() != " ":
        return evaluate_board()
    if G.BOARD.check_draw():
        return evaluate_board()

    # Is maximizing player
    if G.BOARD.X_turn:
        best_score = -9999
        valid_list = list(G.BOARD.valid_set)
        for row,col in valid_list:
            move = mov.Move(row, col)
            G.BOARD.push_move(move)
            score = minimax(depthleft - 1)
            G.BOARD.pop_move()
            best_score = max(best_score, score)
        return best_score
    # Is minimizing player
    else:
        best_score = 9999
        valid_list = list(G.BOARD.valid_set)
        for row, col in valid_list:
            move = mov.Move(row, col)
            G.BOARD.push_move(move)
            score = minimax(depthleft - 1)
            G.BOARD.pop_move()
            best_score = min(best_score, score)
        return best_score
