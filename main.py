from model.game import Game
from view.board_console_view import BoardConsoleView
from view.game_console_view import GameConsoleView
from controller.gameManager import GameManager
board_size = input('Please designate a board size: \n(An even number between 4-10) ')
game = Game(size=int(board_size))

board_view = BoardConsoleView(game.board)
game_view = GameConsoleView(board_view)

controller = GameManager(game, game_view)
controller.run_game()

