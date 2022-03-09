import tkinter as tk

# from main_menu_view import MainMenu

bg_1 = "#E0FBFC"
bg_2 = "#C2DFE3"
cor_1 = "#9DB4C0"
incor_1 = "#5C6B73"
fg_1 = "#253237"


class SettingsView(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title('Reversi')
        self.geometry('300x350')
        self.configure(bg=bg_1)
        self.frame = tk.Frame(self)

        self.frame = tk.Frame(self)
        self.leaderboard_title = tk.Label(self.frame, text="Settings", bg=bg_2, width="300", height="1",
                                          font=("Calibri", 24, "bold"), fg=fg_1, borderwidth=4, relief="groove",
                                          pady="10")
        self.leaderboard_title.pack()
        self.main_button = tk.Button(self.frame, text='Main Menu', command=self.open_main)
        self.main_button.pack()

        self.p1_listbox_label = tk.Label(self.frame, text='Choose Player 1 Disk Color: ', font=('Calibri', 11))
        self.p1_listbox_label.pack()
        colors = ('Red', 'Green', 'Blue', 'Yellow', 'Purple')
        colors_var = tk.StringVar(value=colors)
        self.p1_listbox = tk.Listbox(self.frame, listvariable=colors_var, height='10')
        self.p1_listbox.pack()

        self.p1_listbox.bind('<<ListboxSelect>>', self.p1_color_selected)

        self.p2_listbox_label = tk.Label(self.frame, text='Choose Player 1 Disk Color: ', font=('Calibri', 11))
        self.p2_listbox_label.pack()
        colors = ('Red', 'Green', 'Blue', 'Yellow', 'Purple')
        colors_var = tk.StringVar(value=colors)
        self.p2_listbox = tk.Listbox(self.frame, listvariable=colors_var, height='10')
        self.p2_listbox.pack()

        self.p2_listbox.bind('<<ListboxSelect>>', self.p2_color_selected)

        self.board_size_label = tk.Label(self.frame,
                                         text='Please designate a board size: (An even number between 4-10) ',
                                         font=('Calibri', 11))
        self.board_size_label.pack()
        self.entry = tk.Entry(self.frame)
        self.entry.pack()
        self.board_size_button = tk.Button(self.frame, text='Enter', command=self.set_board_size)
        self.board_size_button.pack()

        # show the frame on the container
        self.frame.pack()

    def open_main(self):
        self.destroy()
        self.master.deiconify()

    def set_board_size(self):
        number = self.entry.get()
        self.master.board_size = int(number)
        self.entry.delete(0, 'end')

    def p1_color_selected(self, event):
        selected_index = self.p1_listbox.curselection()[0]
        color = self.p1_listbox.get(selected_index)
        self.master.p1=color

    def p2_color_selected(self, event):
        selected_index = self.p2_listbox.curselection()[0]
        color = self.p2_listbox.get(selected_index)
        self.master.p2=color



