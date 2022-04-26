from re import I
import tkinter as tk
from reversi_client import ReversiClient

from model.eligible_checker import EligibleChecker
from view.leaderboard_tkinter_view import LeaderboardView
from view.settings_tkinter_view import SettingsView

from model.game import Game
from model.player import Player
from model.human_player import HumanPlayer
from model.ai_player import AIPlayer

from controller.game_manager import GameManager
from view.board_console_view import BoardConsoleView

from view.login_view import LoginView
from view.gui_game_view import GUIView
from view.account_settings_view import AccountSettingsView
from view.matchmaker_view import MatchmakerView
import threading

from model.user import User

from model.eligible_checker import EligibleChecker

bg_1 = "#E0FBFC"
bg_2 = "#C2DFE3"
cor_1 = "#9DB4C0"
incor_1 = "#5C6B73"
fg_1 = "#253237"


class App(tk.Tk):
    board_size = "6"
    ai_difficulty = 2
    # ai_difficulty
    p1 = '#000000'
    p2 = '#FFFFFF'
    default_username = "Guest"
    default_elo = 0
    logged_user = ""
    logged_elo = 0
    matches_played = 0
    ng_btn_stat = "disabled"
    guest_elo = 1500
    guest_username = "Guest"

    user_logged_in = User()

    def __init__(self):
        super().__init__()

        self.title('Reversi')
        # self.geometry('300x410')
        self.configure(bg=bg_1)
        self.resizable(False, False)

        # label
        title_label = tk.Label(text="REVERSI", bg=bg_2, width="24", height="1", font=("Calibri", 24, "bold"), fg=fg_1,
                               borderwidth=4, relief="groove", pady="10")
        title_label.pack()

        self.frame = tk.Frame(self)
        self.frame.configure(bg=bg_1)

        self.username_label = tk.Label(self.frame, text="Welcome {}!\nCurrent Elo: {}\nMatches Played: {}".format(
            self.default_username, str(self.default_elo), str(self.matches_played)),
                                       height="3", font=("Calibri", 12, "italic"), bg=bg_1, fg=fg_1)
        self.username_label.grid(row=0, column=0, columnspan=2, padx=4, pady=4)

        self.new_game_button = tk.Button(self.frame, text="Local Game", height="1", width="14", command=self.new_game,
                                         bg=bg_2, fg=fg_1, font=("Calibri", 18, "bold"), activebackground=cor_1,
                                         state="disabled")
        self.new_game_button.grid(row=1, column=0, padx=(8, 4), pady=4)

        self.new_ai_game_button = tk.Button(self.frame, text="AI Game", height="1", width="14",
                                            command=self.new_ai_game,
                                            bg=bg_2, fg=fg_1, font=("Calibri", 18, "bold"), activebackground=cor_1,
                                            state="disabled")
        self.new_ai_game_button.grid(row=2, column=0, padx=(8, 4), pady=4)

        self.new_online_game_button = tk.Button(self.frame, text="Online Game", height="1", width="14",
                                                command=self.open_matchmake,
                                                bg=bg_2, fg=fg_1, font=("Calibri", 18, "bold"), activebackground=cor_1,
                                                state="disabled")
        self.new_online_game_button.grid(row=3, column=0, padx=(8, 4), pady=4)

        self.settings_button = tk.Button(self.frame, text="Game Settings", height="1", width="14",
                                         command=self.open_settings, bg=bg_2, fg=fg_1,
                                         font=("Calibri", 18, "bold"), activebackground=cor_1)
        self.settings_button.grid(row=1, column=1, padx=(4, 8), pady=4)

        self.account_settings_button = tk.Button(self.frame, text="Account Settings", height="1", width="14",
                                                 command=self.open_account_settings, bg=bg_2, fg=fg_1,
                                                 font=("Calibri", 18, "bold"), activebackground=cor_1, state='disabled')
        self.account_settings_button.grid(row=2, column=1, padx=(4, 8), pady=4)

        self.leaderboard_button = tk.Button(self.frame, text="Leaderboard", height="1", width="14",
                                            command=self.open_leaderboard, bg=bg_2, fg=fg_1,
                                            font=("Calibri", 18, "bold"), activebackground=cor_1)
        self.leaderboard_button.grid(row=3, column=1, padx=(4, 8), pady=4)

        self.login_button = tk.Button(self.frame, text="Login", height="1", width="14", command=self.open_login,
                                      bg=bg_2, fg=fg_1, font=("Calibri", 18, "bold"), activebackground=cor_1)
        self.login_button.grid(row=4, column=0, columnspan=2, padx=4, pady=(4, 12))

        # show the frame on the container
        self.frame.pack()

    def change_username_label(self):
        self.username_label.configure(
            text="Welcome {}!\nCurrent Elo: {}\nMatches Played: {}".format(self.logged_user, self.logged_elo,
                                                                           self.matches_played))
        if self.logged_user != "Guest":
            self.login_button.configure(text="Logout")
        else:
            self.login_button.configure(text="Login")

    def change_newgame_state(self):
        eligible = EligibleChecker()
        is_user_eligible = eligible.is_elegible_for_ranked(self.user_logged_in)

        if is_user_eligible:
            self.new_ai_game_button.configure(state="normal")

        self.new_game_button.configure(state="normal")
        self.new_online_game_button.configure(state="normal")
        # self.new_ai_game_button.configure(stat="normal")

    def change_account_info_state(self):
        self.account_settings_button.configure(state="normal")

    def new_game(self):
        player1 = HumanPlayer(1)
        player2 = HumanPlayer(2)
        game = Game(size=int(self.board_size), player1=player1, player2=player2)  # create the game

        game_win = GUIView(self.master, game.board, self.logged_user, "guest")
        game_win.p1 = self.p1
        game_win.p2 = self.p2

        controller = GameManager(game, game_win)
        player1.controller = controller
        player2.controller = controller
        self.open_thread(controller.run_game)
        game_win.focus_force()

    def new_ai_game(self):
        player1 = HumanPlayer(1)
        player2 = AIPlayer(2, self.ai_difficulty)
        game = Game(size=int(self.board_size), player1=player1, player2=player2)  # create the game

        game_win = GUIView(self.master, game.board, self.logged_user, self.ai_difficulty)
        game_win.p1 = self.p1
        game_win.p2 = self.p2

        controller = GameManager(game, game_win)
        player1.controller = controller
        player2.controller = controller
        self.open_thread(controller.run_game)
        game_win.focus_force()

    def open_settings(self):
        matches = self.user_logged_in.get_total_matches()
        settings_win = SettingsView(self.master)
        settings_win.focus_force()
        self.withdraw()

    def open_account_settings(self):
        account_settings_win = AccountSettingsView(self.master)
        account_settings_win.focus_force()
        self.withdraw()

    def open_leaderboard(self):
        leaderboard_win = LeaderboardView(self.master)
        leaderboard_win.focus_force()
        self.withdraw()

    def open_login(self):
        login_win = LoginView(self.master)
        login_win.focus_force()
        self.withdraw()

    def open_matchmake(self):
        client = ReversiClient()
        client.start_client()
        matchmake_win = MatchmakerView(self.master)
        matchmake_win.focus_force()
        self.withdraw()

    def open_online_game(self):
        player1 = HumanPlayer(1)
        player2 = AIPlayer(2, self.ai_difficulty)
        game = Game(size=int(self.board_size), player1=player1, player2=player2)  # create the game

        game_win = GUIView(self.master, game.board, self.logged_user, "guest")
        game_win.p1 = self.p1
        game_win.p2 = self.p2

        controller = GameManager(game, game_win)
        player1.controller = controller
        player2.controller = controller
        self.open_thread(controller.run_game)
        game_win.focus_force()

    def open_thread(self, function):
        thread = threading.Thread(target=function)
        thread.start()
