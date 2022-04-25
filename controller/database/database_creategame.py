from numpy import size
from controller.database.database_abstract import DatabaseAbstract

class DatabaseCreateGame(DatabaseAbstract):
    def __init__(self, player1, player2, curr_player):
        self.quer_game = "insert into game (player1, player2, curr_player) values (%s, %s, %s)"
        self.create_game = (player1, player2, curr_player)

    def execute_query(self):
        with self.my_connect.cursor() as cursor:
            cursor.execute(self.quer_game, self.create_game)
            result = cursor.fetchall()
            self.my_connect.commit()
            for row in result:
                print(row)