from view.board_view import BoardView
from model.player import Player


class BoardConsoleView(BoardView):
    def __init__(self, board):
        super().__init__(board)

    def display(self):
        board_size = len(self.board)
        header_len = board_size * 4 + 1
        #print('    1   2   3   4   5   6   7   8  ')
        print('\n ', end='')
        for x in range(board_size):
            print('   {}'.format(x + 1), end='')
        print("\n  " +"-" * header_len)
        x = 0
        for row in range(board_size):
            x += 1
            print(x, end=' ')
            for col in range(board_size):
                if self.board[row, col] == 0:
                    cell = " "
                elif self.board[row, col] == 1:
                    cell = "X"
                elif self.board[row, col] == 2:
                    cell = "O"
                else:
                    cell = "."

                print(f"| {cell} ", end="")
            print("|")
            print('  ', end='')
            print("-" * header_len)
        print('  ', end='')
