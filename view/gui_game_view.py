import tkinter as tk
from view.board_view import BoardView
from view.game_view import GameView
from database.database_eloupdate import DatabaseEloupdate
bg_1 = "#E0FBFC"
bg_2 = "#C2DFE3"
cor_1 = "#9DB4C0"
incor_1 = "#5C6B73"
fg_1 = "#253237"
avail_move = '#b0b0b0'
bc_grnd = '#404040'


class GUIView(tk.Toplevel, GameView):
    #Player color/ name
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
        self.makeBoard()

    def makeBoard(self):
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
        self.move[0] = row

    def set_col(self, col):
        self.move[1] = col

    def display_board(self):
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
        if player.symbol == 'X':
            self.curPlayerLabel.config(text="The current Player is {}".format(self.p1))
        elif player.symbol == 'O':
            self.curPlayerLabel.config(text="The current Player is {}".format(self.p2))
        else:
            pass

    def display_curr_score(self, p1_score, p2_score, startingPlayer):
        self.player1Label.config(text="{}'s score is: {}".format(self.p1, p1_score))
        self.player2Label.config(text="{}'s score is: {}".format(self.p2, p2_score))

    def show_legal_moves(self):
        pass

    def get_move(self):
        self.update()
        return self.move

    def display_illegal_moves(self):
        pass

    def display_winner(self, winner):
        print(self.p1_username)
        print(self.p2_username)
        if winner.symbol == 'X':
            self.curPlayerLabel.configure(text="THE WINNER IS {}".format(self.p1))
            self.currgame.execute_query(self.p1_username)
        elif winner.symbol == 'O':
            self.curPlayerLabel.configure(text="THE WINNER IS {}".format(self.p2))
            self.currgame.execute_query(self.p2_username)
        else:
            pass

    def open_main(self):
        self.destroy()
        # self.master.deiconify()
