import socket
import pickle
import threading
from _thread import *


class ReversiServer:
    def __init__(self, host='127.0.0.1', port=1234, buffer_size=1024):
        self.host = host
        self.port = port
        self.buffer_size = buffer_size
        self.connected = set()
        self.games = {}
        self.idCount = 0
        self.p = 0

    def start_server(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as my_socket:
            my_socket.bind((self.host, self.port))
            my_socket.listen()
            print('Server started.')

            while True:
                conn, address = my_socket.accept()
                print(f'Connected by {address}')

                self.idCount += 1



                thread = threading.Thread(target=self.handle_client, args=(conn, self.p))
                thread.start()

    def handle_client(self, conn, p):
        self.idCount
        conn.send(str.encode(str(p)))

        reply = ""
        while True:
            try:
                data = conn.recv(4096).decode()



            except:
                break

        print("Lost connection")

        self.idCount -= 1
        conn.close()


if __name__ == '__main__':
    server = ReversiServer()
    server.start_server()
