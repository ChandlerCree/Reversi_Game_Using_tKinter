from view.game_view import GameView
<<<<<<< HEAD
from model.player import Player


class GameConsoleView(GameView):
    def __init__(self, board_View):
        super().__init__(board_View)

    def display_curr_player(self, player):
        print(f"\nPlayer {player.symbol}: It's your turn.")
=======
from model.player import player_symbol

class GameConsoleView(GameView):
    def __init__(self, board_view):
        super().__init__(board_view)

    def display_curr_player(self, player):
        print("Player {}: It is your turn.".format(player_symbol[player]))
>>>>>>> main

    def show_legal_moves(self):
        pass

    def get_move(self):
<<<<<<< HEAD
        move = input("Enter your move (row, col): ")
        move = move.split(",")
=======
        move = input('Enter your move (row, col): ')
        move = move.split(',')
        print(move)
>>>>>>> main
        row = int(move[0]) - 1
        col = int(move[1]) - 1
        return row, col

<<<<<<< HEAD
    def display_illegal_moves(self):
        print("This move is illegal. Try again.")

    def display_winner(self, winner):
        if winner == 0:
            print("DRAW")
        else:
            print(f"Player {winner.symbol} has won the game")
=======
    def display_illegal_move(self):
        print('This is an illegal move. Try Again')

    def display_winner(self, winner):
        if winner == 0:
            print('DRAW')
        else:
            print('Player {} has won the game.'.format(player_symbol[winner]))
>>>>>>> main
