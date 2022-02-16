from model.game import Game
from view.board_console_view import BoardConsoleView
from view.game_console_view import GameConsoleView
from controller.gameManager import GameManager

game = Game(size=6)

board_view = BoardConsoleView(game.board)
game_view = GameConsoleView(board_view)

controller = GameManager(game, game_view)
controller.run_game()
