"""Simple Rock-Paper-Scissors GUI using Tkinter.

Usage:
    python "c:/Users/dsa90/OneDrive/Área de Trabalho/rock_paper_scissors_gui.py"

Controls:
    - Click the Rock / Paper / Scissors buttons to play a round.
    - Press 'r', 'p', 's' on the keyboard (lower or upper case) as shortcuts.
    - Press 'q' or use the Quit button to exit.

This file is standalone and reimplements minimal game logic so there's no import
dependency on the CLI script.
"""
import random
import tkinter as tk
from tkinter import ttk

OPTIONS = ["rock", "paper", "scissors"]


def get_computer_choice():
    return random.choice(OPTIONS)


def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif ((player == "rock" and computer == "scissors") or
          (player == "paper" and computer == "rock") or
          (player == "scissors" and computer == "paper")):
        return "You win!"
    else:
        return "Computer wins!"


class RPSApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Rock Paper Scissors")
        self.player_score = 0
        self.computer_score = 0

        main = ttk.Frame(root, padding=12)
        main.grid(row=0, column=0, sticky="nsew")

        # Status and score
        self.status_var = tk.StringVar(value="Make your choice")
        self.score_var = tk.StringVar(value=self._score_text())
        self.computer_var = tk.StringVar(value="Computer chose: -")

        status_label = ttk.Label(main, textvariable=self.status_var, font=(None, 12))
        status_label.grid(row=0, column=0, columnspan=3, pady=(0, 8))

        score_label = ttk.Label(main, textvariable=self.score_var)
        score_label.grid(row=1, column=0, columnspan=3, pady=(0, 8))

        computer_label = ttk.Label(main, textvariable=self.computer_var)
        computer_label.grid(row=2, column=0, columnspan=3, pady=(0, 12))

        # Buttons
        rock_btn = ttk.Button(main, text="Rock", command=lambda: self.on_choice("rock"))
        paper_btn = ttk.Button(main, text="Paper", command=lambda: self.on_choice("paper"))
        scissors_btn = ttk.Button(main, text="Scissors", command=lambda: self.on_choice("scissors"))

        rock_btn.grid(row=3, column=0, ipadx=8, padx=4)
        paper_btn.grid(row=3, column=1, ipadx=8, padx=4)
        scissors_btn.grid(row=3, column=2, ipadx=8, padx=4)

        quit_btn = ttk.Button(main, text="Quit", command=self.on_quit)
        quit_btn.grid(row=4, column=0, columnspan=3, pady=(12, 0))

        # Keyboard bindings for r/p/s/q (lower or upper)
        root.bind("r", lambda e: self.on_choice("rock"))
        root.bind("R", lambda e: self.on_choice("rock"))
        root.bind("p", lambda e: self.on_choice("paper"))
        root.bind("P", lambda e: self.on_choice("paper"))
        root.bind("s", lambda e: self.on_choice("scissors"))
        root.bind("S", lambda e: self.on_choice("scissors"))
        root.bind("q", lambda e: self.on_quit())
        root.bind("Q", lambda e: self.on_quit())

        # Make window resize gracefully
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

    def _score_text(self) -> str:
        return f"Score - You: {self.player_score}   Computer: {self.computer_score}"

    def on_choice(self, player_choice: str):
        computer_choice = get_computer_choice()
        self.computer_var.set(f"Computer chose: {computer_choice}")
        result = determine_winner(player_choice, computer_choice)
        self.status_var.set(result)
        if result == "You win!":
            self.player_score += 1
        elif result == "Computer wins!":
            self.computer_score += 1
        self.score_var.set(self._score_text())

    def on_quit(self):
        # Optionally show final score before exit
        final = f"Final score - You: {self.player_score}   Computer: {self.computer_score}"
        print(final)
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = RPSApp(root)
    root.mainloop()
