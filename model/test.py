import game

thing = game.Game(6)
print(thing.board)
map = thing.findLegalMoves()
print(map)
move = [1, 3]

if move in map["valid_moves"]:
    i = map["valid_moves"].index(move)
    thing.makeMove(map["flips"][i])
    print(thing.board)
