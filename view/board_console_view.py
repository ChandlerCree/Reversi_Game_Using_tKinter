<<<<<<< HEAD
from view.board_view import BoardView
from model.player import Player

=======
from email import header
from view.board_view import BoardView
from model.player import Player, player_symbol
>>>>>>> main

class BoardConsoleView(BoardView):
    def __init__(self, board):
        super().__init__(board)

    def display(self):
        board_size = len(self.board)
        header_len = board_size * 4 + 1
<<<<<<< HEAD
        print("-" * header_len)
        for row in range(board_size):
            for col in range(board_size):
                if self.board[row, col] == 0:
                    cell = " "
                elif self.board[row, col] == 1:
                    cell = "X"
                else:
                    cell = "O"

                print(f"| {cell} ", end="")
            print("|")
        print("-" * header_len)
=======
        print('-' * header_len)
        for row in range(board_size):
            for col in range(board_size):
                if self.board[row, col] == 0:
                    cell = ' '
                else: 
                    cell = player_symbol[self.board[row, col]]
                print('| {} '.format(cell), end='')
            print('|')
            print('-' * header_len)

>>>>>>> main
