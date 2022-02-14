from abc import ABC, abstractmethod

class BoardView(ABC):
    def __init__(self,board):
        self.board = board

        @abstractmethod
        def display(self):
            pass