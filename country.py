from sqlwrapper import gensql,dbget,dbput
import json
import datetime
from flask import Flask,request,jsonify

def Insert_Country(request):
    try:
        d=request.json
       
        
        print(d)
        gensql('insert','new.country',d)
        return(json.dumps({"Message":"Record Inserted Successfully","MessageCode":"RIS","Service Status":"Success"},indent=4))
    except:
        return(json.dumps({"Message":"Record Inserted UnSuccessfull","MessageCode":"RIUS","Service Status":"Failure"},indent=4))

def Select_Country(request):
    try:
        
        d1=json.loads(gensql('select','new.country','*'))
        return(json.dumps({"Message":"Record Selected Successfully","MessageCode":"RSS","Service Status":"Success","output":d1},indent=4))
    except:
        return(json.dumps({"Message":"Record Selected UnSuccessfull","MessageCode":"RSUS","Service Status":"Failure"},indent=4))
    

def Update_Country(request):
      try:
          d=request.json
          print(d)
          e= { k : v for k,v in d.items() if k in ('country_id')}
          a= { k : v for k,v in d.items() if k not in ('country_id')}
    
          gensql('update','new.country',a,e)
          #res = dbget("")
          return(json.dumps({"Message":"Record Updated Successfully","MessageCode":"RUS","Service Status":"Success"},indent=4))
      except:
          return(json.dumps({"Message":"Recored Updated UnSuccessfully","MessageCode":"RUUS","Service":"UnSuccess"},indent=4))
    




