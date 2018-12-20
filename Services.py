from flask import Flask,request,jsonify
from sqlwrapper import gensql,dbget,dbput
import json
def insertservices(request):
    try:
        d=request.json
        print(d)
        gensql('insert','Services',d)
        return(json.dumps({"Message":"Record Inserted Successfully","Message Code":"RIS","Service Status":"Success"},indent=4))
    except:
        return("some thing went wrong in input")  



def updateservices(request):
     try:
         d=request.json
         a = { k : v for k,v in d.items() if k not in ('Service_Id')}
         e={ k : v for k,v in d.items() if k in ('Service_Id')}
         gensql('update','Services',a,e)
         return(json.dumps({"Message":"Record Updated Successfully","Message Code":"RUS","Service Status":"Success"},indent=4))
     except:
         return("some thing went wrong in update service function")  


def selectservices(request):
      try:
          d=json.loads(gensql('select','Services','*'))
          return(json.dumps({"Message":"Record Selected Successfully","Message Code":"RSS","Service Status":"Success","output":d},indent=4))
      except:
         return("some thing went wrong in select service function")
           

def deleteservices(request):
    try:
        d=request.json['Service_Id']
        dbput("delete from Services where Service_Id='"+d+"'")
        return(json.dumps({"Message":"Record Deleted Successfully","Message Code":"RDS","Service Status":"Success"},indent=4))
    except:
         return("some thing went wrong in select service function")
           
    

