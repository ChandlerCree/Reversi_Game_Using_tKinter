from abc import ABC, abstractmethod
import numpy as np
import model.player as p
import random

from controller.database.database_creategame import DatabaseCreateGame
from controller.database.database_createdisk import DatabaseCreateDisk
from controller.database.database_updatedisk import DatabaseUpdateDisk
from controller.database.database_getgame import DatabaseGetGame
from controller.database.database_deletegame import DatabaseDeleteGame

class Game(ABC):

    def __init__(self, size, player1, player2, player1_username, player2_username, is_copy):

        self.bSize = size
        if int(size) % 2 != 0:
            raise ValueError("Size of board must be even")

        # initialize empty board and players
        self.board = np.zeros((size, size), dtype=int)
        self.player1 = player1
        self.player2 = player2
        self.player1_username = player1_username
        self.player2_username = player2_username
        self.is_copy = is_copy

        # determine who the first player is randomly
        if self.player1.x == self.who_goes_first():
            self.curPlayer = self.player1
            self.currplayer_username = self.player1_username
        else:
            self.curPlayer = self.player2
            self.currplayer_username = self.player2_username

        if not is_copy:
            self.delete_game_db(self.player1_username)
            self.create_game_db(self.player1_username, self.player2_username, self.currplayer_username)
            self.game_id = self.get_game_db(self.player1_username,self.player2_username)
            print(self.game_id)

        # create initial disks at middle corners

        # first person to move will always go in top left and bottom right of middle
        self.board[int((size / 2) - 1)][int((size / 2) - 1)] = self.curPlayer.x
        self.board[int((size / 2))][int((size / 2))] = self.curPlayer.x


        # second person to move will always go in top right and bottom left of middle
        self.board[int((size / 2) - 1)][int((size / 2))] = (self.curPlayer.x) % 2 + 1
        self.board[int((size / 2))][int((size / 2) - 1)] = (self.curPlayer.x) % 2 + 1

        self.playerOneCount = 2
        self.playerTwoCount = 2

        if self.curPlayer == self.player1 and not is_copy:
            # place initial disks in DB
            self.create_disk_db(int((self.bSize/2)-1), int((self.bSize/2)-1), self.game_id, self.player2_username)
            self.create_disk_db(int(self.bSize/2), int(self.bSize/2), self.game_id, self.player2_username)
            self.create_disk_db(int((self.bSize/2)-1), int(self.bSize/2), self.game_id, self.player1_username)
            self.create_disk_db(int(self.bSize/2), int((self.bSize/2)-1), self.game_id, self.player1_username)

        elif self.curPlayer == self.player2 and not is_copy:
            # place initial disks in DB
            self.create_disk_db(int((self.bSize/2)-1), int((self.bSize/2)-1), self.game_id, self.player1_username)
            self.create_disk_db(int(self.bSize/2), int(self.bSize/2), self.game_id, self.player1_username)
            self.create_disk_db(int((self.bSize/2)-1), int(self.bSize/2), self.game_id, self.player2_username)
            self.create_disk_db(int(self.bSize/2), int((self.bSize/2)-1), self.game_id, self.player2_username)

    # coin flip for who goes first
    def who_goes_first(self):
        return random.randint(1, 2)

    # change who the current player is
    def change_curr_player(self):

        # check who's the current player before changing
        if self.curPlayer.x == 1:
            self.curPlayer = self.player2
            self.currplayer_username = self.player2_username

        else:
            self.curPlayer = self.player1
            self.currplayer_username = self.player1_username

    # checks if this location is on the board
    def in_bounds(self, x, y):
        return 0 <= x <= self.bSize - 1 and 0 <= y <= self.bSize - 1

    # set the board value to 3 on each spot the player can go
    def show_legal_moves(self, validMoves):
        for x, y in validMoves:
            self.board[x][y] = 3
    # takes the "legal moves" off the board
    def reset_board(self):
        for x in range(self.bSize):
            for y in range(self.bSize):
                if self.board[x][y] == 3:
                    self.board[x][y] = 0

    def find_legal_moves(self):
        validMoves = []
        flips = []

        # loop through all board pieces
        for i in range(self.bSize):
            for j in range(self.bSize):

                listOfFlips = []

                # skip any non-empty pieces
                if self.board[i][j] != 0:
                    continue

                self.board[i][j] = self.curPlayer.x

                # loop through the 8 possible directions
                for xdir, ydir in [
                    [0, 1],
                    [1, 1],
                    [1, 0],
                    [1, -1],
                    [0, -1],
                    [-1, -1],
                    [-1, 0],
                    [-1, 1],
                ]:
                    # create copies to keep track of original starting point
                    x, y = i, j

                    # move to adjacent piece
                    x += xdir
                    y += ydir

                    # if you are at another players piece, continue moving
                    if self.in_bounds(x, y) and (
                        self.board[x][y] != self.curPlayer.x and self.board[x][y] != 0
                    ):
                        x += xdir
                        y += ydir

                        # reach the end of the board, try another direction
                        if not self.in_bounds(x, y):
                            continue

                        # while you still see other player pieces, continue moving in the same direction
                        while self.board[x][y] != self.curPlayer.x:
                            x += xdir
                            y += ydir

                            # if you reach the end of the board, no valid move possible
                            if not self.in_bounds(x, y):
                                break

                        if not self.in_bounds(x, y):
                            continue

                        # if you find one of your own pieces, it is a valid move
                        if self.board[x][y] == self.curPlayer.x:
                            while True:
                                x -= xdir
                                y -= ydir
                                listOfFlips.append([x, y])
                                # once you get back to original piece break loop
                                if x == i and y == j:
                                    break

                # reset piece in case it wasn't a valid move
                self.board[i][j] = 0

                # if it was a valid move, keep track of it and its corresponding flips
                if len(listOfFlips) != 0:
                    validMoves.append([i, j])
                    flipList = listOfFlips
                    flips.append(list(flipList))
                else:
                    continue

        # create a dictionary of the valid moves, and the corresponding flips for that move
        movesToFlipsMap = {"valid_moves": validMoves, "flips": flips}

        return movesToFlipsMap

    # make move and then flip corresponding. Assumes move is legal
    def make_move(self, flipPieces):
        for x, y in flipPieces:
            if self.board[x][y] != self.player1.x and self.board[x][y] != self.player2.x and not self.is_copy:
                self.create_disk_db(x, y, self.game_id, self.currplayer_username)
            elif not self.is_copy:
                self.update_disk_db(x, y, self.game_id, self.currplayer_username)

            self.board[x][y] = self.curPlayer.x

    # find if any empty pieces
    def is_board_full(self):
        return not np.any(self.board == 0)

    # checks to see if there are ANY legal moves
    # assumes the current player has been determined to not have any moves
    def ensure_legal_moves(self):

        # look for legal moves for other player
        self.change_curr_player()
        legalMovesOtherPlayer = self.find_legal_moves()

        # make sure to turn curPlayer back orginal
        self.change_curr_player()

        # if there are no legal moves for other player, there are no moves possible
        if len(legalMovesOtherPlayer["valid_moves"]) == 0:
            return False
        return True

    def update_score(self):
        self.playerOneCount = 0
        self.playerTwoCount = 0
        for i in range(self.bSize):
            for j in range(self.bSize):
                if self.board[i][j] == 1:
                    self.playerOneCount += 1
                elif self.board[i][j] == 2:
                    self.playerTwoCount += 1
                else:
                    pass

    def who_wins(self, gameOverBoardNotFull=False):

        # check for special case where no more legal moves but board isn't full
        if not gameOverBoardNotFull:
            # make sure board is full
            if not self.is_board_full():
                return False, None

        self.update_score()

        # if one player has more disks than the other, they win. draw otherwise
        if self.playerOneCount > self.playerTwoCount:
            return True, self.player1
        elif self.playerOneCount < self.playerTwoCount:
            return True, self.player2
        drawPlayer = p.Player(-1)
        return True, drawPlayer

    def get_score(self):
        return (self.playerOneCount, self.playerTwoCount)
    
    def select_move(self, board):
        return self.curPlayer.select_move(board)

    def create_game_db(self, player1_name, player2_name, currplayer_name):
        self.create_game = DatabaseCreateGame(player1_name, player2_name, currplayer_name)
        self.create_game.connect_to_database()
        self.create_game.execute_query()

    def delete_game_db(self, player1_name):
        self.delete_game = DatabaseDeleteGame(player1_name)
        self.delete_game.connect_to_database()
        self.delete_game.execute_query()

    def get_game_db(self, player1_name, player2_name):
        self.get_game = DatabaseGetGame(player1_name, player2_name)
        self.get_game.connect_to_database()
        self.get_game.execute_query()
        return self.get_game.game_id

    def create_disk_db(self, x_pos, y_pos, player, game):
        self.create_disk = DatabaseCreateDisk(x_pos, y_pos, player, game)
        self.create_disk.connect_to_database()
        self.create_disk.execute_query()

    def update_disk_db(self, x_pos, y_pos, game, player):
        self.update_disk = DatabaseUpdateDisk(x_pos, y_pos, game, player)
        self.update_disk.connect_to_database()
        self.update_disk.execute_query()
