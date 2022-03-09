import os
import tkinter as tk
from tkinter import ttk
from mysql.connector import connect, Error
from getpass import getpass
import tkinter as tk

bg_1 = "#E0FBFC"
bg_2 = "#C2DFE3"
cor_1 = "#9DB4C0"
incor_1 = "#5C6B73"
fg_1 = "#253237"


class LoginView(tk.Toplevel):
    def __init__(self, parent, my_connect):
        super().__init__(parent)

        # init function called when new object LoginView is created
        self.first_attempt = True
        self.successful_login = False
        self.my_connect = my_connect

        
        self.geometry("300x350")
        self.title("Reversi")
        self.configure(bg=bg_1)
        #self.resizable(False, False)
        self.frame = tk.Frame(self)
        self.login_title = tk.Label(self.frame, text="REVERSI", bg=bg_2, width="300", height="1", font=("Calibri", 24, "bold"), fg=fg_1, borderwidth=4,
                 relief="groove", pady="10")
        self.login_title.pack()
        self.spacer_1 = tk.Label(self.frame, text="", height="2", bg=bg_1, font=("Calibri", 6))
        self.spacer_1.pack()
        self.login_button = tk.Button(self.frame, text="Login", height="1", width="12", command=self.login, bg=bg_2, fg=fg_1,
                  font=("Calibri", 18, "bold"), activebackground=cor_1)
        self.login_button.pack()
        self.spacer_2 = tk.Label(self.frame, text="", height="2", bg=bg_1, font=("Calibri", 6))
        self.spacer_2.pack()
        self.register_button = tk.Button(self.frame, text="Register", height="1", width="12", command=self.register, bg=bg_2, fg=fg_1,
                  font=("Calibri", 18, "bold"), activebackground=cor_1)
        self.register_button.pack()
        self.spacer_3 = tk.Label(self.frame, text="", height="2", bg=bg_1, font=("Calibri", 6))
        self.spacer_3.pack()
        self.guest_login_button = tk.Button(self.frame, text="Guest Login", height="1", width="12", command=self.logged_as_guest, bg=bg_2, fg=fg_1,
                  font=("Calibri", 18, "bold"), activebackground=cor_1)
        self.guest_login_button.pack()

        self.frame.pack()
    '''
    def login_control(self, connector):
        successful_login = False
        self.main_screen()
        return successful_login
        '''

    '''def main_screen(self):
        # Builds the main screen of the game displaying to the user the graphics
        # two labels and buttons are created and display the user with otpions for
        # loging in or registering a new user
        self.entry_login_screen = tk.Tk()
        self.entry_login_screen.geometry("300x350")
        self.entry_login_screen.title("Reversi")
        self.entry_login_screen.configure(bg=bg_1)
        self.entry_login_screen.resizable(False, False)
        tk.Label(text="REVERSI", bg=bg_2, width="300", height="1", font=("Calibri", 24, "bold"), fg=fg_1, borderwidth=4,
                 relief="groove", pady="10").pack()
        tk.Label(text="", height="2", bg=bg_1, font=("Calibri", 6)).pack()
        tk.Button(text="Login", height="1", width="12", command=self.login, bg=bg_2, fg=fg_1,
                  font=("Calibri", 18, "bold"), activebackground=cor_1).pack()
        tk.Label(text="", height="2", bg=bg_1, font=("Calibri", 6)).pack()
        tk.Button(text="Register", height="1", width="12", command=self.register, bg=bg_2, fg=fg_1,
                  font=("Calibri", 18, "bold"), activebackground=cor_1).pack()
        tk.Label(text="", height="2", bg=bg_1, font=("Calibri", 6)).pack()
        tk.Button(text="Guest Login", height="1", width="12", command=self.logged_as_guest, bg=bg_2, fg=fg_1,
                  font=("Calibri", 18, "bold"), activebackground=cor_1).pack()

        self.entry_login_screen.mainloop()
        return self.successful_login'''

    def login(self):
        # builds the login screen from the toplevel main screen
        # displays the information for the login screen and the general structure of the page
        # the entry values will be passed to the login_verify() function when the button is pressed
        self.login_screen = tk.Toplevel(self.frame)
        self.login_screen.title("Login")
        self.login_screen.geometry("300x350")
        self.login_screen.configure(bg=bg_1)
        tk.Label(self.login_screen, text="REVERSI", bg=bg_2, width="300", height="1", font=("Calibri", 24, "bold"),
                 fg=fg_1, borderwidth=4, relief="groove", pady="10").pack()
        tk.Label(self.login_screen, text="", height="2", bg=bg_1, font=("Calibri", 2)).pack()
        tk.Label(self.login_screen, text="Please enter details below to login", font=("Calibri", 12), fg=fg_1,
                 bg=bg_1).pack()
        tk.Label(self.login_screen, text="", height="2", bg=bg_1, font=("Calibri", 2)).pack()

        self.username_verify_login = tk.StringVar()
        self.password_verify_login = tk.StringVar()

        tk.Label(self.login_screen, text="Username * ", font=("Calibri", 12), fg=fg_1, bg=bg_1).pack()
        self.username_entry_login = tk.Entry(self.login_screen, textvariable=self.username_verify_login, bg=bg_2,
                                             fg=fg_1, font=("Calibri", 18, "bold"))
        self.username_entry_login.pack()
        tk.Label(self.login_screen, text="Password * ", font=("Calibri", 12), fg=fg_1, bg=bg_1).pack()
        self.password_entry_login = tk.Entry(self.login_screen, textvariable=self.password_verify_login, bg=bg_2,
                                             show="*", fg=fg_1, font=("Calibri", 18, "bold"))
        self.password_entry_login.pack()

        tk.Label(self.login_screen, text="", bg=bg_1).pack()
        tk.Button(self.login_screen, text="Login", width=12, height=1, fg=fg_1, bg=bg_2, font=("Calibri", 18, "bold"),
                  command=lambda: [self.remove_verify_text(), self.login_verify()]).pack()

    def login_verify(self):
        # .gets() the entry values from login() for username and password
        # compares the vlaues to the database and displays either incorrect entry options
        # or calls login_success() if information is correct
        self.username_login = self.username_verify_login.get()
        self.password_login = self.password_verify_login.get()

        self.username_entry_login.delete(0, tk.END)
        self.password_entry_login.delete(0, tk.END)

        # quer = []
        # some query here that check blah
        # quer = "Select from *" # full list of users

        quer_user = "SELECT COUNT(1) FROM player WHERE username = '{}'".format(self.username_login)
        quer_pass = "SELECT password FROM player WHERE username = '{}'".format(self.username_login)

        print(quer_user)

        with self.my_connect.cursor(buffered=True) as cursor:
            cursor.execute(quer_user)
            result = cursor.fetchall()
            for row in result:
                user_temp = row[0]

        with self.my_connect.cursor(buffered=True) as cursor:
            cursor.execute(quer_pass)
            result = cursor.fetchall()
            for row in result:
                pass_temp = row[0]

        if user_temp == 1:
            print("username found")
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

    '''
    def login_success(self):
        #Displays the screen if a successful login has been completed. When the ok button is clicked
        #the return_successful_login() function is called. ###change this when finished
        self.login_success_screen = tk.Toplevel(self.entry_login_screen)
        self.login_success_screen.title("Success")
        self.login_success_screen.geometry("150x100")
        tk.Label(self.login_success_screen, text="Login Success").pack()
        tk.Button(self.login_success_screen, text="OK", command=self.return_successful_login).pack()
        #TODO need to connect to main screen of game when successful login
    '''

    def return_successful_login(self):
        # When a successful login has been completed destroy all the windows on the screen
        # Print to the terminal that you have logged in
        self.login_screen.destroy()
        self.frame.destroy()
        self.master.deiconify()
        print('You have successfully logged in.')
        self.successful_login = True

    def register(self):
        # display the register page to the user and take in the variables from the username and password
        # entry fields. When button is pressed call the register function.
        self.register_screen = tk.Toplevel(self.frame)
        self.register_screen.title("Register")
        self.register_screen.geometry("300x350")
        self.register_screen.configure(bg=bg_1)

        tk.Label(self.register_screen, text="REVERSI", bg=bg_2, width="300", height="1", font=("Calibri", 24, "bold"),
                 fg=fg_1, borderwidth=4, relief="groove", pady="10").pack()
        tk.Label(self.register_screen, text="", height="2", bg=bg_1, font=("Calibri", 2)).pack()
        tk.Label(self.register_screen, text="Please enter details below", font=("Calibri", 12), fg=fg_1, bg=bg_1).pack()
        tk.Label(self.register_screen, text="", height="2", bg=bg_1, font=("Calibri", 2)).pack()

        self.username_register = tk.StringVar()
        self.password_register = tk.StringVar()

        tk.Label(self.register_screen, text="Username * ", font=("Calibri", 12), fg=fg_1, bg=bg_1).pack()
        self.username_entry_register = tk.Entry(self.register_screen, textvariable=self.username_register, bg=bg_2,
                                                fg=fg_1, font=("Calibri", 18, "bold"))
        self.username_entry_register.pack()
        tk.Label(self.register_screen, text="Password * ", font=("Calibri", 12), fg=fg_1, bg=bg_1).pack()
        self.password_entry_register = tk.Entry(self.register_screen, textvariable=self.password_register, bg=bg_2,
                                                show="*", fg=fg_1, font=("Calibri", 18, "bold"))
        self.password_entry_register.pack()

        tk.Label(self.register_screen, text="", bg=bg_1).pack()
        tk.Button(self.register_screen, text="Register", width=12, height=1, fg=fg_1, bg=bg_2,
                  font=("Calibri", 18, "bold"), command=self.register_user).pack()

    def register_user(self):
        try:
            # my_conn = my_connect.cursor()
            # register a user into the database
            self.username_info = self.username_register.get()
            self.password_info = self.password_register.get()

            print("insert into player (username, password, elo) values ('{}', '{}', 1500);".format(self.username_info,
                                                                                                   self.password_info))
            quer = "insert into player (username, password, elo) values ('{}', '{}', 1500);".format(self.username_info,
                                                                                                    self.password_info)

            with self.my_connect.cursor() as cursor:
                cursor.execute(quer)
                result = cursor.fetchall()
                self.my_connect.commit()
                for row in result:
                    print(row)

            # insert into player (username, password, elo) values (usernameInput, passwordInput, 1500);

            self.username_entry_register.delete(0, tk.END)
            self.password_entry_register.delete(0, tk.END)

            tk.Label(self.register_screen, text="Registration Successful", fg="green", font=("calibri", 11)).pack()

        except Error as e:
            print(e)

    def logged_as_guest(self):
        # self.login_screen.destroy()
        self.entry_login_screen.destroy()
        print('You have successfully logged in as a guest.')
        self.successful_login = 'guest'

    def remove_verify_text(self):
        # function removes the text "Password not recognized" or "User not found"
        # if the login attempt is not the first attempt.
        # This is implemented so the lables do not stack upon each other at the bottom of the screen
        if not self.first_attempt:
            self.result_label.config(text="")
            self.result_label.after(0, self.result_label.destroy())
        self.first_attempt = False
