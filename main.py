from mysql.connector import connect, Error
from getpass import getpass

from model.game import Game
from view.board_console_view import BoardConsoleView
from view.game_console_view import GameConsoleView
from view.main_menu import MainMenu
from view.gui import Gui
from controller.gameManager import GameManager


bg_1 = "#E0FBFC"
bg_2 = "#C2DFE3"
cor_1 = "#9DB4C0"
incor_1 = "#5C6B73"
fg_1 = "#253237"


if __name__ == "__main__":
    try:
        my_connect = connect(
                    host="localhost",
                    #user=input('Enter username: '),
                    #passwd=getpass('Enter password:'),
                    user="root",
                    passwd="NU22ms0cc3rGK",
                    database="reversi"
                )

        # Get user input for board size
        #board_size = input("Please designate a board size: \n(An even number between 4-10) ")
        board_size = 2
        game = Game(size=int(board_size))  # create the game

        # add the views
        board_view = BoardConsoleView(game.board)
        game_view = GameConsoleView(board_view)

        # creates game manager object
        controller = GameManager(game, game_view)
        # prompts user to login
        login_success = False
        login_success = controller.login(my_connect)
        # runs the game
        if login_success == True:
            print('Logged in as User!')
            gui = Gui()
            frame = MainMenu(gui)
            gui.mainloop()
        elif login_success == 'guest':
            print('Logged in as guest!')
            gui = Gui()
            frame = MainMenu(gui)
            gui.mainloop()
        else:
            print("Error logging in.")
    except Error as e:
        print(e)

    



### run the game
#controller = GameManager(game, game_view)
#controller.run_game()

