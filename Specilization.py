from flask import Flask,request,jsonify
from sqlwrapper import gensql,dbget,dbput
import json
def insertspecialization(request):
    try:
        d=request.json
        print(d)
        gensql('insert','Specilization',d)
        return(json.dumps({"Message":"Record Inserted Successfully","Message Code":"RIS","Service Status":"Success"},indent=4))
    except:
        return("some thing went wrong in input")  

def updatespecialization(request):
    try:
        d=request.json
        a= { k : v for k,v in d.items() if k not in ('Specilization_Id')}
        e={ k : v for k,v in d.items() if k in ('Specilization_Id')}
        gensql('update','Specilization',a,e)
        return(json.dumps({"Message":"Record Updated Successfully","Message Code":"RUS","Service Status":"Success"},indent=4))
    except:
        return("some thing went wrong in specialization update funtion")
    


def selectspecialization(request):
    try:
        d=json.loads(gensql('select','Specilization','*'))
        return(json.dumps({"Message":"Record Selected Successfully","Message Code":"RSS","Service Status":"Success","output":d},indent=4))
    except:
         return("some thing went wrong in specialization select funtion")
    
           

def deletespecialization(request):
    try:
        d=request.json['Specilization_Id']
        dbput("delete from Specilization where Specilization_Id='"+d+"'")
        return(json.dumps({"Message":"Record Deleted Successfully","Message Code":"RDS","Service Status":"Success"},indent=4))
    except:
         return("some thing went wrong in specialization update")

