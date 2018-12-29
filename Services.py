from flask import Flask,request,jsonify
from sqlwrapper import gensql,dbget,dbput
import json
def insertservices(request):
    try:
        d=request.json
        gensql('insert','new.services',d)
        return(json.dumps({"Message":"Record Inserted Successfully","Message Code":"RIS","Service Status":"Success"},indent=4))
    except:
        return(json.dumps({"Message":"Record Inserted UnSuccessful","Message Code":"RIUS","Service Status":"Success"},indent=4))  



def updateservices(request):
     try:
         d=request.json
         a = { k : v for k,v in d.items() if k not in ('service_id')}
         e={ k : v for k,v in d.items() if k in ('service_id')}
         gensql('update','new.services',a,e)
         return(json.dumps({"Message":"Record Updated Successfully","Message Code":"RUS","Service Status":"Success"},indent=4))
     except:
         return(json.dumps({"Message":"Record Updated UnSuccessful","Message Code":"RUUS","Service Status":"Failure"},indent=4))  


def selectservices(request):
      try:
          d=json.loads(gensql('select','new.services','*'))
          return(json.dumps({"Message":"Record Selected Successfully","Message Code":"RSS","Service Status":"Success","output":d},indent=4))
      except:
         return(json.dumps({"Message":"Record Selected UnSuccessful","Message Code":"RSUS","Service Status":"Failure"},indent=4))
           

def deleteservices(request):
    try:
        d=request.json['service_id']
        dbput("delete from new.services where service_id='"+d+"'")
        return(json.dumps({"Message":"Record Deleted Successfully","Message Code":"RDS","Service Status":"Success"},indent=4))
    except:
         return(json.dumps({"Message":"Record Deleted UnSuccessful","Message Code":"RDUS","Service Status":"Failure"},indent=4))
           
    

