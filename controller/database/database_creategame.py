from numpy import size
from controller.database.database_abstract import DatabaseAbstract

class DatabaseCreateGame(DatabaseAbstract):
    def __init__(self, player1, player2, curr_player, size):
        self.quer_game = "insert into game (player1, player2, curr_player, size) values (%s, %s, %s, %s)"
        self.create_game = (player1, player2, curr_player, size)

    def execute_query(self):
        with self.my_connect.cursor() as cursor:
            cursor.execute(self.quer_game, self.create_game)
            result = cursor.fetchall()
            self.my_connect.commit()
            for row in result:
                print(row)