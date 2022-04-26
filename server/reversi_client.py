
import pickle
from server.network import Network

from model.disk import Disk

class ReversiClient:
    def __init__(self):
        run = True
        n = Network()
        player = int(n.getP())
        print("You are player", player)

        while run:
            try:
                game = n.send("get")

            except:
                run = False
                print("Couldn't get game")
                break

            if game.playerWent():
                ##redraw window

                





