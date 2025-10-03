import re
from select import select
from sqlite3 import Cursor
from django.shortcuts import redirect, render
from Foodplazaapp.models import Food,Cart,Customer,Admin,Orders
from Foodplazaapp.forms import FoodForm,CustomerForm,AdminForm,CartForm,OrderForm
from django.db import connection
import datetime
# Create your views here.

cursor =connection.cursor()

def displayIndex(request):
    return render(request,'Foodplazaapp/index.html')

#Food 
def displayfoodform(request):
    form=FoodForm           #name from forms.py
    return render(request,'Foodplazaapp/addfood.html',{'form':form})

def addfood(request):
    
    if request.method=='POST':
        form=FoodForm(request.POST)
        
        if form.is_valid():
            try:
                form.save()
                return render(request,'Foodplazaapp/success.html')
            except:
                return render(request,'Foodplazaapp/fail.html')

def showfood(request):
    food=Food.objects.all        #Food from models.py
    return render(request,'Foodplazaapp/foodlist.html',{'foods':food})

def updatefoodform(request):
    form=FoodForm()
    return render(request,'Foodplazaapp/updatefood.html',{'form':form})

def updatefood(request):
    food=Food.objects.get(foodId=request.POST.get('foodId'))
    form=FoodForm(request.POST,instance=food)
    if form.is_valid():
        try:
            form.save()
            return render(request,'Foodplazaapp/success.html')
        except:
            return render(request,'Foodplazaapp/fail.html')

def getfood(request,foodId):
    food=Food.objects.get(foodId=foodId)
    return render(request,'Foodplazaapp/updatefood.html',{'f':food})    

def deletefood(request,foodId):
    food=Food.objects.get(foodId=foodId)
    food.delete()
    return render(request,'Foodplazaapp/success.html')

#customer
def displaycustomerform(request):
    form=CustomerForm
    return render(request,'Foodplazaapp/addcust.html',{'form':form})


def addcust(request):
    if request.method=='POST':
        form=CustomerForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return render(request,'Foodplazaapp/success.html')
            except:
                return render(request,'Foodplazaapp/fail.html')

def showcust(request):
    cust=Customer.objects.all
    return render(request,'Foodplazaapp/custlist.html',{'custs':cust})

def updatecustform(request):
    cust=CustomerForm()
    return render(request,'Foodplazaapp/updatecust.html',{'cust':cust})

def updatecust(request):
    cust=Customer.objects.get(custEmail=request.POST.get('custEmail'))
    custform=CustomerForm(request.POST,instance=cust)
    if custform.is_valid():
        try:
            custform.save()
            return render(request,'Foodplazaapp/success.html')
        except:
            return render(request,'Foodplazaapp/fail.html')

def getcust(request):
    cust=Customer.objects.get(custEmail=request.session['userId'])
    return render(request,'Foodplazaapp/updatecust.html',{'c':cust})

def deletecust(request,custEmail):
    cust=Customer.objects.get(custEmail=custEmail)
    cust.delete()
    return render(request,'Foodplazaapp/success.html')


#Cart
def displaycart(request,foodId):
    food=Food.objects.get(foodId=foodId)
    return render(request,'Foodplazaapp/addcart.html',{'f':food})  

def addcart(request):
    
    if request.method=='POST':
        form=CartForm(request.POST)
        print("Hello")
        if form.is_valid():
            try:
                form.save()
                return render(request,'Foodplazaapp/success.html')
            except:
                return render(request,'Foodplazaapp/fail.html')
  
def addcart1(request):
    if request.method=='POST':
        uid=request.session['userId']
        fid=request.session('foodId')
        fn=request.session('foodName')
        fp=request.session('foodPrice')
        fq=request.session('foodQuantity')
        tp=float(fp)*float(fq)
        sql="insert into cart501(custEmail,foodId,foodName,foodPrice,foodQuantity,totalPrice) values('%s','%s','%s','%s','%s','%f')"%(uid,fid,fn,fp,fq,tp)
        cursor.execute(sql)
        if cursor.rowcount==1:
            return redirect('/Foodplazaapp/showfood')
        else:
            return render(request,'Foodplazaapp/fail.html')


