from controller.database.database_abstract import DatabaseAbstract

class DatabaseEloupdate(DatabaseAbstract):
    def __init__(self, logged_user, updated_matches):
        self.quer_eloupdate = "UPDATE player SET matches = %s WHERE username = %s"
        
        self.update_tuple = (updated_matches, logged_user)


    def execute_query(self):
        with self.my_connect.cursor() as cursor:
            cursor.execute(self.quer_eloupdate, self.update_tuple)
            self.my_connect.commit()
