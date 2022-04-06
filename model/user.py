class User:
    def __init__(self):
        self.username = "guest"
        self.userelo = 1500
        self.total_matches_played = 0

    def update_username(self, un):
        self.username = un
        print(self.username)

    def update_elo(self, elo):
        self.userelo = elo

    def update_matches(self, matches):
        self.total_matches_played = matches

    def increase_matches(self):
        self.total_matches_played += 1

    def get_username(self):
        return self.username
    
    def get_userelo(self):
        return self.userelo
    
    def get_total_matches(self):
        return self.total_matches_played
