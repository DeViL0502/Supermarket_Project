from logging.config import valid_ident
from turtle import goto
from django.shortcuts import render
import mysql.connector
import datetime

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="deep",
    database="supermarket"
)
cursor=mydb.cursor()

keys=[['pname1','prc1','qty1','tot1'],['pname2','prc2','qty2','tot2'],['pname3','prc3','qty3','tot3'],['pname4','prc4','qty4','tot4'],['pname5','prc5','qty5','tot5'],['pname6','prc6','qty6','tot6'],['pname7','prc7','qty7','tot7'],['pname8','prc8','qty8','tot8'],['pname9','prc9','qty9','tot9'],['pname10','prc10','qty10','tot10']]

names=[['prdt1','prc1','qty1'],['prdt2','prc2','qty2'],['prdt3','prc3','qty3'],['prdt4','prc4','qty4'],['prdt5','prc5','qty5'],['prdt6','prc6','qty6'],['prdt7','prc7','qty7'],['prdt8','prc8','qty8'],['prdt9','prc9','qty9'],['prdt10','prc10','qty10']]

# Create your views here.
def index(request):
    return render(request,'index.html')

def billArea(request):
    context={"total":0,"items":["Toothpaste","Biscuit","Washing Powder","Chocolate","Maggie","Deodrent","Soap","Shampoo","Soft Drinks","Milk","Ice Cream","Eggs","Facewash","Harpic"],"date":datetime.datetime.now().strftime("%x")}
    cursor.execute("delete from bill;")

    for k in range(0,10):
        if(request.POST.get(names[k][0])!='' and request.POST.get(names[k][0])!=None):
            sql1="INSERT INTO bill(item,price,quantity,total) VALUES(%s,%s,%s,%s)"
            sql2="INSERT INTO sellings(Date,PName,Price,Quantity,Total) VALUES(%s,%s,%s,%s,%s)"
            val1=(request.POST.get(names[k][0]),request.POST.get(names[k][1]),request.POST.get(names[k][2]),int(request.POST.get(names[k][1]))*int(request.POST.get(names[k][2])))
            val2=(datetime.datetime.now().strftime("%x"),request.POST.get(names[k][0]),request.POST.get(names[k][1]),request.POST.get(names[k][2]),int(request.POST.get(names[k][1]))*int(request.POST.get(names[k][2])))
            cursor.execute(sql1,val1)
            cursor.execute(sql2,val2)
            sql3="update stocks set Quantity=Quantity-"+request.POST.get(names[k][2])+" where PName='"+request.POST.get(names[k][0])+"';"
            cursor.execute(sql3)
            context["total"]=context["total"]+int(request.POST.get(names[k][1]))*int(request.POST.get(names[k][2]))
            mydb.commit()

    cursor.execute("SELECT * FROM bill")
    result = cursor.fetchall()
    for i in range(0,len(result)):
        for j in range(0,4):
            context[keys[i][j]]=result[i][j]

    return render(request,'billArea.html',context)

def sellings(request):
    cursor.execute("SELECT * FROM sellings")
    result = cursor.fetchall()
    context={"result":result}
    
    return render(request,'sellings.html',context)

def stocks(request):
    items=["Toothpaste","Biscuit","Washing Powder","Chocolate","Maggie","Deodrent","Soap","Shampoo","Soft Drinks","Milk","Ice Cream","Eggs","Facewash","Harpic"]

    if(request.POST.get('pname')!='' and request.POST.get('pname')!=None):
        if( request.POST.get('pname')==items[0] or request.POST.get('pname')==items[1] or request.POST.get('pname')==items[2] or request.POST.get('pname')==items[3] or request.POST.get('pname')==items[4] or request.POST.get('pname')==items[5] or request.POST.get('pname')==items[6] or request.POST.get('pname')==items[7] or request.POST.get('pname')==items[8] or request.POST.get('pname')==items[9] or request.POST.get('pname')==items[10] or request.POST.get('pname')==items[11] or request.POST.get('pname')==items[12]):
            sql1="update stocks set Quantity=Quantity+"+request.POST.get('pqty')+" where PName='"+request.POST.get('pname')+"';"
            cursor.execute(sql1)
            sql2="update stocks set Date='"+datetime.datetime.now().strftime("%x")+"' where PName='"+request.POST.get('pname')+"';"
            cursor.execute(sql2)
            mydb.commit()
        else:
            sql="INSERT INTO stocks(PName,Quantity,Date) VALUES(%s,%s,%s)"
            val=(request.POST.get('pname'),request.POST.get('pqty'),datetime.datetime.now().strftime("%x"))
            cursor.execute(sql,val)
            mydb.commit()

    cursor.execute("SELECT * FROM stocks")
    result = cursor.fetchall()
    context={"result":result,"items":["Toothpaste","Biscuit","Washing Powder","Chocolate","Maggie","Deodrent","Soap","Shampoo","Soft Drinks","Milk","Ice Cream","Eggs","Facewash","Harpic"]}
    
    return render(request,'stocks.html',context)
