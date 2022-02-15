from model.game import Game
from view.game_view import GameView


class GameManager:
    def __init__(self, model: Game, view: GameView):
        self.model = model
        self.view = view

    def run_game(self):
        game_terminated = False

        # loop that runs the entire game
        while not game_terminated:

            # find legal moves and display board
            moveFlipMap = self.model.findLegalMoves()
            self.view.display_board()
            self.view.display_curr_player(self.model.curPlayer)

            row, col = self.view.get_move()

            move = [row, col]

            # make sure move is valid
            while move not in moveFlipMap["valid_moves"]:
                self.view.display_illegal_moves()
                row, col = self.view.get_move()
                move = [row, col]

            # make move
            i = moveFlipMap["valid_moves"].index(move)
            self.model.makeMove(moveFlipMap["flips"][i])

            # make sure no one has one
            game_terminated, winner = self.model.whoWins()
            if not game_terminated:
                self.model.changeCurPlayer()
            else:
                self.view.display_board()
                self.view.display_winner(winner)
