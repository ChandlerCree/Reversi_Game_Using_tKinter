import mysql.connector
import tkinter as tk
from tkinter import *
window = tk.Tk()
window.geometry("400x250")
 my_connect = mysql.connector.connect(
   host="localhost",
   user="userid",
   passwd="password",
   database="database_name"
 )
 my_conn = my_connect.cursor()
 ####### end of connection ####
 my_conn.execute("SELECT * FROM student limit 0,10")
i=0
for student in my_conn:
    for j in range(len(student)):
        e = Entry(window, width=10, fg='blue')
        e.grid(row=i, column=j)
        e.insert(END, student[j])
    i=i+1
window.mainloop()