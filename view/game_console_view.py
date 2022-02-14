from view.game_view import GameView
from model.player import player_symbol

class GameConsoleView(GameView):
    def __init__(self, board_view):
        super().__init__(board_view)

    def display_curr_player(self, player):
        print("Player {}: It is your turn.".format(player_symbol[player]))

    def show_legal_moves(self):
        pass

    def get_move(self):
        move = input('Enter your move (row, col): ')
        move = move.split(',')
        print(move)
        row = int(move[0]) - 1
        col = int(move[1]) - 1
        return row, col

    def display_illegal_move(self):
        print('This is an illegal move. Try Again')

    def display_winner(self, winner):
        if winner == 0:
            print('DRAW')
        else:
            print('Player {} has won the game.'.format(player_symbol[winner]))