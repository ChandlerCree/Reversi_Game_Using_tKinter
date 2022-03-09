import tkinter as tk
from view.board_view import BoardView
from view.game_view import GameView

bg_1 = "#E0FBFC"
bg_2 = "#C2DFE3"
cor_1 = "#9DB4C0"
incor_1 = "#5C6B73"
fg_1 = "#253237"
avail_move = '#f5ef42'
bc_grnd = '#7d7d7d'


class GUIView(tk.Toplevel, GameView):
    p1 = '#000000'
    p2 = '#FFFFFF'
    def __init__(self, parent, board):
        super().__init__(parent)
        self.title('Reversi')
        self.geometry('300x350')
        self.configure(bg=bg_1)
        self.frame = tk.Frame(self)

        self.board = board
        self.boardSize = board.shape[0]
        self.buttons = [None] * (self.boardSize * self.boardSize)
        self.player1Label = None
        self.player2Label = None
        self.curPlayerLabel = None
        self.main_button = None
        self.parent = parent
        self.move = [-1, -1]
        self.makeBoard()

    def makeBoard(self):
        # main labels
        # self.reversi_label = tk.Label(text="  REVERSI  ", bg=bg_2, height="1" , font=("Calibri", 24, "bold"), fg=fg_1, borderwidth=4, relief="groove", pady="10")
        # self.reversi_label.grid(row=0, columnspan=self.boardSize, sticky='ew')
        self.main_button = tk.Button(self, text='Main Menu', command=self.open_main)
        self.main_button.grid(row=self.boardSize * 3 + 1, columnspan=self.boardSize, sticky='ew')
        self.player1Label = tk.Label(self, text="Player 1's score is: 2", padx=10, pady=10,
                                     font=("Calibri", 12, "bold"), bg=bg_1, fg=fg_1)
        self.player1Label.grid(row=1, columnspan=self.boardSize, sticky='ew')

        self.player2Label = tk.Label(self, text="Player 2's score is: 2", padx=10, pady=10,
                                     font=("Calibri", 12, "bold"), bg=bg_1, fg=fg_1)
        self.player2Label.grid(row=self.boardSize * 3, columnspan=self.boardSize, sticky='ew')

        # current player
        self.curPlayerLabel = tk.Label(self, text="The current player is Player 1", font=("Calibri", 12, "bold"),
                                       bg=bg_1, fg=fg_1)
        self.curPlayerLabel.grid(row=0, columnspan=self.boardSize, sticky='ew')

        # buttons
        for i in range(self.boardSize):  # row variable
            for j in range(self.boardSize):  # column variable
                self.buttons[i * self.boardSize + j] = tk.Button(self, width=5, height=1,
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
                    self.buttons[i * self.boardSize + j]['bg'] = p1
                elif self.board[i, j] == 2:
                    self.buttons[i * self.boardSize + j]['bg'] = p2
                elif self.board[i, j] == 3:
                    self.buttons[i * self.boardSize + j]['bg'] = avail_move
                else:
                    self.buttons[i * self.boardSize + j]['bg'] = bc_grnd

    def display_curr_player(self, player):
        self.curPlayerLabel.config(text=f"The current Player is {player.symbol}")

    def display_curr_score(self, p1_score, p2_score, startingPlayer):
        self.player1Label.config(text=f"Player 1's score is: {p1_score}")
        self.player2Label.config(text=f"Player 2's score is: {p2_score}")

    def show_legal_moves(self):
        pass

    def get_move(self):
        self.update()
        return self.move

    def display_illegal_moves(self):
        pass

    def display_winner(self, winner):
        self.curPlayerLabel.configure(text=f"THE WINNNER IS {winner.symbol}")

    def open_main(self):
        self.destroy()
        self.master.deiconify()
