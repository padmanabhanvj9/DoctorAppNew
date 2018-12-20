from sqlwrapper import gensql,dbget,dbput
import json
import random
import datetime
from flask import Flask,request,jsonify
def insertbloodgroup(request):
    try:
         d=request.json
         print(d)
         gensql('insert','Blood_Group',d)
         return(json.dumps({"Message":"Record Inserted Successfully","MessageCode":"RIS","Service Status":"Success"},indent=4))
    except:
         return("some thing went wrong in input")  


def updatebloodgroup(request):
     try:
          d=request.json
          a = { k : v for k,v in d.items() if k not in ('Blood_Group_Id')}
          e={ k : v for k,v in d.items() if k in ('Blood_Group_Id')}
          gensql('update','Blood_Group',a,e)
          return(json.dumps({"Message":"Record Updated Successfully","MessageCode":"RUS","Service Status":"Success"},indent=4))
     except:
         return("some thing went wrong in given Id please give the valid id")  

     


def selectbloodgroup(request):
     try:
     
          d=json.loads(gensql('select','Blood_Group','*'))
          return(json.dumps({"Message":"Record Selected Successfully","MessageCode":"RSS","Service Status":"Success","Output":d},indent=4))
     except:
         return("some thing went wrong in select function ")  



def deletebloodgroup(request):
     try:
         d=request.json['Blood_Group_Id']
         dbput("delete from Blood_Group where Blood_Group_Id='"+d+"'")
         return(json.dumps({"Message":"Record Deleted Successfully","MessageCode":"RDS","Service Status":"Success"},indent=4))
     except:
         return("some thing went wrong in Delete function ")  

     
