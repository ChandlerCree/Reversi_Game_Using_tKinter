import tkinter as tk
#from main_menu_view import MainMenu

bg_1 = "#E0FBFC"
bg_2 = "#C2DFE3"
cor_1 = "#9DB4C0"
incor_1 = "#5C6B73"
fg_1 = "#253237"


class SettingsView(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title('Reversi')
        self.geometry('300x250')
        self.configure(bg=bg_1)
        self.frame = tk.Frame(self)

        self.frame = tk.Frame(self)
        self.leaderboard_title = tk.Label(self.frame, text="Settings", bg=bg_2, width="300", height="1",
                                          font=("Calibri", 24, "bold"), fg=fg_1, borderwidth=4, relief="groove",
                                          pady="10")
        self.leaderboard_title.pack()
        self.main_button = tk.Button(self.frame, text='Main Menu', command=self.open_main)
        self.main_button.pack()

        self.label = tk.Label(self.frame, text='Choose Disk Color: ', font=('Calibri', 11))
        self.label.pack()
        colors = ('Red', 'Green', 'Blue', 'Yellow', 'Purple')
        colors_var = tk.StringVar(value=colors)
        self.listbox = tk.Listbox(self.frame, listvariable=colors_var)
        self.listbox.pack()

        # show the frame on the container
        self.frame.pack()

    def open_main(self):
        self.destroy()
        self.master.deiconify()