def showcart(request):
    uid=request.session["userId"]
    cart=Cart.objects.filter(custEmail=uid)
    return render(request,'Foodplazaapp/cartlist.html',{'c':cart})

#method name must be same as cartlist.html page href
def deletecart(request,cartId):
    cart=Cart.objects.get(cartId=cartId)
    cart.delete()
    return render(request,'Foodplazaapp/success.html')


#Login
def displayLoginForm(request):
    return render(request,'Foodplazaapp/login.html')

def Login(request):
    if request.method=='POST':
        emailId=request.POST.get('username',' ')
        password=request.POST.get('password',' ')
        type=request.POST.get('type',' ')
        if type=="user":
            for c in Customer.objects.raw("select * from customer501 where custEmail='%s' and custPassword='%s'"%(emailId,password)):
                request.session['userId']=emailId
                return render(request,'Foodplazaapp/index.html')
            else:
                return render(request,'Foodplazaapp/fail.html')
        if type=='admin':
            for a in Admin.objects.raw("select * from admin501 where adminName='%s' and adminPassword='%s'"%(emailId,password)):
                request.session['admin']=emailId
                return render(request,'Foodplazaapp/index.html')
            else:
                return render(request,'Foodplazaapp/fail.html')

#logout
def logout(request):
    session_keys=list(request.session.keys())
    for key in session_keys:
        del request.session[key]
    return render(request,'Foodplazaapp/index.html')

#update username and password

def updatepass(request):
    return render(request,'Foodplazaapp/updatepassword.html')

def updatepassword(request):
    if request.method=='POST':
        userId=request.POST.get('username','')
        password=request.POST.get('password','')
        newpassword=request.POST.get('new password')
        utype=request.POST.get('type','')
        if utype=='user':
            for c in Customer.objects.raw("select * from customer501 where custEmail='%s'"%(userId)):
                if c.custEmail==userId:
                    sql="update customer501 set custPassword='%s' where custEmail='%s' "%(newpassword,userId)
                    cursor.execute(sql)
                    if cursor.rowcount==1:
                        return render(request,'Foodplazaapp/success.html')
                    else:
                        return render(request,'Foodplazaapp/fail.html')

        elif utype=='admin':
            for c in Admin.objects.raw("select * from admin501 where adminName='%s'"%(userId)):
                if c.adminName==userId:
                    sql="update admin501 set adminPassword='%s' where adminName='%s' "%(newpassword,userId)
                    cursor.execute(sql)
                    if cursor.rowcount==1:
                        return render(request,'Foodplazaapp/success.html')
                    else:
                        return render(request,'Foodplazaapp/fail.html')


def placeOrder(request):
    if request.method=='POST':
        uid=request.session["userId"]
        sql="select sum(totalPrice) from cart501 where custEmail='%s'"%(uid)
        cursor.execute(sql)
        data=cursor.fetchone()
        tb=data[0]
        dt=datetime.date.today()
        sql="insert into order501(custEmail,orderDate,totalBill) values('%s','%s','%f')"%(uid,dt,tb)
        cursor.execute(sql)
        if cursor.rowcount==1:
            clearCart(request)
            return render(request,"Foodplazaapp/success.html")
        else:
            return render(request,"Foodplazaapp/fail.html")
    else:
        return render(request,"Foodplazaapp/fail.html")

def clearCart(request):
    custEmail=request.session['userId']
    cart=Cart.objects.filter(custEmail=custEmail)
    cart.delete()
    return render(request,'Foodplazaapp/success.html')
    

def showOrders(request):
    custEmail=request.session['userId']
    orders=Orders.objects.filter(custEmail=custEmail)
    return render(request,'Foodplazaapp/orderlist.html',{'orders':orders})

