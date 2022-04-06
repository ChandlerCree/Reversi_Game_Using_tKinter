from controller.database.database_abstract import DatabaseAbstract

class DatabaseDelete(DatabaseAbstract):
    def __init__(self, entry_username):
        self.delacc_quer = "DELETE FROM player WHERE username = %s"

        self.user_to_delete = (entry_username,)

    
    def execute_query(self):
        with self.my_connect.cursor(buffered=True) as cursor:
            cursor.execute(self.delacc_quer, self.user_to_delete)
            self.my_connect.commit()
            print(str(self.user_to_delete[0]) + "'s account has been deleted.")
