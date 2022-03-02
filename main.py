from mysql.connector import connect, Error
from getpass import getpass
from model.game import Game
from view.board_console_view import BoardConsoleView
from view.game_console_view import GameConsoleView
import tkinter as tk
from view.main_menu import MainMenu
from view.login_view import LoginView
from controller.gameManager import GameManager


bg_1 = "#E0FBFC"
bg_2 = "#C2DFE3"
cor_1 = "#9DB4C0"
incor_1 = "#5C6B73"
fg_1 = "#253237"


class Gui(tk.Tk):
    def __init__(self):
        super().__init__()
        # configure the root window
        self.title('Reversi')
        self.geometry('300x250')
        self.configure(bg=bg_1)

        # label
        title_label = tk.Label(text="REVERSI", bg=bg_2, width="300", height="1", font=("Calibri", 24, "bold"), fg=fg_1,
                               borderwidth=4, relief="groove", pady="10")
        title_label.pack()


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
        if login_success:
            gui = Gui()
            frame = MainMenu(gui)
            gui.mainloop()
        else:
            print("Error logging in.")
    except Error as e:
        print(e)

    



# run the game
controller = GameManager(game, game_view)
controller.run_game()

