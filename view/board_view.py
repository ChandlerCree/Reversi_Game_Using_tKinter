from abc import ABC, abstractmethod

class BoardView(ABC):
<<<<<<< HEAD
    def __init__(self, board):
        self.board=board

    @abstractmethod
    def display(self):
        pass
    
=======
    def __init__(self,board):
        self.board = board

        @abstractmethod
        def display(self):
            pass
>>>>>>> main
