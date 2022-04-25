import tkinter as tk

# from main_menu_view import MainMenu

bg_1 = "#E0FBFC"
bg_2 = "#C2DFE3"
cor_1 = "#9DB4C0"
incor_1 = "#5C6B73" 
fg_1 = "#253237"


class SettingsView(tk.Toplevel):
    color_p1_bool = False
    color_p2_bool = False
    board_size_bool = False
    ai_diff_bool = False

    def __init__(self, parent):
        super().__init__(parent)
        self.title('Reversi')
        #self.geometry('300x600')
        self.configure(bg=bg_1)
        self.resizable(False, False)
        self.frame = tk.Frame(self)

        # Settings Title
        self.frame = tk.Frame(self)
        self.frame.configure(bg=bg_1)
        self.leaderboard_title = tk.Label(self.frame, text="Game Settings", bg=bg_2, width="20", height="1",
                                          font=("Calibri", 24, "bold"), fg=fg_1, borderwidth=4, relief="groove",
                                          pady="10")
        self.leaderboard_title.pack(pady=(0,4))

        # Add a Button to return to the main menu
        self.main_button = tk.Button(self.frame, width="12", text='Main Menu', command=self.open_main, font=('Calibri', 14, "bold"), 
                                        bg=bg_2, fg=fg_1, activebackground=cor_1)
        self.main_button.pack(pady=(4,10))

        # Create a listbox for player 1's color
        self.p1_listbox_label = tk.Label(self.frame, text='Choose Player 1 Disk Color: ', font=('Calibri', 12, "bold"), bg=bg_1, fg=fg_1)
        self.p1_listbox_label.pack(pady=4)
        colors = ('Red', 'Green', 'Blue', 'Yellow', 'Purple')
        colors_var = tk.StringVar(value=colors)
        self.p1_listbox = tk.Listbox(self.frame, listvariable=colors_var, height='5', exportselection=False, bg=bg_2, fg=fg_1, justify="center")
        self.p1_listbox.pack(pady=(0,8))

        self.p1_listbox.bind('<<ListboxSelect>>', self.p1_color_selected)

        # Create a listbox for player 2's color
        self.p2_listbox_label = tk.Label(self.frame, text='Choose Player 2 Disk Color: ', font=('Calibri', 12, "bold"), bg=bg_1, fg=fg_1)
        self.p2_listbox_label.pack(pady=4)
        colors = ('Red', 'Green', 'Blue', 'Yellow', 'Purple')
        colors_var = tk.StringVar(value=colors)
        self.p2_listbox = tk.Listbox(self.frame, listvariable=colors_var, height='5', exportselection=False, bg=bg_2, fg=fg_1, justify="center")
        self.p2_listbox.pack(pady=(0,8))

        self.p2_listbox.bind('<<ListboxSelect>>', self.p2_color_selected)

        self.boardsize_info = tk.Label(self.frame, text="Choose the board size!", font=("Calibri", 12, "bold"), bg=bg_1, fg=fg_1)
        self.boardsize_info.pack(pady=(8,0))

        self.rdobtn_lblframe = tk.Frame(self.frame)
        self.rdobtn_lblframe.configure(bg=bg_1)
        self.rdobtn_frame = tk.Frame(self.frame)
        self.rdobtn_frame.configure(bg=bg_1)

        self.boardsize_4 = tk.Label(self.rdobtn_lblframe, text="4x4", font=("Calibri"), bg=bg_1, fg=fg_1)
        self.boardsize_6 = tk.Label(self.rdobtn_lblframe, text="6x6", font=("Calibri"), bg=bg_1, fg=fg_1)
        self.boardsize_8 = tk.Label(self.rdobtn_lblframe, text="8x8", font=("Calibri"), bg=bg_1, fg=fg_1)
        self.boardsize_10 = tk.Label(self.rdobtn_lblframe, text="10x10", font=("Calibri"), bg=bg_1, fg=fg_1)

        self.board_size_temp = tk.IntVar()

        self.radiobttn_4 = tk.Radiobutton(self.rdobtn_lblframe, variable=self.board_size_temp, value=4, bg=bg_1, command=self.set_board_sizez)
        self.radiobttn_6 = tk.Radiobutton(self.rdobtn_lblframe, variable=self.board_size_temp, value=6, bg=bg_1, command=self.set_board_sizez)
        self.radiobttn_8 = tk.Radiobutton(self.rdobtn_lblframe, variable=self.board_size_temp, value=8, bg=bg_1, command=self.set_board_sizez)
        self.radiobttn_10 = tk.Radiobutton(self.rdobtn_lblframe, variable=self.board_size_temp, value=10, bg=bg_1, command=self.set_board_sizez)

        self.boardsize_4.grid(row=0, column=0)
        self.boardsize_6.grid(row=0, column=1)
        self.boardsize_8.grid(row=0, column=2)
        self.boardsize_10.grid(row=0, column=3)

        self.radiobttn_4.grid(row=1, column=0, padx=(8,0))
        self.radiobttn_6.grid(row=1, column=1, padx=(8,0))
        self.radiobttn_8.grid(row=1, column=2, padx=(8,0))
        self.radiobttn_10.grid(row=1, column=3, padx=(8,0))

        self.rdobtn_aidifflbl = tk.Frame(self.frame)
        self.rdobtn_aidifflbl.configure(bg=bg_1)
        self.rdobtn_aidiffframe = tk.Frame(self.frame)
        self.rdobtn_aidiffframe.configure(bg=bg_1)

        self.aidiff_easy = tk.Label(self.rdobtn_aidifflbl, text="Easy", font=("Calibri"), bg=bg_1, fg=fg_1)
        self.aidiff_medium = tk.Label(self.rdobtn_aidifflbl, text="Medium", font=("Calibri"), bg=bg_1, fg=fg_1)
        self.aidiff_hard = tk.Label(self.rdobtn_aidifflbl, text="Hard", font=("Calibri"), bg=bg_1, fg=fg_1)
        self.aidiff_expert = tk.Label(self.rdobtn_aidifflbl, text="Expert", font=("Calibri"), bg=bg_1, fg=fg_1)

        self.ai_difficulty_level = tk.IntVar()

        self.radiobttn_easy = tk.Radiobutton(self.rdobtn_aidiffframe, variable=self.ai_difficulty_level, value=2, bg=bg_1, command=self.set_ai_difficulty)
        self.radiobttn_medium = tk.Radiobutton(self.rdobtn_aidiffframe, variable=self.ai_difficulty_level, value=3, bg=bg_1, command=self.set_ai_difficulty)
        self.radiobttn_hard = tk.Radiobutton(self.rdobtn_aidiffframe, variable=self.ai_difficulty_level, value=4, bg=bg_1, command=self.set_ai_difficulty)
        self.radiobttn_expert = tk.Radiobutton(self.rdobtn_aidiffframe, variable=self.ai_difficulty_level, value=5, bg=bg_1, command=self.set_ai_difficulty)

        self.aidiff_easy.grid(row=0, column=0)
        self.aidiff_medium.grid(row=0, column=1)
        self.aidiff_hard.grid(row=0, column=2)
        self.aidiff_expert.grid(row=0, column=3)

        self.radiobttn_easy.grid(row=1, column=0, padx=(8,0))
        self.radiobttn_medium.grid(row=1, column=1, padx=(8,0))
        self.radiobttn_hard.grid(row=1, column=2, padx=(8,0))
        self.radiobttn_expert.grid(row=1, column=3, padx=(8,0))


        self.rdobtn_lblframe.pack() 
        self.rdobtn_frame.pack()
        self.rdobtn_aidifflbl.pack()
        self.rdobtn_aidiffframe.pack()

        # Submit button for board size entry
        self.board_size_button = tk.Button(self.frame, width="6", text='Apply', command=lambda: [self.open_main(), 
                                                                        self.master.change_newgame_state()], font=('Calibri', 14, "bold"), 
                                                                        bg=bg_2, fg=fg_1, activebackground=cor_1, state='disabled')
        
        self.board_size_button.pack(pady=(4,12))

        # show the frame on the container
        self.frame.pack()

    def open_main(self):
        self.destroy()
        self.master.deiconify()

    def set_board_sizez(self):
        self.master.board_size = self.board_size_temp.get()
        self.board_size_bool = True
        self.enable_apply()
        #print(str(self.board_size_bool) + "size=true")
        print("Board size selected = " + str(self.master.board_size))

    def set_ai_difficulty(self):
        self.master.ai_difficulty = self.ai_difficulty_level.get()
        self.ai_diff_bool = True
        self.enable_apply()
        print("AI difficulty level selected = " + str(self.master.ai_difficulty))


    '''    def set_board_size(self):
        #number = self.entry.get()
        #self.master.board_size = int(number)
        #self.entry.delete(0, 'end')
        pass'''

    def p1_color_selected(self, event):
        selected_index = self.p1_listbox.curselection()[0]
        color = self.p1_listbox.get(selected_index)
        self.master.p1 = color
        self.color_p1_bool = True
        self.enable_apply()
        print(str(self.color_p1_bool) + "p1=true")

    def p2_color_selected(self, event):
        selected_index = self.p2_listbox.curselection()[0]
        color = self.p2_listbox.get(selected_index)
        self.master.p2 = color
        self.color_p2_bool = True
        self.enable_apply()
        print(str(self.color_p2_bool) + "p2=true")

    def enable_apply(self):
        print(self.color_p1_bool, self.color_p2_bool, self.board_size_bool, self.ai_diff_bool)
        if self.color_p1_bool and self.color_p2_bool and self.board_size_bool == True and self.ai_diff_bool == True:
            print(self.master.p1 + self.master.p2)
            if self.master.p1 != self.master.p2:          
                self.board_size_button.configure(state='normal')
            else:
                self.board_size_button.configure(state='disable')