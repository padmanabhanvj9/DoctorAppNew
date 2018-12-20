from flask import Flask,request,jsonify
from sqlwrapper import gensql,dbget,dbput
import json
import random
import datetime
def insertgender(request):
     try:
         d=request.json
         print(d)
         gensql('insert','Gender',d)
         return(json.dumps({"Message":"Record Inserted Successfully","MessageCode":"RIS","Service":"Success"},indent=2))
     except:
         return("some thing went wrong in input funtion")

def updategender(request):
    try:
        d=request.json
        id= { k : v for k,v in d.items() if k not in ('Gender_Id')}
        name={ k : v for k,v in d.items() if k in ('Gender_Id')}
        gensql('update','Gender',name,id)
        return(json.dumps({"Message":"Record Updated Successfully","MessageCode":"RUS","Service":"Success"},indent=2))
    except:
         return("some thing went wrong in update funtion")


def selectgender(request):
    try:
        d=json.loads(gensql('select','Gender','*'))
        return(json.dumps({"Message":"Record Selected Successfully","MessageCode":"RSS","Service":"Success","output":d},indent=2))
    except:
         return("some thing went wrong in select funtion")


           

def deletegender(request):
    try:
        res=request.json['Gender_Id']
        dbput("delete from Gender where Gender_Id='"+res+"'")
        return(json.dumps({"Message":"Record Deleted Successfully","MessageCode":"RDS","Service Status":"Success"},indent=4))
    except:
         return("some thing went wrong in delete funtion")

