import tkinter as tk
from tkinter import messagebox
import math

HUMAN = 'X'
AI = 'O'
EMPTY = ' '

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe AI Game")
        self.board = [[EMPTY for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_board()
        self.current_player = HUMAN

    def create_board(self):
        for i in range(3):
            for j in range(3):
                btn = tk.Button(self.root, text='', font=('Arial', 32), width=5, height=2,
                                command=lambda row=i, col=j: self.on_click(row, col))
                btn.grid(row=i, column=j)
                self.buttons[i][j] = btn

    def on_click(self, row, col):
        if self.board[row][col] == EMPTY and self.current_player == HUMAN:
            self.make_move(row, col, HUMAN)
            if self.check_game_over():
                return
            self.root.after(500, self.ai_move)

    def make_move(self, row, col, player):
        self.board[row][col] = player
        self.buttons[row][col]['text'] = player
        self.buttons[row][col]['state'] = 'disabled'

    def ai_move(self):
        row, col = self.find_best_move()
        self.make_move(row, col, AI)
        self.check_game_over()

    def check_game_over(self):
        result = self.evaluate()
        if result == 10:
            messagebox.showinfo("Result", "AI wins!")
            self.reset_game()
            return True
        elif result == -10:
            messagebox.showinfo("Result", "You win!")
            self.reset_game()
            return True
        elif not self.is_moves_left():
            messagebox.showinfo("Result", "It's a draw!")
            self.reset_game()
            return True
        return False

    def is_moves_left(self):
        return any(cell == EMPTY for row in self.board for cell in row)

    def evaluate(self):
        # Rows and columns
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != EMPTY:
                return 10 if self.board[i][0] == AI else -10
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != EMPTY:
                return 10 if self.board[0][i] == AI else -10

        # Diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != EMPTY:
            return 10 if self.board[0][0] == AI else -10
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != EMPTY:
            return 10 if self.board[0][2] == AI else -10

        return 0

    def minimax(self, depth, is_max, alpha, beta):
        score = self.evaluate()
        if score == 10 or score == -10:
            return score
        if not self.is_moves_left():
            return 0

        if is_max:
            best = -math.inf
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == EMPTY:
                        self.board[i][j] = AI
                        best = max(best, self.minimax(depth + 1, False, alpha, beta))
                        self.board[i][j] = EMPTY
                        alpha = max(alpha, best)
                        if beta <= alpha:
                            break
            return best
        else:
            best = math.inf
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == EMPTY:
                        self.board[i][j] = HUMAN
                        best = min(best, self.minimax(depth + 1, True, alpha, beta))
                        self.board[i][j] = EMPTY
                        beta = min(beta, best)
                        if beta <= alpha:
                            break
            return best

    def find_best_move(self):
        best_val = -math.inf
        best_move = (-1, -1)

        for i in range(3):
            for j in range(3):
                if self.board[i][j] == EMPTY:
                    self.board[i][j] = AI
                    move_val = self.minimax(0, False, -math.inf, math.inf)
                    self.board[i][j] = EMPTY
                    if move_val > best_val:
                        best_val = move_val
                        best_move = (i, j)
        return best_move

    def reset_game(self):
        self.board = [[EMPTY for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]['text'] = ''
                self.buttons[i][j]['state'] = 'normal'
        self.current_player = HUMAN

# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
