import tkinter as tk
from tkinter import ttk
from leaderboard_tkinter_view import LeaderboardView
from settings_tkinter_view import SettingsView
from view.login_view import LoginView
from gui_game_view import GUIView

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
        self.settings_button = tk.Button(text="Settings", height="1", width="12", command=self.open_settings, bg=bg_2, fg=fg_1,
                                    font=("Calibri", 18, "bold"), activebackground=cor_1)
        self.settings_button.pack()

        self.leaderboard_button = tk.Button(text="Leaderboard", height="1", width="12", command=self.open_leaderboard, bg=bg_2, fg=fg_1,
                                       font=("Calibri", 18, "bold"), activebackground=cor_1)
        self.leaderboard_button.pack()
        self.logout_button = tk.Button(text="Logout", height="1", width="12", command=self.open_login, bg=bg_2, fg=fg_1,
                                  font=("Calibri", 18, "bold"), activebackground=cor_1)
        self.logout_button.pack()

        # show the frame on the container
        self.pack()

    def new_game(self):
        game_win = GUIView(self)
        game_win.focus_force()
        self.withdraw()

    def open_settings(self):
        settings_win = SettingsView(self)
        settings_win.focus_force()
        self.withdraw()

    def open_leaderboard(self):
        leaderboard_win = LeaderboardView(self)
        leaderboard_win.focus_force()
        self.withdraw()

    def open_login(self):
        login_win = LoginView(self)
        login_win.focus_force()
        self.withdraw()


