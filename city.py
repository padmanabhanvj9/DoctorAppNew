from sqlwrapper import gensql,dbget,dbput
import json
import re
from flask import Flask,request,jsonify

def InsertCity(request):
    try:
        d=request.json
        e = request.json['city_name']
        regex = re.compile('[a-zA-Z]')
        city_name = json.loads(dbget("select count(*) as city_name from new.city where city_name ='"+e+"'"))
        if city_name[0]['city_name'] == 1:
            return(json.dumps({"Message":"Already Exists","Message_Code":"AE","Service_Status":"Failure"},indent=4))
            
        if  regex.match(e):
            gensql('insert','new.city',d)
            return(json.dumps({"Message":"Record Inserted Successfully","Message_Code":"RIS","Service_Status":"Success"},indent=4))
        else:
            return(json.dumps({"Message":"Invalid Input","Message_Code":"II","Service_Status":"Failure"},indent=4))
    except:
       return(json.dumps({"Message":"Record Inserted UnSuccessfull","Message_Code":"RIUS","Service_Status":"Failure"},indent=4))

def SelectCity(request):
    try:
        d1 = json.loads(gensql('select','new.city','*'))
        return(json.dumps({"Message":"Record Selected Successfully","Message_Code":"RSS","Service_Status":"Success","output":d1},indent=4))
    except:
        return(json.dumps({"Message":"Record Selected UnSuccessfull","Message_Code":"RSUS","Service_Status":"Failure"},indent=4))
    

def UpdateCity(request):
    try:
        d=request.json
        e= { k : v for k,v in d.items() if k in ('city_id')}
        a= { k : v for k,v in d.items() if k not in ('city_id')}
        city = json.loads(dbget("select count(*) city_id from new.city where city_id ='"+str(d['city_id'])+"'"))
        if city[0]['city_id'] == 1:
            gensql('update','new.city',a,e)
            return(json.dumps({"Message":"Record Updated Successfully","Message_Code":"RUS","Service_Status":"Success"},indent=4))
        else:
            return(json.dumps({"Message":"Invalid city_id ","Message_Code":"ICI","Service_Status":"Failure"},indent=4))
    except:
          return(json.dumps({"Message":"Recored Updated UnSuccessfully","Message_Code":"RUUS","Service":"Failure"},indent=4))


def deleteCity(request):
    try:
        d=request.json['city_id']
        dbput("delete from new.city where city_id='"+d+"'")
        return(json.dumps({"Message":"Record Deleted Successfully","Message_Code":"RDS","Service_Status":"Success"},indent=4))
    except:
        return(json.dumps({"Message":"Record Deleted UnSuccessful","Message_Code":"RDUS","Service_Status":"Failure"},indent=4))


    




