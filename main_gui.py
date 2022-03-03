from model.game import Game
from view.gui_view import GUIView
from controller.gameManager import GameManager
import tkinter as tk



# Get user input for board size
board_size = input("Please designate a board size: \n(An even number between 4-10) ")
game = Game(size=int(board_size))  # create the game

root = tk.Tk()
game_view = GUIView(root, game.board)
controller = GameManager(game, game_view)
controller.run_game()
root.mainloop()