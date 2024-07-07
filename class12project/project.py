import customtkinter as tk
from tkinter import *
from tkinter import ttk
import mysql.connector
import tkinter.messagebox as tkmb
import time

tk.set_appearance_mode("dark")
tk.set_default_color_theme("blue")
con = mysql.connector.connect(
    host="localhost", user="root", password="Narenguru2007", database="new_project"
)

cur = con.cursor()


def log_event(event):
    q = "select tid,tpass from teacher"
    cur.execute(q)
    tdata = cur.fetchall()
    tid = [i[0] for i in tdata]
    tpass = [i[1] for i in tdata]

    q1 = "select sid,spass from studentbio"
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
        tkmb.showwarning("Invail ID","Invaild Id")


def admin():
    adwin = tk.CTk()
    adwin.state("zoomed")
    adwin.geometry("1300x700+0+0")

    adtab = tk.CTkTabview(adwin, width=1300, height=650)
    adtab.pack(padx=20, pady=20)
    distea = adtab.add("Display Teacher")
    distub = adtab.add("Display Student Bio")
    distum = adtab.add("Display Student mark")
    adstub = adtab.add("Add Student bio")
    adstum = adtab.add("Add Student mark")
    adtea = adtab.add("Add Teacher")
    astea = adtab.add("Assign class For teacher")

    # display teacher
    tree1 = ttk.Treeview(distea, height=600)
    tree1.pack(padx=10, pady=10)
    tree1["columns"] = ("tid", "tname", "classt", "tclasses")
    tree1.column("#0", width=0, anchor="center")
    tree1.column("tid", width=100, anchor="center")
    tree1.column("tname", width=200, anchor="center")
    tree1.column("classt", width=100, anchor="center")
    tree1.column("tclasses", width=200, anchor="center")

    tree1.heading("tid", text="Teacher_Id")
    tree1.heading("tname", text="Teacher_Name")
    tree1.heading("classt", text="Class teacher of")
    tree1.heading("tclasses", text="Handling Classes")

    q1 = "select tid,tname,classt,tclasses from teacher"
    cur.execute(q1)
    tdata = cur.fetchall()

    for i in range(len(tdata)):
        tree1.insert(parent="", index="end", iid=i, values=tdata[i])

    # dispay studentbio
    def getstub(x):
        cur = con.cursor()

        if x == "All":
            sql = f"select * from studentbio"
        else:
            sql = f"select * from studentbio where sclass = '{x}'"
        cur.execute(sql)
        return cur.fetchall()
    
    def changestub(event):
        for j in tree2.get_children():
            tree2.delete(j)
        inval = getstub(combo.get())
        for i in range(len(inval)):
            tree2.insert(parent="", index="end", iid=i, values=inval[i])


    val = getval()
    val.insert(0, "All")
    combo = ttk.Combobox(distub, width=20, values=val, state="readonly")
    combo.pack(pady=10)
    combo.bind("<<ComboboxSelected>>", changestub)
    combo.set("All")

    tree2 = ttk.Treeview(distub, height=600)
    tree2.pack(padx=10, pady=10)
    tree2["columns"] = ("admnid", "sname", "sclass", "dob", "fname", "mname")
    tree2.column("#0", width=0, anchor="center")
    tree2.column("admnid", width=100, anchor="center")
    tree2.column("sname", width=200, anchor="center")
    tree2.column("sclass", width=100, anchor="center")
    tree2.column("dob", width=100, anchor="center")
    tree2.column("fname", width=200, anchor="center")
    tree2.column("mname", width=200, anchor="center")

    tree2.heading("admnid", text="Admission_Id")
    tree2.heading("sname", text="Student_Name")
    tree2.heading("sclass", text="Student_Class")
    tree2.heading("dob", text="Date of Birth")
    tree2.heading("fname", text="Father_Name")
    tree2.heading("mname", text="Mother_Name")

    q2 = "select admnid,sname,sclass,dob,fname,mname from studentbio"
    cur.execute(q2)
    sdata = cur.fetchall()

    for i in range(len(sdata)):
        tree2.insert(parent="", index="end", iid=i, values=sdata[i])

    #display student mark
    def getstum(x):
        cur = con.cursor()

        if x == "All":
            sql = f"select * from studentamrk"
        else:
            sql = f"select * from studentmark where sclass = '{x}'"
        cur.execute(sql)
        return cur.fetchall()
    
    def changestum(event):
        for j in tree3.get_children():
            tree3.delete(j)
        inval = getstum(combo.get())
        for i in range(len(inval)):
            tree2.insert(parent="", index="end", iid=i, values=inval[i])


    val1 = getval()
    val1.insert(0, "All")
    combo1 = ttk.Combobox(distub, width=20, values=val, state="readonly")
    combo1.pack(pady=10)
    combo1.bind("<<ComboboxSelected>>", changestum)
    combo1.set("All")

    tree3 = ttk.Treeview(distub, height=600)
    tree3.pack(padx=10, pady=10)
    tree3["columns"] = ("admnid", "sname", "sclass", "dob", "fname", "mname")
    tree3.column("#0", width=0, anchor="center")
    tree3.column("admnid", width=100, anchor="center")
    tree3.column("sname", width=200, anchor="center")
    tree3.column("sclass", width=100, anchor="center")
    tree3.column("dob", width=100, anchor="center")
    tree3.column("fname", width=200, anchor="center")
    tree3.column("mname", width=200, anchor="center")

    tree3.heading("admnid", text="Admission_Id")
    tree3.heading("sname", text="Student_Name")
    tree3.heading("sclass", text="Student_Class")
    tree3.heading("dob", text="Date of Birth")
    tree3.heading("fname", text="Father_Name")
    tree3.heading("mname", text="Mother_Name")

    q3 = "select * from studentmark"
    cur.execute(q3)
    smdata = cur.fetchall()

    for i in range(len(smdata)):
        tree3.insert(parent="", index="end", iid=i, values=smdata[i])
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

def getval():
    res = []
    for i in range(1, 13):
        for j in range(65, 70):
            res.append(f"{i}" f"{chr(j)}")
    return res



loginwin = tk.CTk()
loginwin.geometry("400x300+500+200")
loginwin.title("Login Window")

logframe = tk.CTkFrame(loginwin, width=400, height=300, fg_color="#272221")
logframe.pack()

label1 = tk.CTkLabel(logframe, text="Login", font=("Arial", 24))
label1.grid(row=0, column=0, padx=30, pady=20)

loginid = tk.CTkEntry(logframe, placeholder_text="Enter your Id", width=250)
loginid.grid(row=1, column=0, padx=10, pady=20)

loginpass = tk.CTkEntry(
    logframe, placeholder_text="Enter your password", width=250, show="*"
)
loginpass.grid(row=2, column=0, padx=10, pady=10)
loginpass.bind("<Return>", command=log_event)

logbutton = tk.CTkButton(logframe, text="Login", command=log)
logbutton.grid(row=3, column=0, padx=20, pady=20)

eyebutton = tk.CTkButton(
    logframe, text="👁", width=10, command=lambda: loginpass.configure(show="")
)
eyebutton.grid(row=2, column=1, padx=10, pady=20)

loginwin.mainloop()
