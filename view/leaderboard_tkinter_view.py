import tkinter as tk
from tkinter import ttk
from main_menu import MainMenu

bg_1 = "#E0FBFC"
bg_2 = "#C2DFE3"
cor_1 = "#9DB4C0"
incor_1 = "#5C6B73"
fg_1 = "#253237"


class LeaderboardView(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.leaderboard_title = tk.Label(text="Leaderboard", bg=bg_2, width="300", height="1",
                                          font=("Calibri", 11, "bold"), fg=fg_1, borderwidth=4, relief="groove",
                                          pady="10")
        self.leaderboard_title.pack()
        self.main_button = tk.Button(text='Main Menu', command=self.button_main)
        self.main_button.pack()

        self.leaderboard = ttk.Treeview()

        self.leaderboard['columns'] = ('rank', 'player_Name', 'elo')
        self.leaderboard.column("#0", width=0, stretch=False)
        self.leaderboard.column("rank", anchor=tk.CENTER, width=80)
        self.leaderboard.column("player_Name", anchor=tk.CENTER, width=80)
        self.leaderboard.column("elo", anchor=tk.CENTER, width=80)

        self.leaderboard.heading("#0", text="", anchor=tk.CENTER)
        self.leaderboard.heading("rank", text="Rank", anchor=tk.CENTER)
        self.leaderboard.heading("player_Name", text="Player Name", anchor=tk.CENTER)
        self.leaderboard.heading("elo", text="ELO", anchor=tk.CENTER)

        self.leaderboard.insert(parent='', index='end', iid=0, text='',
                                values=('1', 'john', '00'))
        self.leaderboard.insert(parent='', index='end', iid=1, text='',
                                values=('2', 'john', '00'))
        self.leaderboard.insert(parent='', index='end', iid=2, text='',
                                values=('3', 'john', '00'))
        self.leaderboard.insert(parent='', index='end', iid=3, text='',
                                values=('4', 'john', '00'))
        self.leaderboard.insert(parent='', index='end', iid=4, text='',
                                values=('5', 'john', '00'))
        self.leaderboard.insert(parent='', index='end', iid=5, text='',
                                values=('6', 'john', '00'))
        self.leaderboard.insert(parent='', index='end', iid=6, text='',
                                values=('7', 'john', '00'))
        self.leaderboard.insert(parent='', index='end', iid=7, text='',
                                values=('8', 'john', '00'))
        self.leaderboard.insert(parent='', index='end', iid=8, text='',
                                values=('9', 'john', '00'))
        self.leaderboard.insert(parent='', index='end', iid=9, text='',
                                values=('10', 'john', '00'))

        self.leaderboard.pack()
        # show the frame on the container
        self.pack()

    def button_main(self):
        button_clicked_label = tk.Label(text="button clicked", bg=bg_2, width="300", height="1",
                                        font=("Calibri", 11, "bold"), fg=fg_1, borderwidth=4, relief="groove",
                                        pady="10")
        button_clicked_label.pack()
