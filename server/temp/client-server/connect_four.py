player1 = input('Player one, please enter your name: ')
player2 = input('Player 2, please enter your name: ')

def create_board():
    gameboard = [] 
    for row in range(6):
        row_list = []
        for col in range(7):
            row_list.append('[ ]')
        gameboard.append(row_list)
    return(gameboard)
g_gameboard = create_board()

def print_board(board):
    print(' ', end = '')
    for i in range(1,8):
        print(i, end = '   ')
    for row in board:
        print()
        for item in row:
            print(item, end = ' ')
    print()

print_board(g_gameboard)

def valid_move(g_gameboard, g_column):
    for i in range(6):
        if g_gameboard[i][g_column - 1] == '[ ]':
            return(True)
        else:
            return(False)
        
def place_token(g_gameboard, g_column, g_token):
    for i in range(5, -1, -1):
        if g_gameboard[i][g_column - 1 ] == '[ ]':
            g_gameboard[i][g_column - 1] = '[' + (str(g_token)) + ']'
            break
             
def horizontal_win(g_gameboard, g_column, g_token):
    for i in range(6):
        if g_gameboard[i][g_column - 1] == g_gameboard[i][g_column] == g_gameboard[i][g_column + 1] == g_gameboard[i][
           g_column + 2] == '[' + (str(g_token)) + ']':
           return(True)
        elif g_gameboard[i][g_column - 2] == g_gameboard[i][g_column - 1] == g_gameboard[i][g_column] == g_gameboard[i][g_column + 1] == '[' + (str(g_token)) + ']':
            return(True)
        elif g_gameboard[i][g_column - 3] == g_gameboard[i][g_column - 2] == g_gameboard[i][g_column - 1] == g_gameboard[i][g_column] == '[' + (str(g_token)) + ']':
            return(True)
        elif g_gameboard[i][g_column - 4] == g_gameboard[i][g_column - 3] == g_gameboard[i][g_column - 2] == g_gameboard[i][g_column - 1] == '[' + (str(g_token)) + ']':
            return(True)

def vertical_win(g_gameboard, g_column, g_token):
    for i in range(3):
        if g_gameboard[i][g_column - 1] == g_gameboard[i + 1][g_column - 1] == g_gameboard[i + 2][g_column - 1] == g_gameboard[i + 3][g_column - 1] == '[' + (str(g_token)) + ']':
            return(True)

gameover = False
g_token = 'x'
while not gameover:
    g_column = int(input('Please pick a column from 1 to 7.\n'))
    if valid_move(g_gameboard, g_column) == True:
        place_token(g_gameboard, g_column, g_token)
        print_board(g_gameboard)
        if vertical_win(g_gameboard, g_column, g_token) == True:
            print(player1 + ' won!')
            gameover = True
        elif horizontal_win(g_gameboard, g_column, g_token) == True:
            print(player2 + ' won!')
            gameover = True
    if g_token == 'x':
        g_token = 'o'
    else:
        g_token = 'x'