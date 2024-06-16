import customtkinter as tk
from tkinter import *
from tkinter import ttk
import mysql.connector
import tkinter.messagebox as tkmb

tk.set_appearance_mode("dark")
tk.set_default_color_theme("blue")
con = mysql.connector.connect(
    host="localhost", user="root", password="Narenguru2007", database="new_project"
)

cur = con.cursor()

def log():
    q = "select tid,tpass from teacher"
    cur.execute(q)
    tdata = cur.fetchall()
    tid = [i[0] for i in tdata]
    tpass = [i[1] for i in tdata]

    q1 = "select admnid,spass from studentbio"
    cur.execute(q1)
    sdata = cur.fetchall()
    sid = [i[0] for i in sdata]
    spass = [i[1] for i in sdata]

    if loginpass.get() == "admin":

        admin()
    elif int(loginid.get()) in tid:
        index = tid.index(int(loginid.get()))
        if loginpass.get() == tpass[index]:
            teacher()
        else:
            tkmb.showwarning("Invaild", "Wrong Password")
    elif int(loginid.get()) in sid:
        index = sid.index(int(loginid.get()))
        if loginpass.get() == spass[index]:

            student()

        else:
            tkmb.showwarning("Invaild", "Wrong Password")
    else:
        tkmb.showwarning("Invail ID")

    


def admin():
    adwin = tk.CTk()
    adwin.state("zoomed")
    adwin.geometry("1300x700+0+0")

    adtab = tk.CTkTabview(adwin)
    adtab.pack()
    diste=adtab.add('Display Teacher')
    distub=adtab.add('Display Student Bio')
    distum=adtab.add('Display Student mark')

    adwin.mainloop()


def teacher():
    twin = tk.CTk()
    twin.state("zoomed")
    twin.geometry("1300x700+0+0")
    twin.mainloop()


def student():
    swin = tk.CTk()
    swin.state("zoomed")
    swin.geometry("1300x700+0+0")
    swin.mainloop()




loginwin = tk.CTk()
loginwin.geometry("400x300+500+200")
loginwin.title("Login Window")

logframe = tk.CTkFrame(loginwin, width=400, height=300, fg_color="#272221")
logframe.pack()

label1 = tk.CTkLabel(logframe, text="Login", font=("Arial", 24))
label1.grid(row=0, column=0, padx=30, pady=20)

loginid = tk.CTkEntry(logframe, placeholder_text="Enter your Id", width=250)
loginid.grid(row=1, column=0, padx=10, pady=20)

loginpass = tk.CTkEntry(logframe, placeholder_text="Enter your password", width=250)
loginpass.grid(row=2, column=0, padx=10, pady=10)

logbutton = tk.CTkButton(logframe, text="Login",command=log)
logbutton.grid(row=3, column=0, padx=20, pady=20)

loginwin.mainloop()

