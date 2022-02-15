from view.game_view import GameView
from model.player import Player


class GameConsoleView(GameView):
    def __init__(self, board_View):
        super().__init__(board_View)

    def display_curr_player(self, player):
        print(f"\nPlayer {player.symbol}: It's your turn.")

    def show_legal_moves(self):
        pass

    def get_move(self):
        move = input("Enter your move (row, col): ")
        move = move.split(",")
        row = int(move[0]) - 1
        col = int(move[1]) - 1
        return row, col

    def display_illegal_moves(self):
        print("This move is illegal. Try again.")

    def display_winner(self, winner):
        if winner.x == -1:
            print("DRAW")
        else:
            print(f"Player {winner.symbol} has won the game")
