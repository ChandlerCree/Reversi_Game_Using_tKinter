import tkinter as tk
from view.board_view import BoardView
from view.game_view import GameView


class GUIView(tk.Frame, GameView):

    def __init__(self, parent, board):
        super().__init__(parent)
        self.board = board
        self.boardSize = board.shape[0]
        self.buttons = [None] * (self.boardSize * self.boardSize)
        self.player1Label = None
        self.player2Label = None
        self.curPlayerLabel = None
        self.move = [-1,-1]
        self.makeBoard()
        self.pack()

    def makeBoard(self):

        # main labels
        self.player1Label = tk.Label(self, text="Player 1's score is: 2", padx=10, pady=10)
        self.player1Label.grid(row=1, columnspan=3)

        self.player2Label = tk.Label(self, text="Player 2's score is: 2", padx=10, pady=10)
        self.player2Label.grid(row=self.boardSize*3, columnspan=3)

        # current player
        self.curPlayerLabel = tk.Label(self, text="The current player is Player 1")
        self.curPlayerLabel.grid(row=0, columnspan=3)

        # buttons
        for i in range(self.boardSize):  # row variable
            for j in range(self.boardSize):  # column variable
                self.buttons[i*self.boardSize+j] = tk.Button(self, width=5, height=1, command=lambda arg=(i,j): [self.set_row(arg[0]), self.set_col(arg[1])])
                self.buttons[i*self.boardSize+j].grid(row=(i + self.boardSize-1), column=j)

    def set_row(self,row):
        self.move[0] = row

    def set_col(self,col):
        self.move[1] = col

    def display_board(self):
        for i in range(self.boardSize):  # row variable
            for j in range(self.boardSize):
                if self.board[i, j] == 1:
                    self.buttons[i*self.boardSize+j]['text'] = 'X'
                elif self.board[i, j] == 2:
                    self.buttons[i*self.boardSize+j]['text'] = 'O'
                elif self.board[i, j] == 3:
                    self.buttons[i*self.boardSize+j]['text'] = '.'
                else:
                    self.buttons[i*self.boardSize+j]['text'] = ' '

    

    def display_curr_player(self, player):
        self.curPlayerLabel.config(text = f"The current Player is {player.symbol}")
        

    def display_curr_score(self, p1_score, p2_score, startingPlayer):
        self.player1Label.config(text = f"Player 1's score is: {p1_score}")
        self.player2Label.config(text = f"Player 2's score is: {p2_score}")

    def show_legal_moves(self):
        pass

    def get_move(self):
        return self.move

    def display_illegal_moves(self):
        pass

    def display_winner(self, winner):
        self.curPlayerLabel.configure(text=f"THE WINNNER IS {winner.symbol}")
