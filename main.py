from model.game import Game
from view.board_console_view import BoardConsoleView
from view.game_console_view import GameConsoleView
from controller.gameManager import GameManager

<<<<<<< HEAD
game = Game(size=8)

board_view = BoardConsoleView(game.board)
game_view = GameConsoleView(board_view)

controller = GameManager(game, game_view)
controller.run_game()
=======
game = Game(board_size=8)

board_view = BoardConsoleView(game.board)
game_view = GameConsoleView (board_view)

controller = GameManager (game, game_view)
controller.run_game()
>>>>>>> main
