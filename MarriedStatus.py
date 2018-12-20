from sqlwrapper import gensql,dbget,dbput
import json
import datetime
from flask import Flask,request,jsonify
def Insert_Married_Status(request):
    try:
        d= request.json
        gensql('insert','Married_Status',d)
        return(json.dumps({"Message":"Record Inserted Successfully","MessageCode":"RIS","Service Status":"Success"},indent=2))
    except:
        return("some thing went wrong in input")  



def Update_Married_Status(request):
    try:
        d= request.json
        a= { k : v for k,v in d.items() if k not in ('Married_Status_Id')}
        e= { k : v for k,v in d.items() if k in ('Married_Status_Id')}

        gensql('update','Married_Status',a,e)
        return(json.dumps({"Message":"Record Updated Successfully","MessageCode":"RUS","Service Status":"Success"},indent=2))
    except:
        return("some thing went wrong in update function")  


def Select_Married_Status(request):
     try:
         c=json.loads(gensql('select','Married_status','*'))
         return (json.dumps({"Message":"Record Selected Successfully","MessageCode":"RSS","Service Status":"Success","Output":c},indent=2))
     except:
        return("some thing went wrong in select function")  




def Delete_Married_Status(request):
    try:
        d=request.json['Married_Status_Id']
        dbput("delete from Married_Status where Married_Status_Id='"+d+"'")
        return(json.dumps({"Message":"Record Deleted Successfully","MessageCode":"RDS","Service Status":"Success"},indent=4))
    except:
        return("some thing went wrong in select function")  


