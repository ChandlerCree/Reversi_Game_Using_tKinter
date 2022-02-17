from abc import ABC, abstractmethod

class GameView(ABC):
    def __init__(self, board_view):
        self.board_view = board_view

    def display_board(self):
        self.board_view.display()

    @abstractmethod
    def display_curr_player(self, player):
        pass

    @abstractmethod
    def display_curr_score(self, p1_score, p2_score):
        pass

    @abstractmethod
    def show_legal_moves(self):
        pass

    @abstractmethod
    def get_move(self):
        pass

    @abstractmethod
    def display_illegal_moves(self):
        pass

    @abstractmethod
    def display_winner(self, winner):
        pass
