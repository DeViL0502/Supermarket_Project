from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
from tkinter import messagebox
import mysql.connector

def connection():
    connectObj = mysql.connector.connect(
        host="localhost",
        user="root",
        password="deep",
        database="supermarket"
    )
    cur = connectObj.cursor()
    try:
        cur.execute("CREATE TABLE sellings (Date VARCHAR(225),PName VARCHAR(225),Price VARCHAR(225),Quantity int,Total int)")
    except:
        print("")
    try:
        cur.execute("CREATE TABLE stocks (Date VARCHAR(225),PName VARCHAR(225),Price VARCHAR(225),Quantity int)")
    except:
        print("")


# ----------------------------------------------tab1 ----------------------------------

def GenerateBill():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="0502",
        database="supermarket"
    )
    cur = mydb.cursor()

    global billarea
    if p1quantity.get() == 0 and p2quantity.get() == 0 and p3quantity.get() == 0 and p4quantity.get() == 0:
        messagebox.showerror("Error", "No product purchased")
    else:

        price = IntVar()
        price2 = IntVar()
        price3 = IntVar()
        price4 = IntVar()

        price = price2 = price3 = price4 = 0
        if p1quantity.get() != 0:
            price = p1quantity.get() * p1price.get()
            billarea.insert(END, f"\n{dateE.get()}\t Washing Powder \t {p1price.get()}\t   {p1quantity.get()}\t    {price}")

            cur.execute("INSERT INTO sellings (Date,PName,Price,Quantity,Total) VALUES(%s,%s,%s,%s,%s)",(dateE.get(),"Washing Powder",p1price.get(),p1quantity.get(),price))
            cur.execute("select Quantity from stocks where PName='Washing Powder'")
            q=cur.fetchall()
            cur.execute("UPDATE stocks set Quantity=%s where PName='Washing Powder';",
                        (q[0][0]-p1quantity.get(),))
            mydb.commit()

        if p2quantity.get() != 0:
            price2 = (p2quantity.get() * p2price.get())
            billarea.insert(END, f"\n{dateE.get()}\t Colgate        \t {p2price.get()}\t   {p2quantity.get()}\t    {price2}")
            cur.execute("INSERT INTO sellings (Date,PName,Price,Quantity,Total) VALUES(%s,%s,%s,%s,%s)",
                        (dateE.get(), "Colgate", p2price.get(), p2quantity.get(), price2))
            cur.execute("select Quantity from stocks where PName='Colgate'")
            q = cur.fetchall()
            cur.execute("UPDATE stocks set Quantity=%s where PName='Colgate';",
                        (q[0][0] - p2quantity.get(),))
            mydb.commit()

        if p3quantity.get() != 0:
            price3 = p3quantity.get() * p1price.get()
            print(price3)
            billarea.insert(END, f"\n{dateE.get()}\t Shampoo        \t {p3price.get()}\t   {p3quantity.get()}\t    {price3}")

            cur.execute("INSERT INTO sellings (Date,PName,Price,Quantity,Total) VALUES(%s,%s,%s,%s,%s)",
                        (dateE.get(), "Shampoo", p3price.get(), p3quantity.get(), price3))
            cur.execute("select Quantity from stocks where PName='Shampoo'")
            q = cur.fetchall()
            cur.execute("UPDATE stocks set Quantity=%s where PName='Shampoo';",
                        (q[0][0] - p3quantity.get(),))
            mydb.commit()

        if p4quantity.get() != 0:
            price4 = p4quantity.get() * p1price.get()
            billarea.insert(END, f"\n{dateE.get()}\t Sugar          \t {p4price.get()}\t   {p4quantity.get()}\t    {price4}")

            cur.execute("INSERT INTO sellings (Date,PName,Price,Quantity,Total) VALUES(%s,%s,%s,%s,%s)",
                        (dateE.get(), "Sugar", p4price.get(), p4quantity.get(), price4))
            cur.execute("select Quantity from stocks where PName='Sugar'")
            q = cur.fetchall()
            cur.execute("UPDATE stocks set Quantity=%s where PName='Sugar';",
                        (q[0][0] - p4quantity.get(),))
            mydb.commit()

        Totalprice = IntVar()
        Totalprice = price + price2 + price3 + price4

        Totalquantity = IntVar()
        Totalquantity = p1quantity.get() + p2quantity.get() + p3quantity.get() + p4quantity.get()
        billarea.insert(END,"\n-------------------------------------------")
        billarea.insert(END, f"\nTotal                            {Totalquantity}\t   {Totalprice}")


