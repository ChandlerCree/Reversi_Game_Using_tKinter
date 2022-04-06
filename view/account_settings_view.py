import tkinter as tk
from tkinter import messagebox

from numpy import delete
from controller.database.database_delete import DatabaseDelete

# from main_menu_view import MainMenu

bg_1 = "#E0FBFC"
bg_2 = "#C2DFE3"
cor_1 = "#9DB4C0"
incor_1 = "#5C6B73"
fg_1 = "#253237"

class AccountSettingsView(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title('Reversi')
        self.configure(bg=bg_1)
        self.resizable(False, False)
        self.frame = tk.Frame(self)

        self.frame.configure(bg=bg_1)
        self.leaderboard_title = tk.Label(self.frame, text="Account Settings", bg=bg_2, width="20", height="1",
                                          font=("Calibri", 24, "bold"), fg=fg_1, borderwidth=4, relief="groove",
                                          pady="10")
        self.leaderboard_title.pack()

        self.main_button = tk.Button(self.frame, width="12", text='Main Menu', command=self.open_main, font=('Calibri', 18, "bold"), 
                                        bg=bg_2, fg=fg_1, activebackground=cor_1)
        self.main_button.pack(pady=8)

        self.delete_caution = tk.Label(self.frame, text="If you would like to delete your account\ntype your username below and press\n'Delete Account'\nNote this is a permanent action\n and all accountinformation\nwill be lost",
                                            bg=bg_1, fg='red', font=("Calibri", 12, 'bold italic'))
        self.delete_caution.pack(pady=8)

        self.username_entry = tk.StringVar()

        self.username_confirmation = tk.Entry(self.frame, width="16", textvariable=self.username_entry, bg=bg_2, fg='red', font=("Calibri", 16))
        self.username_confirmation.pack(pady=8)

        self.username_confirmation.insert(0, 'username')

        self.delete_account_button = tk.Button(self.frame, width = "12", text='Delete Account', command=self.delete_account, font=('Calibri', 18, 'bold'),
                                        bg=bg_2, fg='red', activebackground=cor_1)
        self.delete_account_button.pack(pady=(8,16))

        self.frame.pack()

    
    def open_main(self):
        self.destroy()
        self.master.deiconify()

    
    def delete_account(self):
        self.username = self.username_entry.get()

        if self.username == self.master.logged_user:
            delete_user = DatabaseDelete(self.username)
            delete_user.connect_to_database()
            delete_user.execute_query()

            print("successfullly deleted account")
            self.master.logged_user = 'Guest'
            self.master.logged_elo = 0
            self.master.matches_played = 0
            self.master.user_logged_in.update_username(self.master.logged_user)
            self.master.user_logged_in.update_elo(self.master.logged_elo)
            self.master.user_logged_in.update_matches(self.master.matches_played)
            self.master.change_username_label()

            messagebox.showerror(title="Account Deleted", message="Account Deleted Successfully.")

            self.destroy()
            self.master.deiconify()




