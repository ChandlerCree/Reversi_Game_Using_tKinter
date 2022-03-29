from abc import ABC, abstractmethod
from mysql.connector import connect
from getpass import getpass

class DatabaseAbstract(ABC):
    def __init__(self):
        pass


    def connect_to_database(self):
        self.my_connect = connect(
            host="reversigroup4.cm0trrj52t1s.us-east-1.rds.amazonaws.com",
            #user=input('Enter username: '),
            #passwd=getpass('Enter password:'),
            user="admin",
            passwd="admin123",
            database="reversi"
        )


    @abstractmethod
    def execute_query(self):
        pass
    

