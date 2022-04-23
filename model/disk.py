
class Disk:
    def __init__(self, row, col, player):
        self.row = row
        self.col = col
        self.player = player

    def get_row(self):
        return self.row

    def get_col(self):
        return self.col

    def get_player(self):
        return self.player