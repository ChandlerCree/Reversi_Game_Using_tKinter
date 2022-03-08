from mysql.connector import connect, Error
from getpass import getpass

from model.game import Game
from app import App

from controller.gameManager import GameManager

import tkinter as tk

bg_1 = "#E0FBFC"
bg_2 = "#C2DFE3"
cor_1 = "#9DB4C0"
incor_1 = "#5C6B73"
fg_1 = "#253237"


if __name__ == "__main__":
    try:
        my_connect = connect(
            host="localhost",
            # user=input('Enter username: '),
            # passwd=getpass('Enter password:'),
            user="root",
            passwd="NU22ms0cc3rGK",
            database="reversi"
        )

        # Get user input for board size
        board_size = input("Please designate a board size: \n(An even number between 4-10) ")
        # board_size = 2
        game = Game(size=int(board_size))  # create the game

        # add the views
        app = App()
        app.mainloop()


        # creates game manager object
        controller = GameManager(game, tkinter_gui_view)
        controller.run_game()
    except Error as e:
        print(e)
