import tkinter as tk
from tkinter import ttk
from controller.connector_controller import ConnectorController
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

        self.spacer_1 = tk.Label(text="", height="1", fg="fg_1")
        self.spacer_1.pack()

        self.new_game_button = tk.Button(text="New Game", height="1", width="12", command=self.new_game, bg=bg_2, fg=fg_1,
                                    font=("Calibri", 18, "bold"), activebackground=cor_1)
        self.new_game_button.pack()
        #self.spacer_1 = tk.Label(text="", height="1", fg="fg_1")
        self.spacer_1.pack()
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
        connection = ConnectorController()
        my_connect = connection.connect_mysql()
        login_win = LoginView(self, my_connect)
        login_win.focus_force()
        self.withdraw()


