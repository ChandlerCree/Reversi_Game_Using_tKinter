from model.user import User

class LoggedInManager():
    def is_user_logged_in(self, user: User):
        print("Checking if user is logged in...")
        username = user.get_username()
        if username != "guest":
            print("Username = " + username)
            print("Confirmed.")
            return True
        return False