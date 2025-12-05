class GameLogic:
    def __init__(self):
        self.reset()

    def reset(self):
        self.current_player = "X"
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.winner = None
        self.is_draw = False

    def on_click(self, row, col):
        if self.winner or self.is_draw:
            return False # Le jeu est déjà terminé

        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            if self.check_win(self.current_player):
                self.winner = self.current_player
            elif self.check_draw():
                self.is_draw = True
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
            return True
        return False

    def check_win(self, player):
        # Check rows
        for i in range(3):
            if all(self.board[i][j] == player for j in range(3)):
                return True
        # Check columns
        for j in range(3):
            if all(self.board[i][j] == player for i in range(3)):
                return True
        # Check diagonals
        if all(self.board[i][i] == player for i in range(3)) or \
           all(self.board[i][2 - i] == player for i in range(3)):
            return True
        return False

    def check_draw(self):
        for row in self.board:
            if "" in row:
                return False
        return True
