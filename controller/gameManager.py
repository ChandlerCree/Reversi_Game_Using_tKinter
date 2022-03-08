from model.game import Game
from view.game_view import GameView


class GameManager:
    def __init__(self, model: Game, view: GameView):
        self.model = model
        self.view = view
        self.starting_player = self.model.curPlayer.symbol


    def run_game(self):
        game_terminated = False

        # loop that runs the entire game
        while not game_terminated:
            moveFlipMap = self.model.find_legal_moves()
            if not len(moveFlipMap["valid_moves"]) == 0:

                # find legal moves and display board
                self.model.show_legal_moves(moveFlipMap["valid_moves"])
                self.view.display_board()
                self.view.display_curr_player(self.model.curPlayer)
                self.view.display_curr_score(
                    self.model.playerOneCount,
                    self.model.playerTwoCount,
                    self.starting_player,
                )

                row, col = self.view.get_move()

                move = [row, col]

                # make sure move is valid
                while move not in moveFlipMap["valid_moves"]:
                    self.view.display_illegal_moves()
                    row, col = self.view.get_move()
                    move = [row, col]

                # make move
                i = moveFlipMap["valid_moves"].index(move)
                self.model.make_move(moveFlipMap["flips"][i])
                self.model.reset_board()

                # make sure no one has won
                game_terminated, winner = self.model.who_wins()
                if not game_terminated:
                    self.model.change_curr_player()
                else:
                    self.view.display_board()
                    print("\n")
                    self.view.display_curr_score(
                        self.model.playerOneCount,
                        self.model.playerTwoCount,
                        self.starting_player,
                    )
                    self.view.display_winner(winner)

                self.model.update_score()
            else:
                # make sure there are legal moves
                if self.model.ensure_legal_moves():
                    self.model.change_curr_player()
                else:
                    # if there are none, game is over, use special who_wins
                    game_terminated = True
                    __, winner = self.model.who_wins(gameOverBoardNotFull=True)
                    self.view.display_board()
                    print("\n")
                    self.view.display_curr_score(
                        self.model.playerOneCount,
                        self.model.playerTwoCount,
                        self.starting_player,
                    )
                    self.view.display_winner(winner)
