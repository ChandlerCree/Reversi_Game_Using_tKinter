import os
import mysql.connector
import tkinter as tk


class LoginView():
    def __init__(self):
        self.first_attempt = True
        self.successful_login = False

    def register_user(self):
        username_info = self.username_register.get()
        password_info = self.password_register.get()

        file = open("temp_accounts/"+username_info, "w")
        file.write(username_info + "\n")
        file.write(password_info)
        file.close

        self.username_entry_register.delete(0, tk.END)
        self.password_entry_register.delete(0, tk.END)

        tk.Label(self.register_screen, text = "Registration Successful", fg = "green", font = ("calibri", 11)).pack()

    def register(self):
        self.register_screen = tk.Toplevel(self.entry_login_screen)
        self.register_screen.title("Register")
        self.register_screen.geometry("300x250")

        self.username_register = tk.StringVar()
        self.password_register = tk.StringVar()
        
        tk.Label(self.register_screen, text = "Please enter details below").pack()
        
        tk.Label(self.register_screen, text = "").pack()

        tk.Label(self.register_screen, text = "Username * ").pack()
        self.username_entry_register = tk.Entry(self.register_screen, textvariable = self.username_register)
        self.username_entry_register.pack()
        tk.Label(self.register_screen, text = "Password * ").pack()
        self.password_entry_register = tk.Entry(self.register_screen, textvariable = self.password_register)
        self.password_entry_register.pack()

        tk.Button(self.register_screen, text = "Register", width = 10, height = 1, command = self.register_user).pack()

    def remove_verify_text(self):
        if not self.first_attempt:
            self.result_label.config(text= "")
            self.result_label.after(0, self.result_label.destroy())
        self.first_attempt = False

    def login_verify(self):
        username_login = self.username_verify_login.get()
        password_login = self.password_verify_login.get()

        self.username_entry_login.delete(0, tk.END)
        self.password_entry_login.delete(0, tk.END)
        

        list_of_files = os.listdir("temp_accounts/")
        if username_login in list_of_files:
            file1 = open("temp_accounts/" + username_login, "r")
            verify = file1.read().splitlines()
            if password_login in verify:
                self.login_success()
            else:
                self.result_label = tk.Label(self.login_screen, text = "Password not recognized")
                self.result_label.pack()
            
        else:
            self.result_label = tk.Label(self.login_screen, text = "User not found")
            self.result_label.pack()

    def login_success(self):
        self.login_success_screen = tk.Toplevel(self.entry_login_screen)
        self.login_success_screen.title("Success")
        self.login_success_screen.geometry("150x100")
        tk.Label(self.login_success_screen, text = "Login Success").pack()
        tk.Button(self.login_success_screen, text = "OK", command = self.return_successful_login).pack()

    def return_successful_login(self):
        self.login_success_screen.destroy()
        self.login_screen.destroy()
        self.entry_login_screen.destroy()
        print('You have successfully logged in.')
        self.successful_login = True



    def login(self):
        self.login_screen = tk.Toplevel(self.entry_login_screen)
        self.login_screen.title("Login")
        self.login_screen.geometry("300x250")
        tk.Label(self.login_screen, text = "Please enter details below to login").pack()
        tk.Label(self.login_screen, text = "").pack()
        
        #global username_verify_login
        #global password_verify_login
        #global username_entry_login
        #global password_entry_login

        self.username_verify_login = tk.StringVar()
        self.password_verify_login = tk.StringVar()

        tk.Label(self.login_screen, text = "Username * ").pack()
        self.username_entry_login = tk.Entry(self.login_screen, textvariable = self.username_verify_login)
        self.username_entry_login.pack()
        tk.Label(self.login_screen, text = "Password * ").pack()
        self.password_entry_login = tk.Entry(self.login_screen, textvariable = self.password_verify_login)
        self.password_entry_login.pack()

        tk.Label(self.login_screen, text = "").pack()
        tk.Button(self.login_screen, text = "Login", width = 10, height = 1, command = lambda:[self.remove_verify_text(), self.login_verify()]).pack()
    
    def main_screen(self):
        self.entry_login_screen = tk.Tk()
        self.entry_login_screen.geometry("300x250")
        self.entry_login_screen.title("Reversi")
        tk.Label(text = "Reversi", bg = "grey", width = "300", height = "2", font = ("Calibri", 13)).pack()
        tk.Label(text = "").pack()
        tk.Button(text = "Login", height = "2", width = "30", command = self.login).pack()
        tk.Label(text = "").pack()
        tk.Button(text = "Register", height = "2", width = "30", command = self.register).pack()

        self.entry_login_screen.mainloop()
        return self.successful_login