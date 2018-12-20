from flask import Flask,request,jsonify
from sqlwrapper import gensql,dbget,dbput
import json
def insertstatus(request):
    try:
        d=request.json
        gensql('insert','Token_Status',d)
        return(json.dumps({"Message":"Record Inserted Successfully","Message Code":"RIS","Service Status":"Success"},indent=4))
    except:
        return("some thing went wrong in input")  


def updatestatus(request):
    try:
        d=request.json
        a= { k : v for k,v in d.items() if k not in ('Status_Id')}
        e={ k : v for k,v in d.items() if k in ('Status_Id')}
        gensql('update','Token_Status',a,e)
        return(json.dumps({"Message":"Record Updated Successfully","Message Code":"RUS","Service Status":"Success"},indent=4))
    except:
        return("some thing went wrong in updatestatus function")  


def selectstatus(request):
    try:
        d=json.loads(gensql('select','Token_Status','*'))
        return(json.dumps({"Message":"Record Selected Successfully","Message Code":"RSS","Service Status":"Success","output":d},indent=4))
    except:
        return("some thing went wrong in selectstatus function")  

    
           

def deletestatus(request):
     try:
         d=request.json['Status_Id']
         dbput("delete from Token_Status where Status_Id='"+d+"'")
         return(json.dumps({"Message":"Record Deleted Successfully","Message Code":"RDS","Service Status":"Success"},indent=4))
     except:
         return("some thing went wrong in selectstatus function")  
        
