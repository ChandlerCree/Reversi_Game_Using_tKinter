from abc import ABC, abstractmethod
from mysql.connector import connect
from getpass import getpass

class DatabaseAbstract(ABC):
    def __init__(self):
        pass


    def connect_to_database(self):
        self.my_connect = connect(
            host="localhost",
            #user=input('Enter username: '),
            #passwd=getpass('Enter password:'),
            user="root",
            passwd="NU22ms0cc3rGK",
            database="reversi"
        )


    @abstractmethod
    def execute_query(self):
        pass
    

