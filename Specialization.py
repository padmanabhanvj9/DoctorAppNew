from flask import Flask,request,jsonify
from sqlwrapper import gensql,dbget,dbput
import json
def insertspecialization(request):
    try:
        d=request.json
        gensql('insert','new.specialization',d)
        return(json.dumps({"Message":"Record Inserted Successfully","Message Code":"RIS","Service Status":"Success"},indent=4))
    except:
        return(json.dumps({"Message":"Record Inserted UnSuccessful","Message Code":"RIUS","Service Status":"Failure"},indent=4))  

def updatespecialization(request):
    try:
        d=request.json
        a= { k : v for k,v in d.items() if k not in ('specialization_id')}
        e={ k : v for k,v in d.items() if k in ('specialization_id')}
        gensql('update','new.specialization',a,e)
        return(json.dumps({"Message":"Record Updated Successfully","Message Code":"RUS","Service Status":"Success"},indent=4))
    except:
        return(json.dumps({"Message":"Record Updated UnSuccessful","Message Code":"RUUS","Service Status":"Failure"},indent=4))
    


def selectspecialization(request):
    try:
        d=json.loads(gensql('select','new.specialization','*'))
        return(json.dumps({"Message":"Record Selected Successfully","Message Code":"RSS","Service Status":"Success","output":d},indent=4))
    except:
         return(json.dumps({"Message":"Record Selected UnSuccessful","Message Code":"RSUS","Service Status":"Failure"},indent=4))
    
           

def deletespecialization(request):
    try:
        d=request.json['specialization_id']
        dbput("delete from new.specialization where specialization_id='"+d+"'")
        return(json.dumps({"Message":"Record Deleted Successfully","Message Code":"RDS","Service Status":"Success"},indent=4))
    except:
         return(json.dumps({"Message":"Record Deleted UnSuccessful","Message Code":"RDUS","Service Status":"Failure"},indent=4))

