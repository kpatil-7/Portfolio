# This file describe the board class
class Board:
    def __init__(self):
        self.matrix = [[" "] * 3 for i in range(0, 3)]
        self.valid_set = set([(row, col) for row in range(0, 3) for col in range(0, 3)])
        self.move_mem = []
        self.X_turn = True # Default X play first

    def __str__(self):
        m = self.matrix
        to_return = m[0][0] + "|" + m[0][1] + "|" + m[0][2] + "\n"
        to_return += "-----" + "\n"
        to_return += m[1][0] + "|" + m[1][1] + "|" + m[1][2] + "\n"
        to_return += "-----" + "\n"
        to_return += m[2][0] + "|" + m[2][1] + "|" + m[2][2] + "\n"
        return to_return

    def push_move(self, move):
        # Remove position from valid list
        position = (move.row, move.col)
        self.valid_set.remove(position)
        # Update the board
        player = "X" if self.X_turn else "O"
        self.matrix[move.row][move.col] = player
        # Update the turn
        self.X_turn = not self.X_turn
        # Update the move memory
        self.move_mem.append(move)

    def pop_move(self):
        # Pop from the move memory
        move = self.move_mem.pop()
        # Update the board
        self.matrix[move.row][move.col] = " "
        # Update the turn
        self.X_turn = not self.X_turn
        # Add position back to valid list
        position = (move.row, move.col)
        self.valid_set.add(position)

    def check_win(self):
        m = self.matrix
        win_X = ("X", "X", "X")
        win_O = ("O", "O", "O")
        # Check for horizontal files
        for row in range(0,3):
            to_test = tuple(m[row])
            if to_test == win_X:
                return "X"
            if to_test == win_O:
                return "O"
        # Check for vertical files
        for col in range(0,3):
            to_test = tuple([m[0][col], m[1][col], m[2][col]])
            if to_test == win_X:
                return "X"
            if to_test == win_O:
                return "O"
        # Check for diagonal files
        first_dia = tuple([m[0][0], m[1][1], m[2][2]])
        if first_dia == win_X:
            return "X"
        if first_dia == win_O:
            return "O"
        second_dia = tuple([m[0][2], m[1][1], m[2][0]])
        if second_dia == win_X:
            return "X"
        if second_dia == win_O:
            return "O"
        # No one wins
        return " "

    def check_draw(self):
        return len(self.valid_set) == 0

    def check_valid(self, row, col):
        return (row, col) in self.valid_set
