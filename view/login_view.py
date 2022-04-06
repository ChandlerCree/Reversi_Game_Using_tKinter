import tkinter as tk
from mysql.connector import connect, Error
from getpass import getpass
import tkinter as tk
from controller.database.database_login import DatabaseLogin
from controller.database.database_register import DatabaseRegister
from model.user import User

bg_1 = "#E0FBFC"
bg_2 = "#C2DFE3"
cor_1 = "#9DB4C0"
incor_1 = "#5C6B73"
fg_1 = "#253237"


class LoginView(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        # init function called when new object LoginView is created
        self.first_attempt = True
        self.successful_login = False
        
        #self.geometry("300x250")
        self.title("Reversi")
        self.configure(bg=bg_1)
        self.resizable(False, False)
        self.frame = tk.Frame(self)
        self.frame.configure(bg=bg_1)

        self.login_title = tk.Label(self.frame, text="REVERSI", bg=bg_2, width="20", height="1", font=("Calibri", 24, "bold"), fg=fg_1, borderwidth=4,
                 relief="groove", pady="10")
        self.login_title.pack(pady=(0,12))

        self.login_button = tk.Button(self.frame, text="Login", height="1", width="12", command=self.login, bg=bg_2, fg=fg_1,
                  font=("Calibri", 18, "bold"), activebackground=cor_1)
        self.login_button.pack(pady=12)

        self.register_button = tk.Button(self.frame, text="Register", height="1", width="12", command=self.register, bg=bg_2, fg=fg_1,
                  font=("Calibri", 18, "bold"), activebackground=cor_1)
        self.register_button.pack(pady=12)

        self.guest_login_button = tk.Button(self.frame, text="Return to Menu", height="1", width="12", command=self.logged_as_guest, bg=bg_2, fg=fg_1,
                  font=("Calibri", 18, "bold"), activebackground=cor_1)
        self.guest_login_button.pack(pady=(12,24))

        self.frame.pack()
    

    def login(self):
        # builds the login screen from the toplevel main screen
        # displays the information for the login screen and the general structure of the page
        # the entry values will be passed to the login_verify() function when the button is pressed
        self.login_screen = tk.Toplevel(self.frame)
        self.login_screen.title("Login")
        #self.login_screen.geometry("300x350")
        self.login_screen.configure(bg=bg_1)
        self.login_screen.resizable(False, False)

        self.login_title = tk.Label(self.login_screen, text="REVERSI", bg=bg_2, width="20", height="1", font=("Calibri", 24, "bold"),
                 fg=fg_1, borderwidth=4, relief="groove", pady="10")
        self.login_title.pack(pady=(0,8))

        self.login_prompt = tk.Label(self.login_screen, text="Please enter details below to login", font=("Calibri", 12), fg=fg_1,
                 bg=bg_1)
        self.login_prompt.pack(pady=8)

        self.username_verify_login = tk.StringVar()
        self.password_verify_login = tk.StringVar()

        self.username_label = tk.Label(self.login_screen, text="Username * ", font=("Calibri", 12), fg=fg_1, bg=bg_1)
        self.username_label.pack(pady=8)
        self.username_entry_login = tk.Entry(self.login_screen, textvariable=self.username_verify_login, bg=bg_2,
                                             fg=fg_1, font=("Calibri", 18, "bold"))
        self.username_entry_login.pack(pady=8)
        self.password_label = tk.Label(self.login_screen, text="Password * ", font=("Calibri", 12), fg=fg_1, bg=bg_1)
        self.password_label.pack(pady=8)
        self.password_entry_login = tk.Entry(self.login_screen, textvariable=self.password_verify_login, bg=bg_2,
                                             show="*", fg=fg_1, font=("Calibri", 18, "bold"))
        self.password_entry_login.pack(pady=8)

        self.login_button = tk.Button(self.login_screen, text="Login", width=12, height=1, fg=fg_1, bg=bg_2, font=("Calibri", 18, "bold"),
                  command=lambda: [self.remove_verify_text(), self.login_verify(), self.open_main()], activebackground=cor_1)
        self.login_button.pack(pady=(8, 24))


    def login_verify(self):
        # .gets() the entry values from login() for username and password
        # compares the vlaues to the database and displays either incorrect entry options
        # or calls login_success() if information is correct
        self.username_login = self.username_verify_login.get()
        self.password_login = self.password_verify_login.get()

        self.username_entry_login.delete(0, tk.END)
        self.password_entry_login.delete(0, tk.END)
        
        self.username_login_tuple = (self.username_login,)

        login = DatabaseLogin(self.username_login_tuple, self.password_login)
        login.connect_to_database()
        
        user_temp, self.master.logged_elo, self.master.matches_played, pass_temp = login.execute_query()


        if user_temp == 1:
            print("username found")
            self.master.user_logged_in.update_username(self.username_login)
            self.master.user_logged_in.update_elo(self.master.logged_elo)
            self.master.user_logged_in.update_matches(self.master.matches_played)
            if self.password_login == pass_temp:
                print("correct password")
                self.return_successful_login()
            else:
                self.result_label = tk.Label(self.login_screen, font=("Calibri", 12), fg='red', bg=bg_1,
                                             text="Password not recognized")
                self.result_label.pack()
        else:
            self.result_label = tk.Label(self.login_screen, font=("Calibri", 12), fg='red', bg=bg_1,
                                         text="User not found")
            self.result_label.pack()


    def return_successful_login(self):
        # When a successful login has been completed destroy all the windows on the screen
        # Print to the terminal that you have logged in
        self.master.logged_user = self.username_login
        #self.master.logged_elo = self.logged_user_elo
        self.master.change_username_label()

        self.login_screen.destroy()
        self.frame.destroy()
        self.master.deiconify()
        print('You have successfully logged in.')


    def register(self):
        # display the register page to the user and take in the variables from the username and password
        # entry fields. When button is pressed call the register function.
        self.register_screen = tk.Toplevel(self.frame)
        self.register_screen.title("Register")
        #self.register_screen.geometry("300x350")
        self.register_screen.configure(bg=bg_1)
        self.register_screen.resizable(False, False)

        self.register_title = tk.Label(self.register_screen, text="REVERSI", bg=bg_2, width="20", height="1", font=("Calibri", 24, "bold"),
                 fg=fg_1, borderwidth=4, relief="groove", pady="10")
        self.register_title.pack(pady=8)
        self.register_prompt = tk.Label(self.register_screen, text="Please enter details below", font=("Calibri", 12), fg=fg_1, bg=bg_1)
        self.register_prompt.pack(pady=8)

        self.username_register = tk.StringVar()
        self.password_register = tk.StringVar()

        self.username_label_register = tk.Label(self.register_screen, text="Username * ", font=("Calibri", 12), fg=fg_1, bg=bg_1)
        self.username_label_register.pack(pady=8)
        self.username_entry_register = tk.Entry(self.register_screen, textvariable=self.username_register, bg=bg_2,
                                                fg=fg_1, font=("Calibri", 18, "bold"))
        self.username_entry_register.pack(pady=8)
        self.password_label_register = tk.Label(self.register_screen, text="Password * ", font=("Calibri", 12), fg=fg_1, bg=bg_1)
        self.password_label_register.pack(pady=8)
        self.password_entry_register = tk.Entry(self.register_screen, textvariable=self.password_register, bg=bg_2,
                                                show="*", fg=fg_1, font=("Calibri", 18, "bold"))
        self.password_entry_register.pack(pady=8)

        self.register_button = tk.Button(self.register_screen, text="Register", width=12, height=1, fg=fg_1, bg=bg_2,
                  font=("Calibri", 18, "bold"), command=self.register_user, activebackground=cor_1)
        self.register_button.pack(pady=(8,24))


    def register_user(self):
        try:
            # my_conn = my_connect.cursor()
            # register a user into the database
            self.username_info = self.username_register.get()
            self.password_info = self.password_register.get()

            self.info_tuple = (self.username_info, self.password_info)

            register = DatabaseRegister(self.info_tuple)
            register.connect_to_database()
            register.execute_query()

            self.username_entry_register.delete(0, tk.END)
            self.password_entry_register.delete(0, tk.END)

            tk.Label(self.register_screen, text="Registration Successful", fg="green", font=("calibri", 11)).pack()

        except Error as e:
            print(e)


    def logged_as_guest(self):
        self.master.logged_user = "Guest"
        self.master.logged_elo = 0
        self.master.change_username_label()
        self.destroy()
        self.master.deiconify()
        print('You have successfully logged in as a guest.')


    def remove_verify_text(self):
        # function removes the text "Password not recognized" or "User not found"
        # if the login attempt is not the first attempt.
        # This is implemented so the lables do not stack upon each other at the bottom of the screen
        if not self.first_attempt:
            self.result_label.config(text="")
            self.result_label.after(0, self.result_label.destroy())
        self.first_attempt = False

    def open_main(self):
        self.destroy()
        self.master.deiconify()