def view():
    connectObj = mysql.connector.connect(
        host="localhost",
        user="root",
        password="0502",
        database="supermarket"
    )
    cur = connectObj.cursor()

    sql = 'Select * from Sellings'
    cur.execute(sql)
    rows = cur.fetchall()

    for i in rows:
        allrows = ""
        for j in i:
            allrows += str(j) + '        \t'
        allrows += '\n'
        viewarea.insert(END, allrows)

def addStock():
    global dateE2, qty, name, price

    connectObj = mysql.connector.connect(
        host="localhost",
        user="root",
        password="0502",
        database="supermarket"
    )
    cur = connectObj.cursor()
    cur.execute("select Quantity from stocks where PName=%s",
                (name.get(),))
    quantity=cur.fetchall()
    cur.execute("UPDATE stocks set Quantity=%s where PName=%s",
                (quantity[0][0]+qty.get(),name.get()))
    connectObj.commit()


def viewStock():
    connectObj = mysql.connector.connect(
        host="localhost",
        user="root",
        password="0502",
        database="supermarket"
    )
    cur = connectObj.cursor()

    sql = 'Select Date,Quantity from stocks'
    cur.execute(sql)

    qu = cur.fetchall()
    allrows=""
    allrows = str(qu[0][0]) + "         Washing Powder           350         " + str(qu[0][1]) + "\n"
    viewarea2.insert(END, allrows)
    allrows = str(qu[1][0]) + "         Colgate                  150         " + str(qu[1][1]) + "\n"
    viewarea2.insert(END, allrows)
    allrows = str(qu[2][0]) + "         Shampoo                  170         " + str(qu[2][1]) + "\n"
    viewarea2.insert(END, allrows)
    allrows = str(qu[3][0]) + "         Sugar                    150         " + str(qu[3][1]) + "\n"
    viewarea2.insert(END, allrows)
    allrows = "-------------------------------------------------------------\n"
    viewarea2.insert(END, allrows)






connection()
window = Tk()
window.title("Deepraj's Shop Management Project")
tabs = ttk.Notebook(window)
root = ttk.Frame(tabs)
root2 = ttk.Frame(tabs)
root3 = ttk.Frame(tabs)

tabs.add(root, text='Billing')
tabs.add(root2, text='Stocks')
tabs.add(root3, text='Sellings')
tabs.pack(expand=1, fill="both")
dateL = Label(root, text="Date", bg="DodgerBlue2", width=12, font=('arial', 15, 'bold'))
dateL.grid(row=0, column=0, padx=7, pady=7)

dateE = DateEntry(root, width=12, font=('arial', 15, 'bold'))
dateE.grid(row=0, column=1, padx=7, pady=7)

l = Label(root, text="Product", font=('arial', 15, 'bold'), bg="DodgerBlue2", width=12)
l.grid(row=1, column=0, padx=7, pady=7)

l = Label(root, text="Price", font=('arial', 15, 'bold'), bg="DodgerBlue2", width=12)
l.grid(row=1, column=1, padx=7, pady=7)

l = Label(root, text="Quantity", font=('arial', 15, 'bold'), bg="DodgerBlue2", width=12)
l.grid(row=1, column=2, padx=7, pady=7)

