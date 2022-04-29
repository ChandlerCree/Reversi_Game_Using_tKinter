from controller.database.database_abstract import DatabaseAbstract

class DatabaseDeleteGame(DatabaseAbstract):
    def __init__(self, player1):
        self.del_game_quer = "DELETE FROM game WHERE player1 = %s or player2 = %s"
        self.game_to_delete = (player1, player1)
    
    def execute_query(self):
        with self.my_connect.cursor(buffered=True) as cursor:
            cursor.execute(self.del_game_quer, self.game_to_delete)
            self.my_connect.commit()
