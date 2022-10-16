import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="deep",
    database="supermarket"
)
cursor=mydb.cursor()
cursor.execute("insert into stocks(PName,Quantity,Date)value('Biscuit',50,'10/15/22');")
cursor.execute("insert into stocks(PName,Quantity,Date)value('Washing Powder',20,'10/15/22');")
cursor.execute("insert into stocks(PName,Quantity,Date)value('Chocolate',50,'10/15/22');")
cursor.execute("insert into stocks(PName,Quantity,Date)value('Maggie',50,'10/15/22');")
cursor.execute("insert into stocks(PName,Quantity,Date)value('Deodrent',50,'10/15/22');")
cursor.execute("insert into stocks(PName,Quantity,Date)value('Soap',50,'10/15/22');")
cursor.execute("insert into stocks(PName,Quantity,Date)value('Shampoo',50,'10/15/22');")
cursor.execute("insert into stocks(PName,Quantity,Date)value('Soft Drinks',50,'10/15/22');")
cursor.execute("insert into stocks(PName,Quantity,Date)value('Milk',50,'10/15/22');")
cursor.execute("insert into stocks(PName,Quantity,Date)value('Eggs',50,'10/15/22');")
cursor.execute("insert into stocks(PName,Quantity,Date)value('Facewash',50,'10/15/22');")
cursor.execute("insert into stocks(PName,Quantity,Date)value('Harpic',50,'10/15/22');")
mydb.commit()
