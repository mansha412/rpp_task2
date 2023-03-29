from django.shortcuts import render

from signup.models import jain
import mysql.connector as sql
fn=''
ln=''
s=''
em=''
pswd=''

# Create your views here.
def signaction(request):
    global fn,ln,s,em,pswd
    if request.method=='POST':
        m=sql.connect(host='localhost',user='root',password='mansha@412',database='website')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="First_Name":
                fn=value
            if key=="Last_Name":
                ln=value
            if key=="Sex":
                s=value
            if key=="Email":
                em=value
            if key=="Password":
                pswd=value

        c="insert into jain Values('{}','{}','{}','{}','{}')".format(fn,ln,s,em,pswd)
        cursor.execute(c)
        m.commit()
        about = jain(First_Name=fn,Last_Name=ln,Sex=s,Email=em,Password=pswd)
        about.save()
        

        

        

    return render(request,'signup.html')    