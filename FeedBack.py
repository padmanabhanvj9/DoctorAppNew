from sqlwrapper import gensql,dbget,dbput
import json
import datetime
from flask import Flask,request,jsonify


def Insert_FeedBack(request):
    try:
        d=request.json
        d['time'] = datetime.datetime.now()
        
        print(d)
        gensql('insert','new.FeedBack',d)
        return(json.dumps({"Message":"Record Inserted Successfully","Message_Code":"RIS","Service_Status":"Success"},indent=4))
    except:
        return(json.dumps({"Message":"Record Inserted UnSuccessfull","Message_Code":"RIUS","Service_Status":"Failure"},indent=4))

def Select_FeedBack(request):
    try:
        d=request.json
        print('mohan',d)
        d1=json.loads(gensql('select','new.FeedBack','*',d))
        return(json.dumps({"Message":"Record Selected Successfully","Message_Code":"RSS","Service_Status":"Success","output":d1},indent=4))
    except:
        return(json.dumps({"Message":"Record Selected UnSuccessfull","Message_Code":"RSUS","Service_Status":"Failure"},indent=4))
    

def Update_FeedBack(request):
      try:
          d=request.json
          print(d)
          e= { k : v for k,v in d.items() if k in ('feedback_id')}
          a= { k : v for k,v in d.items() if k not in ('feedback_id')}
    
          gensql('update','new.FeedBack',a,e)
          #res = dbget("")
          return(json.dumps({"Message":"Record Updated Successfully","Message_Code":"RUS","Service_Status":"Success"},indent=4))
      except:
          return(json.dumps({"Message":"Recored Updated UnSuccessfully","Message_Code":"RUUS","Service":"UnSuccess"},indent=4))
    


def Delete_FeedBack(request):
    try:
        d=request.json['feedback_id']
        dbput("delete from new.FeedBack where FeedBack_Id='"+d+"'")
        return(json.dumps({"Message":"Record Deleted Successfully","Message_Code":"RDS","Service_Status":"Success"},indent=4))
    except:
        return(json.dumps({"Message":"Record Deleted UnSuccessfully","Message_Code":"RDUS","Service_Status":"UnSuccess"},indent=4)) 

