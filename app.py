import tkinter as tk
from view.login_view import LoginView

bg_1 = "#E0FBFC"
bg_2 = "#C2DFE3"
cor_1 = "#9DB4C0"
incor_1 = "#5C6B73"
fg_1 = "#253237"


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Reversi')
        self.geometry('300x250')
        self.configure(bg=bg_1)

        # label
        title_label = tk.Label(text="REVERSI", bg=bg_2, width="300", height="1", font=("Calibri", 24, "bold"), fg=fg_1,
                               borderwidth=4, relief="groove", pady="10")
        title_label.pack()

    def open_login(self):
        login_win = LoginView(self)
        login_win.focus_force()
        self.withdraw()
