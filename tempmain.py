import random
import sys


def drawBoard(board):
    HLINE = '  +---+---+---+---+---+---+---+---+'
    VLINE = '  |   |   |   |   |   |   |   |   |'

    print('    1   2   3   4   5   6   7   8')
    print(HLINE)
    for y in range(8):
        #print(VLINE)
        print(y + 1, end=' ')
        for x in range(8):
            print('| %s' % (board[x][y]), end=' ')
        print('|')
        #print(VLINE)
        print(HLINE)


def resetBoard(board):
    for x in range(8):
        for y in range(8):
            board[x][y] = ' '

    board[3][3] = 'X'
    board[3][4] = 'O'
    board[4][3] = 'O'
    board[4][4] = 'X'


def getNewBoard():
    board = []
    for i in range(8):
        board.append([' '] * 8)

    return board


def isValidMove(board, square, xstart, ystart):
    if board[xstart][ystart] != ' ' or not isOnBoard(xstart, ystart):
        return False

    board[xstart][ystart] = square

    if square == 'X':
        otherSquare = 'O'
    else:
        otherSquare = 'X'

    squaresToFlip = []

    for xdir, ydir in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
        x, y = xstart, ystart
        x += xdir
        y += ydir
        if isOnBoard(x, y) and board[x][y] == otherSquare:
            x += xdir
            y += ydir
            if not isOnBoard(x, y):
                continue
            while board[x][y] == otherSquare:
                x += xdir
                y += ydir
                if not isOnBoard(x, y):
                    break
            if not isOnBoard(x, y):
                continue
            if board[x][y] == square:
                while True:
                    x -= xdir
                    y -= ydir
                    if x == xstart and y == ystart:
                        break
                    squaresToFlip.append([x, y])

    board[xstart][ystart] = ' '
    if len(squaresToFlip) == 0:
        return False
    return squaresToFlip


def isOnBoard(x, y):
    return 0 <= x <= 7 and 0 <= y <= 7


def getBoardWithValidMoves(board, square):
    duplicateBoard = getBoardCopy(board)
    for x, y in getValidMoves(duplicateBoard, square):
        duplicateBoard[x][y] = '.'
    return duplicateBoard


def getValidMoves(board, square):
    validMoves = []

    for x in range(8):
        for y in range(8):
            if isValidMove(board, square, x, y) != False:
                validMoves.append([x, y])
    return validMoves


def getScoreOfBoard(board):
    xscore = 0
    oscore = 0
    for x in range(8):
        for y in range(8):
            if board[x][y] == 'X':
                xscore += 1
            if board[x][y] == 'O':
                oscore += 1
    return {'X':xscore, 'O':oscore}


def enterPlayerSquare():
    square = ''
    while not (square == 'X' or square == 'O'):
        print('Choose X or O.')
        square = input().upper()

    #the first element in the list is the player square second is the opponent square.
    if square == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def whoGoesFirst():
    if random.randint(0,1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


def makeMove(board, square, xstart, ystart):
    squaresToFlip = isValidMove(board, square, xstart, ystart)

    if squaresToFlip == False:
        return False

    board[xstart][ystart] = square
    for x, y in squaresToFlip:
        board[x][y] = square
    return True


def getBoardCopy(board):
    duplicateBoard = getNewBoard()

    for x in range(8):
        for y in range(8):
            duplicateBoard[x][y] = board[x][y]

    return duplicateBoard


def isOnCorner(x, y):
    return (x==0 and y==0) or (x==7 and y==7) or (x==0 and y==7) or (x==7 and y==0)


def getPlayerMove(board, playerSquare):
    DIGITS1TO8 = '1 2 3 4 5 6 7 8'.split()
    while True:
        print('Please make your move or type quit to end the game. \nHorizontal number first, vertical number second (i.e. 53).')
        move = input().lower()
        if move == 'quit':
            return 'quit'

        #Checks if input is 2 digits long and if both digits are in range 1-8
        if len(move) == 2 and move[0] in DIGITS1TO8 and move[1] in DIGITS1TO8:
            x = int(move[0]) - 1
            y = int(move[1]) - 1
            if isValidMove(board, playerSquare, x, y) == False:
                continue
            else:
                break

        else:
            print('Invalid Move')

    return [x, y]


def getOpponentMove(board, opponentSquare):
    #Creates an array of possible moves for the opponent
    possibleMoves = getValidMoves(board, opponentSquare)

    #Shuffles the list of possible moves
    random.shuffle(possibleMoves)

    #Opponent will always go for a corner if it is available
    for x, y in possibleMoves:
        if isOnCorner(x, y):
            return [x, y]

    bestScore = -1
    for x, y in possibleMoves:
        duplicateBoard = getBoardCopy(board)
        makeMove(duplicateBoard, opponentSquare, x, y)
        score = getScoreOfBoard(duplicateBoard)[opponentSquare] #NOT SURE WHAT THIS IS
        if score > bestScore:
            bestMove = [x, y]
            bestScore = score
    return bestMove


def showPoints(playerSquare, opponentSquare):
    scores = getScoreOfBoard(mainBoard)
    print('Player 1 has %s points. Player 2 has %s points.' % (scores[playerSquare], scores [opponentSquare]))


print('Welcome to Reversi!')

if __name__ == '__main__':
    while True:
        mainBoard = getNewBoard()
        resetBoard(mainBoard)
        playerSquare, opponentSquare = enterPlayerSquare()
        turn = whoGoesFirst()
        print('\n' + turn + ' will go first.')

        while True:
            if turn == 'Player 1':
                drawBoard(mainBoard)
                showPoints(playerSquare, opponentSquare)
                print('\nPlayer 1 (%s):' % (playerSquare))
                move = getPlayerMove(mainBoard, playerSquare)
                if move == 'quit':
                    print('Thanks for playing!')
                    sys.exit()
                else:
                    makeMove(mainBoard, playerSquare, move[0], move[1])

                if getValidMoves(mainBoard, opponentSquare) == []:
                    break
                else:
                    turn = 'Player 2'

            else:
                drawBoard(mainBoard)
                showPoints(playerSquare, opponentSquare)
                print('\nPlayer 2 (%s):' % (opponentSquare))
                move = getPlayerMove(mainBoard, opponentSquare)
                if move == 'quit':
                    print('Thanks for playing!')
                    sys.exit()
                else:
                    makeMove(mainBoard, opponentSquare, move[0], move[1])

                if getValidMoves(mainBoard, playerSquare) == []:
                    break
                else:
                    turn = 'Player 1'

                            # Vs Opponent
        '''
        while True:
            if turn == 'Player 1':
                drawBoard(mainBoard)
                showPoints(playerSquare, opponentSquare)
                move = getPlayerMove(mainBoard, playerSquare)
                if move == 'quit':
                    print('Thanks for playing!')
                    sys.exit()
                else:
                    makeMove(mainBoard, playerSquare, move[0], move[1])
                if getValidMoves(mainBoard, opponentSquare) == []:
                    break
                else:
                    turn = 'Player 2'
            else:
                drawBoard(mainBoard)
                showPoints(playerSquare, opponentSquare)
                input('Press Enter to see the opponent\'s move.')
                x, y = getOpponentMove(mainBoard, opponentSquare)
                makeMove(mainBoard, opponentSquare, x, y)
                if getValidMoves(mainBoard, playerSquare) == []:
                    break
                else:
                    turn = 'Player 1'
        '''

        drawBoard(mainBoard)
        scores = getScoreOfBoard(mainBoard)
        print('X scored %s points. O scored %s points.' % (scores['X'], scores['O']))
