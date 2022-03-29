from copy import deepcopy
import random
from shutil import which
import numpy as np
from model.game import Game
from model.player import Player


class AIGame(Game):
    def __init__(self, size, diff):
        super().__init__(size)
        self.AIDifficulty = diff

    def evalfunc(self,board):
        num2 = 0
        num1 = 0
        for i in range(self.bSize):
            for j in range(self.bSize):
                if board[i][j] == 1:
                    num1 += 1
                if board[i][j] == 2:
                    num2 += 1
        return num2 - num1

    def minimax_value(self, board, player, search_depth, alpha, beta):

        winner = self.winner_value(board)

        if winner == 2:
            return 1000
        
        if winner == 1:
            return -1000
        
        if winner == -1:
            return 0

        moveFlips = self.generate_legal_moves(board,player)
        if len(moveFlips["valid_moves"]) == 0:
            return self.minimax_value(board, 3-player, search_depth, alpha, beta)

        if search_depth == 0:
            return self.evalfunc(board)

        if player == 2:
            best_val = float("-inf") 
            moveFlips = self.generate_legal_moves(board,player)
            for m in moveFlips["valid_moves"]:
                newBoard = self.play_move(board, moveFlips["flips"][moveFlips["valid_moves"].index(m)], player)
                best_val = max(best_val, self.minimax_value(newBoard, 3 - player, search_depth - 1, alpha, beta))
                if best_val >= beta:
                    return best_val
                alpha = max(best_val, alpha)
                
        else:
            best_val = float("inf") 
            moveFlips = self.generate_legal_moves(board,player)
            for m in moveFlips["valid_moves"]:
                newBoard = self.play_move(board, moveFlips["flips"][moveFlips["valid_moves"].index(m)], player)
                best_val = min(best_val, self.minimax_value(newBoard, 3 - player, search_depth - 1, alpha, beta))
                if best_val <= alpha:
                    return best_val
                beta = min(best_val, beta)

        return best_val

    def select_move(self, board):

        bestVal = float("-inf")
        bestMove = None
        moveFlips = self.generate_legal_moves(board, 2)
        for m in moveFlips["valid_moves"]:
            newBoard = self.play_move(board, moveFlips["flips"][moveFlips["valid_moves"].index(m)], 2)
            testMove = self.minimax_value(newBoard, 1, self.AIDifficulty, float('-inf'),float('inf') )
            if testMove > bestVal:
                bestMove = m
                bestVal = testMove

        return bestMove
    
    def winner_value(self, board):
        gameCheck = Game(self.bSize)
        gameCheck.board = deepcopy(board)
        #print(gameCheck.board)
        return self.who_wins_2(gameCheck)

    def play_move(self, board, move, player):
        game_piece = Game(self.bSize)
        game_piece.board = deepcopy(board)
        if player == 1:
            game_piece.curPlayer = game_piece.player1
        else: 
            game_piece.curPlayer = game_piece.player2
        
        game_piece.make_move(move)

        newBoard = deepcopy(game_piece.board)
        return newBoard
    
    def generate_legal_moves(self, board, player):
        game_piece = Game(self.bSize)
        game_piece.board = deepcopy(board)
        if player == 1:
            game_piece.curPlayer = game_piece.player1
        else: 
            game_piece.curPlayer = game_piece.player2
        
        #print(game_piece.board)
        legal_moves = game_piece.find_legal_moves()
        return legal_moves
    
    def who_wins_2(self, gameCopy):

        first = gameCopy.find_legal_moves()
        gameCopy.change_curr_player()
        second = gameCopy.find_legal_moves()
        gameCopy.change_curr_player()

        if first["valid_moves"] or second["valid_moves"]:
            return 0

        [one, two] = gameCopy.get_score()

        if one > two:
            return 1
        if two > one: 
            return 2

        return -1
