from django.shortcuts import render
import pymysql 

def areaview(request):
    return render(request,'area.html',{'message':'see here...'})

def areasubmit(request):
    try:
        db=pymysql.connect(host='localhost',port=3306,user='root',passwd='123',db='cha1')
        cmd=db.cursor()
        areaname=request.POST['areaname']
        description=request.POST['description']
        file=request.FILES['picture']
        q="insert into areas(userid,areaname,areadescription,areapicture) values('{}','{}','{}','{}')".format(request.session['SES_USERS'][0],areaname,description,file.name)
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
    return render(request,"area.html",{'message':msg})

def fetchallarea(request):
    db=pymysql.connect(host='localhost',port=3306,user='root',passwd='123',db='cha1')
    cmd=db.cursor()
    q="select * from areas where userid='{}'".format(request.session['SES_USERS'][0])
    cmd.execute(q)
    rows=cmd.fetchall()
    db.close()
    return render(request,"displayallarea.html",{'rows':rows})

def displaybyid(request):
    db=pymysql.connect(host='localhost',port=3306,user='root',passwd='123',db='cha1')
    cmd=db.cursor()
    q="select * from areas where areaid={}".format(request.GET['areaid'])
    print(q)
    cmd.execute(q)
    row=cmd.fetchone()
    db.close()
    return render(request,"displaybyareaid.html",{'row':row})

def editdeletearea(request):
    db=pymysql.connect(host='localhost',port=3306,user='root',passwd='123',db='cha1')
    cmd=db.cursor()
    btn=request.GET['btn']
    if(btn=='Edit'):
        q="update areas set  areaname='{}',areadescription='{}' where areaid={}".format(request.GET['areaname'],request.GET['description'],request.GET['areaid'])
        print(q)
        cmd.execute(q)
        db.commit()
        db.close()
    else:
        q="delete from areas where areaid={}".format(request.GET['areaid'])
        print(q)
        cmd.execute(q)
        db.commit()
        db.close()
    return fetchallarea(request)


def editpicture(request):
    try:
        db=pymysql.connect(host='localhost',port=3306,user='root',passwd='123',db='cha1')
        cmd=db.cursor()
        file=request.FILES['areapicture']
        q="update areas set  areapicture='{}' where areaid={}".format(file.name,request.POST['areaid'])
        print(q)
        cmd.execute(q)
        db.commit()
        db.close()
        f=open('E:/CustomizeHomeAutomation/asset/'+file.name,'wb')
        for chunk in file.chunks():
            f.write(chunk)
        f.close()
    except Exception as e:
        print("Err:",e)
    return fetchallarea(request)

