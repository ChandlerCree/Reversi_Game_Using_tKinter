import tkinter as tk

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
        self.main_button = tk.Button(text='Main Menu', command=self.button_main)
        self.main_button.pack()

        self.label = tk.Label(text='Choose Disk Color: ', font=('Calibri', 11))
        self.label.pack()
        colors = ('Red', 'Green', 'Blue', 'Yellow', 'Purple')
        colors_var = tk.StringVar(value=colors)
        self.listbox = tk.Listbox(listvariable=colors_var)
        self.listbox.pack()



        # show the frame on the container
        self.pack()

    def button_main(self):
        button_clicked_label = tk.Label(text="button clicked", bg=bg_2, width="300", height="1",
                                        font=("Calibri", 11, "bold"), fg=fg_1, borderwidth=4, relief="groove",
                                        pady="10")
        button_clicked_label.pack()







