from django.shortcuts import render
#from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
import mysql.connector as sql
em=''
pswd=''

# Create your views here.
#@login_required
def loginaction(request):
    global em,pswd
    if request.method=='POST':
        m=sql.connect(host='localhost',user='root',password='mansha@412',database='website')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="email":
                em=value
            if key=="password":
                pswd=value

        c="select * from jain where email='{}' and password='{}'".format(em,pswd)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return render(request,"error.html")
        else:
            return render(request,'index.html')
    

    return render(request,'login.html')    