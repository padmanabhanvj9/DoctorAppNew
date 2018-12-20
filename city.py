from sqlwrapper import gensql,dbget,dbput
import json
#import random
import datetime
from flask import Flask,request,jsonify



def insertcity(request):
    try:
        d=request.json
        print(d)
        gensql('insert','City',d)
        return(json.dumps({"Message":"Record Inserted Successfully","MessageCode":"RIS","Service Status":"Success"},indent=4))
    except:
        return("some thing went wrong in input")  


def updatecity(request):
    try:
        d=request.json
        print(d)
        id= { k : v for k,v in d.items() if k in ('city_id')}
        name= { k : v for k,v in d.items() if k not in ('city_id')}
        gensql('update','City',name,id)
        #res = dbget("")
        return(json.dumps({"Message":"Record Updated Successfully","MessageCode":"RUS","Service Status":"Success"},indent=4))
    except:
         return("some thing went wrong in update funtion")

def selectcity(request):
    try:
        d=json.loads(gensql('select','City','*'))
        return(json.dumps({"Message":"Record Selected Successfully","MessageCode":"RSS","Service Status":"Success","Output":d},indent=4))
    except:
        return("some thing went wrong in selection funtion")


def deletecity(request):
    try:
        d=request.json['city_id']
        dbput("delete from city_id where city_id='"+d+"'")
        return(json.dumps({"Message":"Record Deleted Successfully","MessageCode":"RDS","Service Status":"Success"},indent=4))
    except:
        return("some thing went wrong in delete funtion")