# ----product 1----------------------------------------------------
p1name = StringVar()
p1name.set('Washing Power (1kg)')

p1price = IntVar()
p1price.set(350)

connectObj = mysql.connector.connect(
        host="localhost",
        user="root",
        password="deep",
        database="supermarket"
    )
cur = connectObj.cursor()
cur.execute("select * from stocks where PName='Washing Powder'")
rows=cur.fetchall()
for i in rows:
    qty=i[3]
    if qty>0:
        p1quantity = IntVar()
        p1quantity.set(0)
        t = Entry(root, textvariable=p1quantity, font=('arial', 15, 'bold'), width=12)
        t.grid(row=2, column=2, padx=7, pady=7)
    else:
        p1quantity = StringVar()
        p1quantity.set("Out Of Stock")
        t = Label(root, textvariable=p1quantity, font=('arial', 15, 'bold'), width=12)
        t.grid(row=2, column=2, padx=7, pady=7)

l = Label(root, text=p1name.get(), font=('arial', 15, 'bold'), width=20)
l.grid(row=2, column=0, padx=7, pady=7)

l = Label(root, text=p1price.get(), font=('arial', 15, 'bold'), width=12)
l.grid(row=2, column=1, padx=7, pady=7)


# ----product 2-------------------------------------------------------------
p2name = StringVar()
p2name.set('Colgate (200gm)')

p2price = IntVar()
p2price.set(150)

connectObj = mysql.connector.connect(
        host="localhost",
        user="root",
        password="deep",
        database="supermarket"
    )
cur = connectObj.cursor()
cur.execute("select * from stocks where PName='Colgate'")
rows=cur.fetchall()
for i in rows:
    qty=i[3]
    if qty>0:
        p2quantity = IntVar()
        p2quantity.set(0)
        t = Entry(root, textvariable=p2quantity, font=('arial', 15, 'bold'), width=12)
        t.grid(row=3, column=2, padx=7, pady=7)
    else:
        p2quantity = StringVar()
        p2quantity.set("Out Of Stock")
        t = Label(root, textvariable=p2quantity, font=('arial', 15, 'bold'), width=12)
        t.grid(row=3, column=2, padx=7, pady=7)

l = Label(root, text=p2name.get(), font=('arial', 15, 'bold'), width=20)
l.grid(row=3, column=0, padx=7, pady=7)

l = Label(root, text=p2price.get(), font=('arial', 15, 'bold'), width=12)
l.grid(row=3, column=1, padx=7, pady=7)


# ----product 3----
p3name = StringVar()
p3name.set('Shampoo (400ml)')

p3price = IntVar()
p3price.set(170)

connectObj = mysql.connector.connect(
        host="localhost",
        user="root",
        password="deep",
        database="supermarket"
    )
cur = connectObj.cursor()
cur.execute("select * from stocks where PName='Shampoo'")
rows=cur.fetchall()
for i in rows:
    qty=i[3]
    if qty>0:
        p3quantity = IntVar()
        p3quantity.set(0)
        t = Entry(root, textvariable=p3quantity, font=('arial', 15, 'bold'), width=12)
        t.grid(row=4, column=2, padx=7, pady=7)
    else:
        p3quantity = StringVar()
        p3quantity.set("Out Of Stock")
        t = Label(root, textvariable=p3quantity, font=('arial', 15, 'bold'), width=12)
        t.grid(row=4, column=2, padx=7, pady=7)

l = Label(root, text=p3name.get(), font=('arial', 15, 'bold'), width=20)
l.grid(row=4, column=0, padx=7, pady=7)

l = Label(root, text=p3price.get(), font=('arial', 15, 'bold'), width=12)
l.grid(row=4, column=1, padx=7, pady=7)


# ----product 4----
p4name = StringVar()
p4name.set('Sugar (1kg)')

p4price = IntVar()
p4price.set(150)

