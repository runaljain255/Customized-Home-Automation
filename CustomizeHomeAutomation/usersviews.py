from django.shortcuts import render
import pymysql 
import datetime

def userlogin(request):
    return render(request,'userlogin.html',{'message':''})

def checklogin(request):
    try:
        db=pymysql.connect(host='localhost',port=3306,user='root',passwd='123',db='cha1')
        cmd=db.cursor()
        q="select * from users where emailid='{}' and password='{}'".format(request.GET['emailid'],request.GET['password'])
        print(q)
        cmd.execute(q)
        row=cmd.fetchone()
        print(row)
        if(row==None):
            msg='Invalid Emailid/password'
        else:
            request.session['SES_USERS']=row
            D=datetime.datetime.now()
            request.session['LTIME']=D.strftime('%A %d-%B-%Y %H:%M:%S')
            return render(request,'homepage.html')
        db.commit()
        db.close()
    except Exception as e:
        print("Err:",e)
        msg='Incorrect Id and Password'
    return render(request,"userlogin.html",{'message':msg})

def userview(request):
    return render(request,"users.html",{'message':''})

def usersubmit(request):
    try:
        db=pymysql.connect(host='localhost',port=3306,user='root',passwd='123',db='cha1')
        cmd=db.cursor()
        email=request.POST['email']
        name=request.POST['first']+" "+request.POST['second']
        dob=request.POST['dob']
        mobile=request.POST['mobile']
        password=request.POST['password']
        file=request.FILES['picture']
        # print(email)
        # print(name)
        # print(dob)
        # print(mobile)
        # print(password+)
        # print(picture)
        q="insert into users values('{}','{}','{}','{}','{}','{}')".format(email,name,mobile,dob,password,file.name)
        print(q)
        cmd.execute(q)
        db.commit()
        db.close()
        f=open('E:/CustomizeHomeAutomation/asset/'+file.name,'wb')
        for chunk in file.chunks():
            f.write(chunk)
        f.close()
        msg='Record Submitted...'
    except Exception as e:
        print("Err:",e)
        msg='Fail to submit record...'
    return render(request,"users.html",{'message':msg})