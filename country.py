from sqlwrapper import gensql,dbget,dbput
import json
import re
from flask import Flask,request,jsonify

def Insert_Country(request):
    try:
        d=request.json
        e = request.json['country_name']
        country_name = json.loads(dbget("select count(*) as country_name from new.country where country_name ='"+str(d['country_name'])+"'"))
        if country_name[0]['country_name'] == 1:
            return(json.dumps({"Message":"Already Exists","Message_Code":"AE","Service_Status":"Failure"},indent=4))
        x = re.findall("[a-zA-Z]", e)
        if (x):
            gensql('insert','new.country',d)
            return(json.dumps({"Message":"Record Inserted Successfully","Message_Code":"RIS","Service_Status":"Success"},indent=4))
        else:
            return(json.dumps({"Message":"Invalid Input","Message_Code":"II","Service_Status":"Failure"},indent=4))
    except:
       return(json.dumps({"Message":"Record Inserted UnSuccessfull","Message_Code":"RIUS","Service_Status":"Failure"},indent=4))

def Select_Country(request):
    try:
        d1 = json.loads(gensql('select','new.country','*'))
        return(json.dumps({"Message":"Record Selected Successfully","Message_Code":"RSS","Service_Status":"Success","output":d1},indent=4))
    except:
        return(json.dumps({"Message":"Record Selected UnSuccessfull","Message_Code":"RSUS","Service_Status":"Failure"},indent=4))
    

def Update_Country(request):
      try:
          d=request.json
          e= { k : v for k,v in d.items() if k in ('country_id')}
          a= { k : v for k,v in d.items() if k not in ('country_id')}
          country = json.loads(dbget("select count(*) as country_id from new.country where country_id ='"+str(d['country_id'])+"'"))
          if country[0]['country_id'] == 1:
              gensql('update','new.country',a,e)
              return(json.dumps({"Message":"Record Updated Successfully","Message_Code":"RUS","Service_Status":"Success"},indent=4))
          else:
             return(json.dumps({"Message":"Invalid Country_Id ","Message_Code":"ICI","Service_Status":"Failure"},indent=4))
      except:
          return(json.dumps({"Message":"Recored Updated UnSuccessfully","Message_Code":"RUUS","Service":"Failure"},indent=4))
    




