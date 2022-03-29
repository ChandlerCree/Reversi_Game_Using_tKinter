from model.user import User
from model.high_elo_manager import HighEloManager
from model.logged_in_manager import LoggedInManager
from model.enough_matches_manager import EnoughMatchesManager

class EligibleChecker:
    def __init__(self):
        self.high_elo = HighEloManager()
        self.logged_in = LoggedInManager()
        self.enough_matches = EnoughMatchesManager()

    def is_elegible_for_ranked(self, user: User):
        if not self.high_elo.high_enough_elo(user):
            print("User not eligible.")
            return False
        if not self.logged_in.is_user_logged_in(user):
            print("User not eligible.")
            return False
        if not self.enough_matches.enough_matches_played(user):
            print("User not eligible.")
            return False
        
        print("User is Eligible.")
        return True