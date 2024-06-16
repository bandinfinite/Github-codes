import mysql.connector
from tabulate import tabulate

con = mysql.connector.connect(
    host="localhost", user="root", password="Narenguru2007", database="naren12a"
)

if con.is_connected():
    print("connected")
else:
    print("Not connected")

cur = con.cursor()


def create_customer():
    q = "create table customer(cid int primary key , cname varchar(30), balance float, dob date)"
    cur.execute(q)
    con.commit()
    print("Created succesful")


def insert_customer():
    cid = int(input("Enter Customer Id:"))
    name = input("Enter customer name:")
    bal = float(input("Enter customer balance: "))
    dob = input("Enter dob of customer")
    q = "insert into customer values({},'{}',{},'{}')".format(cid, name, bal, dob)
    cur.execute(q)
    con.commit()
    print("Inserted succesfully")


def select():
    q = "select * from customer"
    cur.execute(q)
    data = cur.fetchall()
    print(tabulate(data, headers=["Cid", "Cname", "Balance", "Dob"]))


def create_transaction():
    q = "create table transaction(tid int auto_increment primary key ,cid int,tdate date ,amt float, ttype varchar(10))"
    cur.execute(q)
    con.commit()
    print("created succesful")


def insert_transaction():
    cid = int(input("Enter Customer Id :"))
    tdate = input("Enter the transaction data:")
    amt = input("Enter transaction amount:")
    ttype = input("Enter transaction type(d,w):")
    q = 'insert into transaction(cid,tdate,amt,ttype) values({},"{}",{},"{}")'.format(
        cid, tdate, amt, ttype
    )
    cur.execute(q)
    con.commit()
    print("Inserted succesful")


def update():
    q = "select c.cid, c.balance,t.amt,t.ttype from customer c , transaction t where c.cid=t.cid"
    cur.execute(q)
    data = cur.fetchall()
    for i in data:
        if i[3].lower() == "d":
            nbal = i[1] + i[2]
            q = "update customer set balance= {} where cid={}".format(nbal, i[0])
            cur.execute(q)
            con.commit()
        elif i[3].lower() == "w":
            nbal = i[1] - i[2]
            q = "update customer set balance= {} where cid={}".format(nbal, i[0])
            cur.execute(q)
            con.commit()
        print(i[0], nbal)
    print("Updated succesfully")


while True:
    print("1.Create table-customer ")
    print("2.create table-transaction")
    print("3.Insert-customer")
    print("4.insert-transaction")
    print("5.update ")
    print("6. To display")
    print("10.Exit")
    ch = int(input("Enter your choice:"))
    if ch == 1:
        create_customer()
    elif ch == 2:
        create_transaction()
    elif ch == 3:
        insert_customer()
    elif ch == 4:
        insert_transaction()
    elif ch == 5:
        update()
    elif ch == 6:
        select()
    elif ch == 10:
        break
    else:
        print("Invalid choice")
