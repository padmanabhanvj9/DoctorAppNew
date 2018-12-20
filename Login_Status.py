from sqlwrapper import gensql,dbget,dbput
import json
import datetime
from flask import Flask,request,jsonify


def Insert_Login_Status(request):
    try:
        d=request.json
        print(d)
        gensql('insert','Login_Status',d)
        return(json.dumps({"Message":"Record Inserted Successfully","MessageCode":"RIS","Service Status":"Success"},indent=4))
    except:
        return("some thing went wrong in input")  


def Select_Login_Status(request):
    try:
        d=json.loads(gensql('select','Login_Status','*'))
           
        return(json.dumps({"Message":"Record Selected Successfully","MessageCode":"RSS","Service Status":"Success","Output":d},indent=4))
    except:
        return("some thing went wrong in select function")  

def Update_Login_Status(request):
    try:
        d=request.json
        a = { k : v for k,v in d.items() if k  in ('Status_Id')}
        print(a)
        e={ k : v for k,v in d.items() if k not in ('Status_Id')}
        print(e)
        gensql('update','Login_Status',e,a)
        return(json.dumps({"Message":"Record Updated Successfully","MessageCode":"RUS","Service Status":"Success"},indent=4))
    except:
        return("some thing went wrong in update function")  


def Delete_Login_Status(request):
    try:
        d=request.json['Status_Id']
        dbput("delete from Login_Status where Status_Id='"+d+"'")
        return(json.dumps({"Message":"Record Deleted Successfully","MessageCode":"RDS","Service Status":"Success"},indent=4))
    except:
        return("some thing went wrong in update function")  

