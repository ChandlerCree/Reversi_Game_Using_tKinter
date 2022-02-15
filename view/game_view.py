from abc import ABC, abstractmethod

<<<<<<< HEAD

=======
>>>>>>> main
class GameView(ABC):
    def __init__(self, board_view):
        self.board_view = board_view

    def display_board(self):
        self.board_view.display()

    @abstractmethod
    def display_curr_player(self, player):
        pass

    @abstractmethod
    def show_legal_moves(self):
        pass

    @abstractmethod
    def get_move(self):
        pass

    @abstractmethod
<<<<<<< HEAD
    def display_illegal_moves(self):
=======
    def display_illegal_move(self):
>>>>>>> main
        pass

    @abstractmethod
    def display_winner(self, winner):
        pass
<<<<<<< HEAD
=======

    
>>>>>>> main
