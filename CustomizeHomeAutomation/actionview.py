from django.shortcuts import render
import pymysql
from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
import time

def fetchallarea(request):
    db=pymysql.connect(host='localhost',port=3306,user='root',passwd='123',db='cha1')
    cmd=db.cursor()
    q="select * from areas where userid='{}'".format(request.session['SES_USERS'][0])
    cmd.execute(q)
    rows=cmd.fetchall()
    return render(request,"actions.html",{'rows':rows})

def fetchallswitchs(request):
    db=pymysql.connect(host='localhost',port=3306,user='root',passwd='123',db='cha1')
    cmd=db.cursor()
    q="select * from switches where userid='{}' and areaid='{}'".format(request.session['SES_USERS'][0],request.GET['areaid'])
    cmd.execute(q)
    rows=cmd.fetchall()
    return render(request,"switchactions.html",{'rows':rows})

def pubnubaction(request):
    btn=request.GET['btn']
    print(btn)
    ConnectPubNub(btn)
    return fetchallarea(request)

def ConnectPubNub(key):
    # Enter your PubNub Publish Key and use the Market Order Demo Subscribe Key
    pc=PNConfiguration()
    pc.subscribe_key="sub-c-a7e5fc3a-c3fa-11e9-93da-dae13b67b174"
    pc.publish_key="pub-c-0f5563aa-14f8-4f2d-ba9a-fca6ef6ad9c6"
    pc.ssl=True
    pubnub = PubNub(pc)
    #  Listen for Messages on the Market Order Channel
    channel = 'philips1'
    pubnub.publish().channel(channel).message(key).pn_async(show)
    time.sleep(2)

def show(msg,stat):
    if(msg and stat):print(msg.timetoken,stat.status_code)
    else:
        print("Error",stat and stat.status_code)    