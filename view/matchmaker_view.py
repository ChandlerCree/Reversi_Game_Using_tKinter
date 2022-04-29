import tkinter as tk
from tkinter import ttk
from controller.database.database_leaderboard import DatabaseLeaderboard
from tkinter import messagebox

bg_1 = "#E0FBFC"
bg_2 = "#C2DFE3"
cor_1 = "#9DB4C0"
incor_1 = "#5C6B73"
fg_1 = "#253237"
font = "Calibri"


class MatchmakerView(tk.Toplevel):
    """
    This class is a tkinter gui that displays a table of player data for choosing an opponent to challenge
    """

    def __init__(self, parent):
        super().__init__(parent)
        self.title('Reversi')
        self.configure(bg=bg_1)
        self.resizable(False, False)
        self.frame = tk.Frame(self)

        # Set up a frame title
        self.frame = tk.Frame(self)
        self.frame.configure(bg=bg_1)
        self.leaderboard_title = tk.Label(self.frame, text="Find an Opponent", bg=bg_2, width="20", height="1",
                                          font=(font, 24, "bold"), fg=fg_1, borderwidth=4, relief="groove",
                                          pady="10")
        self.leaderboard_title.pack(pady=(0, 4))

        # Add a Button to return to the main menu
        self.main_button = tk.Button(self.frame, width="12", text='Main Menu', command=self.open_main,
                                     font=(font, 14, "bold"),
                                     bg=bg_2, fg=fg_1, activebackground=cor_1)
        self.main_button.pack(pady=(4, 10))

        self.leaderboard = ttk.Treeview(self.frame)  # , style="mystyle.Treeview"

        self.leaderboard['columns'] = ('rank', 'player_Name', 'elo')
        self.leaderboard.column("#0", width=0, stretch=False)
        self.leaderboard.column("rank", anchor=tk.CENTER, width=80)
        self.leaderboard.column("player_Name", anchor=tk.CENTER, width=80)
        self.leaderboard.column("elo", anchor=tk.CENTER, width=80)

        self.leaderboard.heading("#0", text="", anchor=tk.CENTER)
        self.leaderboard.heading("rank", text="Rank", anchor=tk.CENTER)
        self.leaderboard.heading("player_Name", text="Player Name", anchor=tk.CENTER)
        self.leaderboard.heading("elo", text="ELO", anchor=tk.CENTER)

        leaderboard = DatabaseLeaderboard()
        leaderboard.connect_to_database()
        leaderboard_top_10 = leaderboard.execute_query()

        count = 0
        for row in leaderboard_top_10:
            self.leaderboard.insert(parent='', index='end', iid=count, text='',
                                    values=(str(count + 1), str(row[0]), str(row[1])))
            count += 1

        self.leaderboard.bind("<<TreeviewSelect>>", self.on_double_click)
        self.leaderboard.pack(pady=14)
        # show the frame on the container
        self.frame.pack()

        # Add a Button to start a game
        self.main_button = tk.Button(self.frame, width="12", text='Start Game', command=self.open_online,
                                     font=(font, 14, "bold"),
                                     bg=bg_2, fg=fg_1, activebackground=cor_1)
        self.main_button.pack(pady=(4, 10))

        # show the frame on the container
        self.frame.pack()

    def open_main(self):
        """
        This function destroys the current window and reopens the main menu
        :param
        :return
        """
        self.destroy()  # close this frame
        self.master.deiconify()  # open the minimized main menu

    def open_online(self):
        """
        This function calls the open online game from the app class while closing this window.
        :param
        :return
        """
        self.destroy()  # close this frame
        self.master.open_online_game()  # open the online game screen from the main menu

    def on_double_click(self, event):
        """
        This function allows the user to challenge an opponent when an item in the Treeview is double clicked. The
        user then has a messagebox pop up to confirm that they would like to challenge.
        :param event - in this case it would be a double click on the listbox
        :return
        """
        item = self.leaderboard.selection()[0]
        print("you clicked on", self.leaderboard.item(item))
        response = messagebox.askquestion('Challenge', 'Do you want to challenge?')
        if response == 'yes':
            print('Send challenge')
