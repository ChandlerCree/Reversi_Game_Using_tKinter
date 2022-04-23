import socket
import pickle
import threading 
from _thread import *
from model.online_game import OnlineGame

from model.disk import Disk


class ReversiServer:
    def __init__(self, host='127.0.0.1', port=1234, buffer_size=2048):
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

                gameId = (self.idCount - 1)//2

                if self.idCount % 2 == 1:
                    self.games[gameId] = OnlineGame(gameId)
                    print("Creating a new game...")
                else:
                    self.games[gameId].ready = True
                    self.p = 1


                thread = threading.Thread(target=self.handle_client, args=(conn, self.p, gameId))
                thread.start()

    def handle_client(self, conn, p, gameId):
        self.idCount
        conn.send(str.encode(str(p)))

        reply = ""
        while True:
            try:
                data = conn.recv(4096).decode()

                if gameId in self.games:
                    game = self.games[gameId]

                    if not data:
                        break
                    else:
                        if data == "reset":
                            print("reset")
                            pass
                        elif data != "get":
                            game.play(p, data)

                        conn.sendall(pickle.dumps(game))

                else:
                    break

            except:
                break

        print("Lost connection")
        try:
            del self.games[gameId]
            print("Closing Game ", gameId)
        except:
            pass
        self.idCount -= 1
        conn.close()




