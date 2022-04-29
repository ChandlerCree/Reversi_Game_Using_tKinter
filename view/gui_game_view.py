import tkinter as tk
from view.board_view import BoardView
from view.game_view import GameView
from controller.database.database_eloupdate import DatabaseEloupdate
from controller.database.database_login import DatabaseLogin

bg_1 = "#E0FBFC"
bg_2 = "#C2DFE3"
cor_1 = "#9DB4C0"
incor_1 = "#5C6B73"
fg_1 = "#253237"
avail_move = '#b0b0b0'
bc_grnd = '#404040'


class GUIView(tk.Toplevel, GameView):
    """
    This class is the view of the game and the board in tkinter
    """
    # Player color/ name
    p1 = '#000000'
    p2 = '#FFFFFF'
    p1_username = 'guest'
    p2_username = 'guest'

    def __init__(self, parent, board, p1_user, p2_user):
        super().__init__(parent)

        self.p1_username = p1_user
        self.p2_username = p2_user

        self.title('Reversi')
        # self.geometry('300x350')
        self.configure(bg=bg_1)
        self.frame = tk.Frame(self)
        self.resizable(False, False)

        self.board = board
        self.boardSize = board.shape[0]
        self.buttons = [None] * (self.boardSize * self.boardSize)
        self.player1Label = None
        self.player2Label = None
        self.curPlayerLabel = None
        self.main_button = None
        self.parent = parent
        self.move = [-1, -1]
        self.currgame = DatabaseEloupdate(self.p1_username, self.p2_username)
        self.currgame.connect_to_database()
        self.make_board()

    def make_board(self):
        """
        This function creates a frame with a grid layout. The grid is filled with buttons equal to the board size
        :param
        :return
        """
        # main labels
        self.game_frame = tk.Frame(self)
        self.reversi_label = tk.Label(self.frame, text="REVERSI", bg=bg_2, height="1", font=("Calibri", 24, "bold"),
                                      fg=fg_1, borderwidth=4, relief="groove", pady="10")
        self.reversi_label.grid(row=0, column=0, sticky='ew')
        self.main_button = tk.Button(self.game_frame, text='Main Menu', command=self.open_main, bg=bg_2, fg=fg_1,
                                     activebackground=cor_1, font=("Calibri", 12, "bold"))
        self.main_button.grid(row=self.boardSize * 3 + 1, columnspan=self.boardSize, sticky='ew')
        self.player1Label = tk.Label(self.game_frame, text="Player 1's score is: 2", padx=10, pady=10,
                                     font=("Calibri", 12, "bold"), bg=bg_1, fg=fg_1)
        self.player1Label.grid(row=1, columnspan=self.boardSize, sticky='ew')

        self.player2Label = tk.Label(self.game_frame, text="Player 2's score is: 2", padx=10, pady=10,
                                     font=("Calibri", 12, "bold"), bg=bg_1, fg=fg_1)
        self.player2Label.grid(row=self.boardSize * 3, columnspan=self.boardSize, sticky='ew')

        # current player
        self.curPlayerLabel = tk.Label(self.game_frame, text="The current player is Player 1",
                                       font=("Calibri", 12, "bold"),
                                       bg=bg_1, fg=fg_1)
        self.curPlayerLabel.grid(row=0, columnspan=self.boardSize, sticky='ew')
        self.frame.grid(row=0, column=0)
        self.game_frame.grid(row=1, column=0)

        # buttons
        for i in range(self.boardSize):  # row variable
            for j in range(self.boardSize):  # column variable
                self.buttons[i * self.boardSize + j] = tk.Button(self.game_frame, width=5, height=1,
                                                                 command=lambda arg=(i, j): [self.set_row(arg[0]),
                                                                                             self.set_col(arg[1])],
                                                                 font=("Calibri", 12, "bold"), bg=bg_2, fg=fg_1)
                self.buttons[i * self.boardSize + j].grid(row=(i + self.boardSize - 1), column=j)

    def set_row(self, row):
        """
        This function set the row value of the move equal to the row of the button where the user clicked
        :param row - the row value
        :return
        """
        self.move[0] = row

    def set_col(self, col):
        """
        This function set the column value of the move equal to the column of the button where the user clicked
        :param col - the column value
        :return
        """
        self.move[1] = col

    def display_board(self):
        """
        This function is adds changes the buttons in the grid to match the board model object
        :param
        :return
        """
        for i in range(self.boardSize):  # row variable
            for j in range(self.boardSize):
                if self.board[i, j] == 1:
                    self.buttons[i * self.boardSize + j]['bg'] = self.p1
                elif self.board[i, j] == 2:
                    self.buttons[i * self.boardSize + j]['bg'] = self.p2
                elif self.board[i, j] == 3:
                    self.buttons[i * self.boardSize + j]['bg'] = avail_move
                else:
                    self.buttons[i * self.boardSize + j]['bg'] = bc_grnd

    def display_curr_player(self, player):
        """
        This function changes the label at the top of the game view to display who's turn it is
        :param player - the name of who is going next
        :return
        """
        if player.symbol == 'X':
            self.curPlayerLabel.config(text="The current Player is {}".format(self.p1))
        elif player.symbol == 'O':
            self.curPlayerLabel.config(text="The current Player is {}".format(self.p2))
        else:
            pass

    def display_curr_score(self, p1_score, p2_score, startingPlayer):
        """
        This function is not used in the tkinter gui but was part of the initial game view design for console
        :param p1_score - player 1's score, p2_score - player 2's score, starting player - the player that goes first
        :return
        """

        # Does this function need the starting Player parameter ??????????????????????????????????????????????????????
        self.player1Label.config(text="{}'s score is: {}".format(self.p1, p1_score))
        self.player2Label.config(text="{}'s score is: {}".format(self.p2, p2_score))

    def show_legal_moves(self):
        """
        This function is not used in the tkinter gui but was part of the initial game view design for console
        :param
        :return
        """
        pass

    def get_move(self):
        """
        This function gets the move from the UI where the user clicked and returns it for the model's use
        :param
        :return self.move
        """
        self.update()
        return self.move

    def display_illegal_moves(self):
        """
        This function is not used in the tkinter gui but was part of the initial game view design for console
        :param
        :return
        """
        pass

    def display_winner(self, winner):
        """
        This function updates the elo of the players in the game and displays the winner at the top of the game
        window
        :param winner - player object that won the game
        :return
        """
        print(self.p1_username)
        print(self.p2_username)
        # DOES THIS UPDATE THE LOSER'S ELO TOO??????????????????????????????????????????????????????
        if winner.symbol == 'X':
            self.curPlayerLabel.configure(text="THE WINNER IS {}".format(self.p1))
            self.currgame.execute_query(self.p1_username)
        elif winner.symbol == 'O':
            self.curPlayerLabel.configure(text="THE WINNER IS {}".format(self.p2))
            self.currgame.execute_query(self.p2_username)
        else:
            pass

    def open_main(self):
        """
        This function destroys the current window and reopens the main menu. Additionally, it updates the label at the
        top of the main menu.
        :param
        :return
        """
        login = DatabaseLogin(self.master.username_login_tup, self.master.password_log)
        login.connect_to_database()

        user_temp, self.master.logged_elo, self.master.matches_played, pass_temp = login.execute_query()

        self.master.change_username_label()

        self.destroy()
        self.master.deiconify()
