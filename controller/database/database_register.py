from controller.database.database_abstract import DatabaseAbstract

class DatabaseRegister(DatabaseAbstract):
    def __init__(self, user_pass_tuple):
        self.register_quer = "insert into player (username, password, elo, matches) values (%s, %s, 1500, 0)"

        self.user_pass_tuple = user_pass_tuple


    def execute_query(self):
        with self.my_connect.cursor() as cursor:
            cursor.execute(self.register_quer, self.user_pass_tuple)
            result = cursor.fetchall()
            self.my_connect.commit()
            for row in result:
                print(row)

        print("user: " + self.user_pass_tuple[0] + " registered successfully.")