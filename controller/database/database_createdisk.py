from numpy import size
from controller.database.database_abstract import DatabaseAbstract

class DatabaseCreateDisk(DatabaseAbstract):
    def __init__(self, x_pos, y_pos, player, game):
        self.quer_disk = "insert into disk (x_pos, y_pos, participant_id, game_id) values (%s, %s, %s, %s)"

        self.create_disk = (x_pos, y_pos, player, game)


    def execute_query(self):
        with self.my_connect.cursor() as cursor:
            cursor.execute(self.quer_disk, self.create_disk)
            result = cursor.fetchall()
            self.my_connect.commit()
            for row in result:
                print(row)
