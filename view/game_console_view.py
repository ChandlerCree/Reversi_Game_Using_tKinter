from view.game_view import GameView


class GameConsoleView(GameView):
    def __init__(self, board_View):
        super().__init__(board_View)

    # Tell the player whose turn it is
    def display_curr_player(self, player):
        print(f"\nPlayer {player.symbol}: It's your turn.")

    # Show how many disks each player currently has on the console
    def display_curr_score(self, p1_score, p2_score, starting_player):
        if starting_player == 'X':
            print(f"Player 'X' has: {p1_score} points.\nPlayer 'O' has: {p2_score} points.")
        elif starting_player == 'O':
            print(f"Player 'O' has: {p2_score} points.\nPlayer 'X' has: {p1_score} points.")
        else:
            print('SCORE ERROR')

    def show_legal_moves(self):
        pass

    # prompt the user to enter a move in the console
    def get_move(self):
        move = input("Enter your move (row, col): ")
        move = move.split(",")
        row = int(move[0]) - 1
        col = int(move[1]) - 1
        return row, col

    # Tells user the move they entered is on the board but not playable
    def display_illegal_moves(self):
        print("This move is illegal. Try again.")

    # show who the winner is
    def display_winner(self, winner):
        if winner.x == -1:
            print("DRAW")
        else:
            print(f"Player {winner.symbol} has won the game")
