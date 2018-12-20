from flask import Flask,request,jsonify
from sqlwrapper import gensql,dbget,dbput
import json
def InsertBusinessType(request):
    try:
        d=request.json
        print(d)
        gensql('insert','Business_Type',d)
        return(json.dumps({"Message":"Record Inserted Successfully","MessageCode":"RIS","Service":"Success"},indent=4))
    except:
        return("some thing went wrong in input")
def UpdateBusinessType(request):
     try:
         d=request.json
         name = { k : v for k,v in d.items() if k not in ('BusinessType_Id')}
         id={ k : v for k,v in d.items() if k in ('BusinessType_Id')}
         gensql('update','Business_Type',name,id)
         return(json.dumps({"Message":"Record Updated Successfully","MessageCode":"RUS","Service":"Success"},indent=2))
     except:
         return("some thing went wrong in input")

def SelectBusinessType(request):
    try:
        res=json.loads(gensql('select','Business_Type','*'))
        return(json.dumps({"Message":"Record Selected Successfully","MessageCode":"RSS","Service":"Success","output":res},indent=2))
    except:
        return("some thing went wrong in input")           

def DeleteBusinessType(request):
    try:
        res=request.json['BusinessType_Id']
        dbput("delete from Business_Type where BusinessType_Id='"+res+"'")
        return(json.dumps({"Message":"Record Deleted Successfully","MessageCode":"RDS","Service Status":"Success"},indent=4))
    except:
         return("some thing went wrong in input")

