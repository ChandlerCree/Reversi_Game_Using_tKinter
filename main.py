from model.game import Game
from view.board_console_view import BoardConsoleView
from view.game_console_view import GameConsoleView
from view.login_view import LoginView
from controller.gameManager import GameManager

if __name__ == "__main__":
    # Get user input for board size
    board_size = input("Please designate a board size: \n(An even number between 4-10) ")
    game = Game(size=int(board_size))  # create the game

    # add the views
    board_view = BoardConsoleView(game.board)
    game_view = GameConsoleView(board_view)

    # creates game manager object
    controller = GameManager(game, game_view)
    # prompts user to login
    login_success = False
    login_success = controller.login()
    # runs the game
    if login_success:
        controller.run_game()
    else:
        print("Error logging in.")
