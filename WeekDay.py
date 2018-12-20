from sqlwrapper import gensql,dbget,dbput
import json
import datetime
from flask import Flask,request,jsonify


def Insert_Week_Day(request):
    try:
        d=request.json
        print(d)
        gensql('insert','Week_Day',d)
        return(json.dumps({"Message":"Record Inserted Sucessfully","MessageCode":"RIS","Service Status":"Success"},indent=4))
    except:
        return("some thing went wrong in input")  


def Select_Week_Day(request):
    try:
        d=json.loads(gensql('select','Week_Day','*'))
        return(json.dumps({"Message":"Record Selected Sucessfully","MessageCode":"RSS","Service Status":"Success","output":d},indent=4))
    except:
        return("some thing went wrong in select weekday function")  


def Update_Week_Day(request):
    try:
        d=request.json
        print(d)
        e= { k : v for k,v in d.items() if k in ('day_id')}
        a= { k : v for k,v in d.items() if k not in ('day_id')}
        
        gensql('update','Week_Day',a,e)
        #res = dbget("")
        return(json.dumps({"Message":"Record Updated Successfully","MessageCode":"RUS","Service Status":"Success"},indent=4))

           
    except:
        return("some thing went wrong in update weekday function")  
    


def Delete_Week_Day(request):
    try:
        d=request.json['day_id']
        dbput("delete from Week_Day where Day_Id='"+d+"'")
        return(json.dumps({"Message":"Record Deleted Successfully","MessageCode":"RDS","Service Status":"Success"},indent=4))
    except:
        return("some thing went wrong in delete weekday function")  
    


