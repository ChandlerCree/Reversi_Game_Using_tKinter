from shutil import move
import socket
import pickle
from server.exercise import Exercise

from model.disk import Disk

class ReversiClient:
    def __init__(self, host='127.0.0.1', port=1234, buffer_size=1024):
        self.host = host
        self.port = port
        self.buffer_size = buffer_size

    def start_client(self):
        with socket.socket() as my_socket:
            my_socket.connect((self.host, self.port))
            print('Client connected.')


