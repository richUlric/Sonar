import tkinter as tk
from tkinter import messagebox
from game_logic import GameLogic

class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.game_logic = GameLogic()
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_widgets()

    def create_widgets(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(
                    self.root,
                    text="",
                    font=('normal', 40),
                    width=5,
                    height=2,
                    command=lambda i=i, j=j: self.on_click(i, j)
                )
                self.buttons[i][j].grid(row=i, column=j)

    def on_click(self, row, col):
        if self.game_logic.on_click(row, col):
            self.buttons[row][col].config(text=self.game_logic.board[row][col])
            
            if self.game_logic.winner:
                messagebox.showinfo("Tic Tac Toe", f"Player {self.game_logic.winner} wins!")
                self.reset_game()
            elif self.game_logic.is_draw:
                messagebox.showinfo("Tic Tac Toe", "It's a draw!")
                self.reset_game()

    def reset_game(self):
        self.game_logic.reset()
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToeGUI(root)
    root.mainloop()
