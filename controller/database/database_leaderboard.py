from controller.database.database_abstract import DatabaseAbstract

class DatabaseLeaderboard(DatabaseAbstract):
    def __init__(self):
        self.leaderboard_query = "Select username, elo from player order by elo desc limit 10;"


    def execute_query(self):
        with self.my_connect.cursor() as cursor:
            cursor.execute(self.leaderboard_query)
            result = cursor.fetchall()
            self.my_connect.commit()

            return result