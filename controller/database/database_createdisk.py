from numpy import size
from controller.database.database_abstract import DatabaseAbstract

class DatabaseCreateDisk(DatabaseAbstract):
    def __init__(self, x_pos, y_pos, game, player):
        self.register_quer = "insert into disk (game, player) values (%s, %s, %s, %s)"

        self.create_disk = (x_pos, y_pos, game, player)


    def execute_query(self):
        with self.my_connect.cursor() as cursor:
            cursor.execute(self.register_quer, self.create_disk)
            result = cursor.fetchall()
            self.my_connect.commit()
            for row in result:
                print(row)

        print("disk: " + self.create_disk[0] + " created successfully.")