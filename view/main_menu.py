import tkinter as tk
from tkinter import ttk

bg_1 = "#E0FBFC"
bg_2 = "#C2DFE3"
cor_1 = "#9DB4C0"
incor_1 = "#5C6B73"
fg_1 = "#253237"


class MainMenu(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.new_game_button = tk.Button(text="New Game", height="1", width="12", command=self.new_game, bg=bg_2, fg=fg_1,
                                    font=("Calibri", 18, "bold"), activebackground=cor_1)
        self.new_game_button.pack()
        self.settings_button = tk.Button(text="Settings", height="1", width="12", command=self.new_game, bg=bg_2, fg=fg_1,
                                    font=("Calibri", 18, "bold"), activebackground=cor_1)
        self.settings_button.pack()

        self.leaderboard_button = tk.Button(text="Leaderboard", height="1", width="12", command=self.new_game, bg=bg_2, fg=fg_1,
                                       font=("Calibri", 18, "bold"), activebackground=cor_1)
        self.leaderboard_button.pack()
        self.logout_button = tk.Button(text="Login", height="1", width="12", command=self.new_game, bg=bg_2, fg=fg_1,
                                  font=("Calibri", 18, "bold"), activebackground=cor_1)
        self.logout_button.pack()

        # show the frame on the container
        self.pack()

    def new_game(self):
        button_clicked_label = tk.Label(text="button clicked", bg=bg_2, width="300", height="1",
                                        font=("Calibri", 11, "bold"), fg=fg_1, borderwidth=4, relief="groove",
                                        pady="10")
        button_clicked_label.pack()

