import tkinter as tk

root = tk.Tk()
root.title("Settings")
root.geometry('500x300')

label = tk.Label(text='Settings', font=('Calibri Bold', 50))
label.pack()


# Will open return to main menu.... right now just opens a new window

def button_main():
    # Toplevel object which will
    # be treated as a new window
    new_window = tk.Tk()

    # sets the title of the
    # Toplevel widget
    new_window.title("Main Menu")

    # sets the geometry of toplevel
    new_window.geometry("500x300")

    # A Label widget to show in toplevel
    main_label = tk.Label(new_window, text='Main Menu', font=('Calibri Bold', 50))
    main_label.pack()


main_button = tk.Button(text='Main Menu', command=button_main)
main_button.pack()

label = tk.Label(text='Choose Disk Color: ', font=('Calibri', 11))
label.pack()
colors = ('Red', 'Green', 'Blue', 'Yellow', 'Purple')
colors_var = tk.StringVar(value=colors)
listbox = tk.Listbox(listvariable=colors_var)
listbox.pack()

root.mainloop()