connectObj = mysql.connector.connect(
        host="localhost",
        user="root",
        password="deep",
        database="supermarket"
    )
cur = connectObj.cursor()
cur.execute("select * from stocks where PName='Sugar'")
rows=cur.fetchall()
for i in rows:
    qty=i[3]
    if qty>0:
        p4quantity = IntVar()
        p4quantity.set(0)
        t = Entry(root, textvariable=p4quantity, font=('arial', 15, 'bold'), width=12)
        t.grid(row=5, column=2, padx=7, pady=7)
    else:
        p4quantity = StringVar()
        p4quantity.set("Out Of Stock")
        t = Label(root, textvariable=p4quantity, font=('arial', 15, 'bold'), width=12)
        t.grid(row=5, column=2, padx=7, pady=7)

l = Label(root, text=p4name.get(), font=('arial', 15, 'bold'), width=20)
l.grid(row=5, column=0, padx=7, pady=7)

l = Label(root, text=p4price.get(), font=('arial', 15, 'bold'), width=12)
l.grid(row=5, column=1, padx=7, pady=7)


# ------------------------bill-------------------------
billarea = Text(root)

submitbtn = Button(root, command=GenerateBill, text="Bill",
                   font=('arial', 15, 'bold'), bg="DodgerBlue2", width=20)

submitbtn.grid(row=6, column=0, padx=7, pady=7)

viewbtn = Button(root3, command=view, text="View All Sellings",
                 font=('arial', 15, 'bold'), bg="DodgerBlue2", width=20)

viewbtn.grid(row=6, column=2, padx=7, pady=7)

billarea.grid(row=0, column=15)
viewarea = Text(root3)
viewarea.grid(row=9, column=2)


# ----------------------------------------------tab2 ----------------------------------



dateL = Label(root2, text="Date", bg="DodgerBlue2", width=12, font=('arial', 15, 'bold'))
dateL.grid(row=0, column=0, padx=7, pady=7)

dateE2 = DateEntry(root2, width=12, font=('arial', 15, 'bold'))
dateE2.grid(row=0, column=1, padx=7, pady=7)

l = Label(root2, text="Product Name", font=('arial', 15, 'bold'), bg="DodgerBlue2", width=12)
l.grid(row=1, column=0, padx=7, pady=7)

l = Label(root2, text="Quantity", font=('arial', 15, 'bold'), bg="DodgerBlue2", width=12)
l.grid(row=2, column=0, padx=7, pady=7)

name = StringVar()
price = IntVar()
qty = IntVar()

Name = Entry(root2, textvariable=name, font=('arial', 15), width=15)
Name.grid(row=1, column=1, padx=7, pady=7)

Qty = Entry(root2, textvariable=qty, font=('arial', 15, 'bold'), width=15)
Qty.grid(row=2, column=1, padx=7, pady=7)

addbtn = Button(root2, command=addStock, text="Add",
                font=('arial', 15, 'bold'), bg="DodgerBlue2", width=20)

addbtn.grid(row=4, column=1, padx=7, pady=7)

viewarea2 = Text(root2)
viewarea2.grid(row=5, column=0, columnspan=2)

viewbtn2 = Button(root2, command=viewStock, text="View Stock",
                  font=('arial', 15, 'bold'), bg="DodgerBlue2", width=20)

viewbtn2.grid(row=4, column=0, padx=7, pady=7)
billarea.delete('1.0', END)
billarea.insert(END, "\t|| Deepraj's Shop Management Project ||")
billarea.insert(END, "\n_________________________________________\n")
billarea.insert(END, "\nDate\t Products\t       Price\t QTY\t  Total")
billarea.insert(END, "\n===========================================")

viewarea.insert(END, f"Date\t         Product\t        Price\t    Quantity\t Total Amount\n")



viewarea2.insert(END,f"  Date \t            Product\t              Price\t     Quantity\t \n")

mainloop()