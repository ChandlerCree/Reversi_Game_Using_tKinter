from numpy import size
from controller.database.database_abstract import DatabaseAbstract

class DatabaseGetDisks(DatabaseAbstract):
    def __init__(self, player, game):
        self.disks = None
        self.quer_disks = "select distinct x_pos, y_pos from disk where player = %s and game = %s"
        self.get_disks = (player, game)

    def execute_query(self):
        with self.my_connect.cursor() as cursor:
            cursor.execute(self.quer_disks, self.get_disk)
            result = cursor.fetchall()
            self.my_connect.commit()
            self.disks = result[0]