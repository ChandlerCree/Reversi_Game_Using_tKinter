from model.user import User

class EnoughMatchesManager():
    def enough_matches_played(self, user: User):
        print("Checking if user has played 30 matches...")
        user_matches = user.get_total_matches()
        if user_matches >= 30:
            print(str(user_matches) + " matches played.")
            print("Confirmed.")
            return True

        print(user_matches)
        return False