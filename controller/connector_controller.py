from mysql.connector import connect, Error
from getpass import getpass

class ConnectorController:
    def __init__(self):
        pass

    def connect_mysql(self):
        self.my_connect = connect(
            host="localhost",
            #user=input('Enter username: '),
            #passwd=getpass('Enter password:'),
            user="root",
            passwd="NU22ms0cc3rGK",
            database="reversi"
        )
        return self.my_connect
