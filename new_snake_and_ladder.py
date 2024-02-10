import tkinter as tk
from tkinter import messagebox
import random

class SnakeAndLadderGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Snake and Ladder Game")

        self.canvas = tk.Canvas(master, width=600, height=600, bg="white")
        self.canvas.grid(row=0, column=0, rowspan=2)

        self.roll_button = tk.Button(master, text="Roll Dice", command=self.roll_dice)
        self.roll_button.grid(row=0, column=1, padx=10, pady=10)

        self.reset_button = tk.Button(master, text="Reset Game", command=self.reset_game)
        self.reset_button.grid(row=1, column=1, padx=10, pady=10)

        self.players = [1, 1]
        self.current_player = 0
        self.draw_board()

    def draw_board(self):
        self.canvas.delete("all")

        for i in range(0, 600, 60):
            self.canvas.create_line(i, 0, i, 600, fill="black", width=2)
            self.canvas.create_line(0, i, 600, i, fill="black", width=2)

        for i in range(10):
            for j in range(10):
                number = i * 10 + j + 1
                x = j * 60 + 30
                y = 540 - i * 60
                self.canvas.create_text(x, y, text=str(number), font=("Arial", 12), fill="black")

        self.update_players()

    def update_players(self):
        self.canvas.delete("players")
        player_colors = ["red", "blue"]

        for idx, player in enumerate(self.players):
            row = 9 - (player - 1) // 10
            col = (player - 1) % 10
            x = col * 60 + 30
            y = row * 60 + 30
            self.canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill=player_colors[idx], tags="players")

    def roll_dice(self):
        dice_roll = random.randint(1, 6)
        messagebox.showinfo("Dice Roll", f"Player {self.current_player + 1} rolled a {dice_roll}")
        self.move_player(self.current_player, dice_roll)

        # Switch to the next player
        self.current_player = (self.current_player + 1) % 2

    def move_player(self, player_idx, steps):
        self.players[player_idx] += steps

        if self.players[player_idx] in snakes:
            messagebox.showinfo("Snake", f"Oops! Snake at {self.players[player_idx]}. You go back to {snakes[self.players[player_idx]]}")
            self.players[player_idx] = snakes[self.players[player_idx]]

        elif self.players[player_idx] in ladders:
            messagebox.showinfo("Ladder", f"Wow! Ladder at {self.players[player_idx]}. You climb up to {ladders[self.players[player_idx]]}")
            self.players[player_idx] = ladders[self.players[player_idx]]

        self.update_players()

        if self.players[player_idx] >= 100:
            messagebox.showinfo("Game Over", f"Player {player_idx + 1} wins!")

    def reset_game(self):
        self.players = [1, 1]
        self.current_player = 0
        self.draw_board()

# Define snakes and ladders positions
snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeAndLadderGame(root)
    root.mainloop()
