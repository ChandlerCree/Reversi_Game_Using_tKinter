class User:
    def __init__(self):
        self.username = "guest"
        self.userelo = 1500

    def update_username(self, un):
        self.username = un
        print(self.username)

    def update_elo(self, elo):
        self.userelo = elo

    def get_username(self):
        return self.username
    
    def get_userelo(self):
        return self.userelo
