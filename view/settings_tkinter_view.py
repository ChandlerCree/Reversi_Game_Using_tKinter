import tkinter as tk
from main_menu_view import MainMenu

bg_1 = "#E0FBFC"
bg_2 = "#C2DFE3"
cor_1 = "#9DB4C0"
incor_1 = "#5C6B73"
fg_1 = "#253237"


class SettingsView(tk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.label = tk.Label(text='Settings', font=('Calibri Bold', 50))
        self.label.pack()
        self.main_button = tk.Button(text='Main Menu', command=self.open_main)
        self.main_button.pack()

        self.label = tk.Label(text='Choose Disk Color: ', font=('Calibri', 11))
        self.label.pack()
        colors = ('Red', 'Green', 'Blue', 'Yellow', 'Purple')
        colors_var = tk.StringVar(value=colors)
        self.listbox = tk.Listbox(listvariable=colors_var)
        self.listbox.pack()

        # show the frame on the container
        self.pack()

    def open_main(self):
        main_win = MainMenu(self)
        main_win.focus_force()
        self.withdraw()
