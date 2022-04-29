from numpy import size
from controller.database.database_abstract import DatabaseAbstract

class DatabaseGetGame(DatabaseAbstract):
    def __init__(self, player1, player2):
        self.quer_game = "select distinct id from game where (player1 = %s and player2 = %s) or (player1 = %s and player2 = %s)"
        self.get_game = (player1, player2, player2, player1)
        self.game_id="not found"

    def execute_query(self):
        with self.my_connect.cursor() as cursor:
            cursor.execute(self.quer_game, self.get_game)
            result = cursor.fetchall()
            self.my_connect.commit()
            self.game_id = result[0][0]