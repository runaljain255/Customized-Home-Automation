from django.shortcuts import render
import pymysql

def fetchallarea(request):
    db=pymysql.connect(host='localhost',port=3306,user='root',passwd='123',db='cha1')
    cmd=db.cursor()
    q="select * from areas where userid='{}'".format(request.session['SES_USERS'][0])
    cmd.execute(q)
    rows=cmd.fetchall()
    return rows

def switchview(request):
    rows=fetchallarea(request)
    return render(request,"switch.html",{'message':'see here...','rows':rows})

def switchsubmit(request):
    try:
        db=pymysql.connect(host='localhost',port=3306,user='root',passwd='123',db='cha1')
        cmd=db.cursor()
        areaid=request.POST['areaid']
        purpose=request.POST['purpose']
        key1=request.POST['key']
        file=request.FILES['picture']
        q="insert into switches(userid,areaid,purpose,s_key,icon) values('{}','{}','{}','{}','{}')".format(request.session['SES_USERS'][0],areaid,purpose,key1,file.name)
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
    rows=fetchallarea(request)
    return render(request,"switch.html",{'message':msg,'rows':rows})