from numpy import size
from controller.database.database_abstract import DatabaseAbstract

class DatabaseGetPlayer2(DatabaseAbstract):
    def __init__(self, player1):
        self.quer_player = "select distinct player2 from game where player1 = %s"
        self.get_player = (player1,)
        self.player_id="not found"

    def execute_query(self):
        with self.my_connect.cursor() as cursor:
            cursor.execute(self.quer_player, self.get_player)
            result = cursor.fetchall()
            self.my_connect.commit()
            self.player_id = result[0][0]