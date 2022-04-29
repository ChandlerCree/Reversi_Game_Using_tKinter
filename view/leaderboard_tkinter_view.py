import tkinter as tk
from tkinter import ttk
from controller.database.database_leaderboard import DatabaseLeaderboard


bg_1 = "#E0FBFC"
bg_2 = "#C2DFE3"
cor_1 = "#9DB4C0"
incor_1 = "#5C6B73"
fg_1 = "#253237"


class LeaderboardView(tk.Toplevel):
    """
    This gui view of the leaderboard
    """
    def __init__(self, parent):
        super().__init__(parent)

        '''self.my_connect = my_connect'''

        self.title('Reversi')
        self.resizable
        #self.geometry('300x350')
        self.configure(bg=bg_1)
        self.frame = tk.Frame(self)
        self.frame.configure(bg=bg_1)

        self.leaderboard_title = tk.Label(self.frame, text="Leaderboard", bg=bg_2, width="20", height="1",
                                          font=("Calibri", 24, "bold"), fg=fg_1, borderwidth=4, relief="groove",
                                          pady="10")
        self.leaderboard_title.pack(pady=(0,4))
        self.main_button = tk.Button(self.frame, text='Main Menu', command=self.open_main, bg=bg_2, 
                                    font=('Calibri', 12, "bold"), activebackground=cor_1)
        self.main_button.pack(pady=4)

        #style = ttk.Style()
        #style.configure("mystyle.Treeview", font=("Calibri", 12), bg=bg_1, fg=fg_1)
        #style.configure("mystyle.Treeview.Heading", font=("Calibri", 14, "Bold"))

        self.leaderboard = ttk.Treeview(self.frame) #, style="mystyle.Treeview"

        self.leaderboard['columns'] = ('rank', 'player_Name', 'elo')
        self.leaderboard.column("#0", width=0, stretch=False)
        self.leaderboard.column("rank", anchor=tk.CENTER, width=80)
        self.leaderboard.column("player_Name", anchor=tk.CENTER, width=80)
        self.leaderboard.column("elo", anchor=tk.CENTER, width=80)

        self.leaderboard.heading("#0", text="", anchor=tk.CENTER)
        self.leaderboard.heading("rank", text="Rank", anchor=tk.CENTER)
        self.leaderboard.heading("player_Name", text="Player Name", anchor=tk.CENTER)
        self.leaderboard.heading("elo", text="ELO", anchor=tk.CENTER)

        '''leaderboard_query = "Select username, elo from player order by elo desc limit 10;"

        with self.my_connect.cursor() as cursor:
            cursor.execute(leaderboard_query)
            result = cursor.fetchall()
            self.my_connect.commit()
            count = 0
            for row in result:
                self.leaderboard.insert(parent='', index='end', iid=count, text='',
                                values=(str(count + 1), str(row[0]), str(row[1])))
                count += 1
                print(row)'''

        leaderboard = DatabaseLeaderboard()
        leaderboard.connect_to_database()
        leaderboard_top_10 = leaderboard.execute_query()

        count = 0
        for row in leaderboard_top_10:
                self.leaderboard.insert(parent='', index='end', iid=count, text='',
                                values=(str(count + 1), str(row[0]), str(row[1])))
                count += 1
                print(row)

        '''self.leaderboard.insert(parent='', index='end', iid=0, text='',
                                values=('1', 'user1', '1500'))
        self.leaderboard.insert(parent='', index='end', iid=1, text='',
                                values=('2', 'user2', '1500'))
        self.leaderboard.insert(parent='', index='end', iid=2, text='',
                                values=('3', 'user3', '1500'))
        self.leaderboard.insert(parent='', index='end', iid=3, text='',
                                values=('4', 'user4', '1500'))
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
                                values=('10', 'john', '00'))'''

        self.leaderboard.pack(pady=14)
        # show the frame on the container
        self.frame.pack()

    def open_main(self):
        """
        This function closes this window and returns to the main menu
        :param
        :return
        """
        self.destroy()
        self.master.deiconify()
