<<<<<<< HEAD
class Player:
    def __init__(self, whatPlayer):
        self.x = whatPlayer
        # symbol for corrsodining values
        if whatPlayer == 1:
            self.symbol = "X"
        else:
            self.symbol = "O"
=======
from enum import IntEnum

class Player(IntEnum):
    X=1
    O=2

# Dictionary that maps the integer into a symbol for display purposes
player_symbol = {
    Player.X:'X',
    Player.O:'O'
}
>>>>>>> main
