import tkinter as tk

bg_1 = "#E0FBFC"
bg_2 = "#C2DFE3"
cor_1 = "#9DB4C0"
incor_1 = "#5C6B73"
fg_1 = "#253237"

root = tk.Tk()
root.title("Reversi")
root.geometry('300x250')
root.configure(bg=bg_1)


def new_game():
    button_clicked_label = tk.Label(text="button clicked", bg=bg_2, width="300", height="1",
                                    font=("Calibri", 11, "bold"), fg=fg_1, borderwidth=4, relief="groove", pady="10")
    button_clicked_label.pack()


title_label = tk.Label(text="REVERSI", bg=bg_2, width="300", height="1", font=("Calibri", 24, "bold"), fg=fg_1,
                       borderwidth=4, relief="groove", pady="10")
title_label.pack()
new_game_button = tk.Button(text="New Game", height="1", width="12", command=new_game, bg=bg_2, fg=fg_1,
                            font=("Calibri", 18, "bold"), activebackground=cor_1)
new_game_button.pack()
settings_button = tk.Button(text="Settings", height="1", width="12", command=new_game, bg=bg_2, fg=fg_1,
                            font=("Calibri", 18, "bold"), activebackground=cor_1)
settings_button.pack()

leaderboard_button = tk.Button(text="Leaderboard", height="1", width="12", command=new_game, bg=bg_2, fg=fg_1,
                               font=("Calibri", 18, "bold"), activebackground=cor_1)
leaderboard_button.pack()
logout_button = tk.Button(text="Login", height="1", width="12", command=new_game, bg=bg_2, fg=fg_1,
                          font=("Calibri", 18, "bold"), activebackground=cor_1)
logout_button.pack()
root.mainloop()
