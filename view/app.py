import tkinter as tk
from view.leaderboard_tkinter_view import LeaderboardView
from view.settings_tkinter_view import SettingsView
from model.game import Game
from controller.gameManager import GameManager
from view.board_console_view import BoardConsoleView
from controller.connector_controller import ConnectorController

from view.login_view import LoginView
from view.gui_game_view import GUIView

bg_1 = "#E0FBFC"
bg_2 = "#C2DFE3"
cor_1 = "#9DB4C0"
incor_1 = "#5C6B73"
fg_1 = "#253237"


class App(tk.Tk):
    board_size = "6"
    p1 = '#000000'
    p2 = '#FFFFFF'
    user_name = "Guest"
    user_elo = 1500
    user_info = "Welcome {}!\nCurrent Elo: {}".format(user_name, str(user_elo))


    def __init__(self):
        super().__init__()

        self.title('Reversi')
        self.geometry('300x410')
        self.configure(bg=bg_1)
        self.resizable(False, False)

        # label
        title_label = tk.Label(text="REVERSI", bg=bg_2, width="300", height="1", font=("Calibri", 24, "bold"), fg=fg_1,
                               borderwidth=4, relief="groove", pady="10")
        title_label.pack()

        self.frame = tk.Frame(self)
        self.frame.configure(bg=bg_1)

        self.username_label = tk.Label(self.frame, text=self.user_info, height="2", font=("Calibri", 12), 
                                            bg=bg_1, fg=fg_1)
        self.username_label.pack(pady=8)

        self.new_game_button = tk.Button(self.frame, text="New Game", height="1", width="12", command=self.new_game,
                                         bg=bg_2, fg=fg_1,
                                         font=("Calibri", 18, "bold"), activebackground=cor_1)
        self.new_game_button.pack(pady=8)

        self.settings_button = tk.Button(self.frame, text="Settings", height="1", width="12",
                                         command=self.open_settings, bg=bg_2, fg=fg_1,
                                         font=("Calibri", 18, "bold"), activebackground=cor_1)
        self.settings_button.pack(pady=8)

        self.leaderboard_button = tk.Button(self.frame, text="Leaderboard", height="1", width="12",
                                            command=self.open_leaderboard, bg=bg_2, fg=fg_1,
                                            font=("Calibri", 18, "bold"), activebackground=cor_1)
        self.leaderboard_button.pack(pady=8)
        
        self.login_button = tk.Button(self.frame, text="Login", height="1", width="12", command=self.open_login,
                                       bg=bg_2, fg=fg_1,
                                       font=("Calibri", 18, "bold"), activebackground=cor_1)
        self.login_button.pack(pady=8)

        # show the frame on the container
        self.frame.pack()

    def new_game(self):
        game = Game(size=int(self.board_size))  # create the game

        game_win = GUIView(self.master, game.board)
        game_win.p1 = self.p1
        game_win.p2 = self.p2
        controller = GameManager(game, game_win)
        controller.run_game()
        game_win.focus_force()
        self.withdraw()

    def open_settings(self):
        settings_win = SettingsView(self.master)
        settings_win.focus_force()
        self.withdraw()

    def open_leaderboard(self):
        leaderboard_win = LeaderboardView(self.master)
        leaderboard_win.focus_force()
        self.withdraw()

    def open_login(self):
        login_controller = ConnectorController()
        self.my_conn = login_controller.connect_mysql()
        login_win = LoginView(self.master, self.my_conn)
        login_win.focus_force()
        self.withdraw()
