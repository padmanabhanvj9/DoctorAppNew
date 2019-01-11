from flask import Flask,request,jsonify
from sqlwrapper import gensql,dbget,dbput
import json
def insertservices(request):
    try:
        d=request.json
        e = request.json['service_name']
        regex = re.compile('[a-zA-Z]')
        Service_Name = json.loads(dbget("select count(*) as Service_Name from new.services where service_name ='"+str(d['service_name'])+"'"))
        if Service_Name[0]['service_name'] == 1:
            return(json.dumps({"Message":"Already Exists","Message_Code":"AE","Service_Status":"Failure"},indent=4))
        if regex.match(e):
            gensql('insert','new.services',d)
            return(json.dumps({"Message":"Record Inserted Successfully","Message_Code":"RIS","Service_Status":"Success"},indent=4))
        else:
            return(json.dumps({"Message":"Invalid Input","Message_Code":"II","Service_Status":"Failure"},indent=4))
    except:
       return(json.dumps({"Message":"Record Inserted UnSuccessfull","Message_Code":"RIUS","Service_Status":"Failure"},indent=4))

def selectservices(request):
    try:
        d1 = json.loads(gensql('select','new.services','*'))
        return(json.dumps({"Message":"Record Selected Successfully","Message_Code":"RSS","Service_Status":"Success","output":d1},indent=4))
    except:
        return(json.dumps({"Message":"Record Selected UnSuccessfull","Message_Code":"RSUS","Service_Status":"Failure"},indent=4))
def updateservices(request):
      try:
          d=request.json
          e= { k : v for k,v in d.items() if k in ('service_id')}
          a= { k : v for k,v in d.items() if k not in ('service_id')}
          country = json.loads(dbget("select count(*) service_id from new.services where service_id ='"+str(d['service_id'])+"'"))
          if country[0]['service_id'] == 1:
              gensql('update','new.services',a,e)
              return(json.dumps({"Message":"Record Updated Successfully","Message_Code":"RUS","Service_Status":"Success"},indent=4))
          else:
             return(json.dumps({"Message":"Invalid service_id ","Message_Code":"ICI","Service_Status":"Failure"},indent=4))
      except:
          return(json.dumps({"Message":"Recored Updated UnSuccessfully","Message_Code":"RUUS","Service":"Failure"},indent=4))
def deleteservices(request):
    try:
        d=request.json['service_id']
        dbput("delete from new.services where service_id='"+d+"'")
        return(json.dumps({"Message":"Record Deleted Successfully","Message_Code":"RDS","Service_Status":"Success"},indent=4))
    except:
         return(json.dumps({"Message":"Record Deleted UnSuccessful","Message_Code":"RDUS","Service_Status":"Failure"},indent=4))

