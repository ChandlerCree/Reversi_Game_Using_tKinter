from controller.database.database_abstract import DatabaseAbstract

class DatabaseUpdateDisk(DatabaseAbstract):
    def __init__(self, disk, game, player):
        self.quer_updatedisk = "UPDATE disk SET player = %s WHERE game = %s and x_pos, y_pos = %s"
        self.update_tuple = (player, game, disk)

    def execute_query(self):
        with self.my_connect.cursor() as cursor:
            cursor.execute(self.quer_updatedisk, self.update_tuple)
            self.my_connect.commit()
