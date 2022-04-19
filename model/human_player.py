from model.game import Game
from model.player import Player

class HumanPlayer(Player):
    def __init__(self, what_player):
        super().__init__(what_player)
        self.controller = None

    def select_move(self, board):
        return self.controller.select_move(board)