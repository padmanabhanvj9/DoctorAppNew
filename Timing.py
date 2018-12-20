from sqlwrapper import gensql,dbget,dbput
import json
import datetime
from flask import Flask,request,jsonify


def Insert_Timing(request):
     try:
         d=request.json
         print(d)
         gensql('insert','Timing',d)
         return(json.dumps({"Message":"Record Inserted Sucessfully","MessageCode":"RIS","Service Status":"Success"},indent=4))
     except:
         return("some thing went wrong in input timing")  



def Select_Timing(request):
    try:
        d=json.loads(gensql('select','Timing','*'))
        return(json.dumps({"Message":"Record Selected Sucessfully","MessageCode":"RSS","Service Status":"Success","output":d},indent=4))
    except:
         return("some thing went wrong in select timing function")  



def Update_Timing(request):
    try:
        d=request.json
        print(d)
        e= { k : v for k,v in d.items() if k in ('timing_id')}
        a= { k : v for k,v in d.items() if k not in ('timing_id')}
    
        gensql('update','Timing',a,e)
        #res = dbget("")
        return(json.dumps({"Message":"Record Updated Successfully","MessageCode":"RUS","Service Status":"Success"},indent=4))
    except:
         return("some thing went wrong in update timing function")  



def Delete_Timing(request):
    try:
        d=request.json['timing_id']
        dbput("delete from Timing where timing_id='"+d+"'")
        return(json.dumps({"Message":"Record Deleted Successfully","MessageCode":"RDS","Service Status":"Success"},indent=4))
    except:
         return("some thing went wrong in delete timing function")  

