from model.game import Game
from view.board_console_view import BoardConsoleView
from view.game_console_view import GameConsoleView
from controller.gameManager import GameManager

# Get user input for board size
board_size = input("Please designate a board size: \n(An even number between 4-10) ")
game = Game(size=int(board_size))  # create the game

# add the views
board_view = BoardConsoleView(game.board)
game_view = GameConsoleView(board_view)

# run the game
controller = GameManager(game, game_view)
controller.run_game()
