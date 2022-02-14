from enum import IntEnum

class Player(IntEnum):
    X=1
    O=2

# Dictionary that maps the integer into a symbol for display purposes
player_symbol = {
    Player.X:'X',
    Player.O:'O'
}