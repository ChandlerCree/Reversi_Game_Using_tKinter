from model.user import User

class UserManager:
    def __init__(self, user: User):
        self.user = user

    def update_elo(self):
        pass