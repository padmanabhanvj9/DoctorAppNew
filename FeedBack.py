from sqlwrapper import gensql,dbget,dbput
import json
import datetime
from flask import Flask,request,jsonify


def Insert_FeedBack(request):
    try:
        d=request.json
        d['fb_time'] = datetime.datetime.now()
        print(d)
        gensql('insert','FeedBack',d)
        return(json.dumps({"Message":"Record Inserted Sucessfully","MessageCode":"Ris","Service Status":"Success"},indent=4))
    except:
        return("some thing went wrong in insert  funtion")

def Select_FeedBack(request):
    try:
        d=json.loads(gensql('select','FeedBack','*'))
        return(json.dumps({"Message":"Record Selected Sucessfully","MessageCode":"Rss","Service Status":"Success","output":d},indent=4))
    except:
        return("some thing went wrong in select  funtion")
    

def Update_FeedBack(request):
      try:
          d=request.json
          print(d)
          e= { k : v for k,v in d.items() if k in ('feedback_id')}
          a= { k : v for k,v in d.items() if k not in ('feedback_id')}
    
          gensql('update','FeedBack',a,e)
          #res = dbget("")
          return(json.dumps({"Message":"Record Updated Successfully","MessageCode":"RUS","Service Status":"Success"},indent=4))
      except:
          return("some thing went wrong in update  funtion")
    


def Delete_FeedBack(request):
    try:
        d=request.json['feedback_id']
        dbput("delete from FeedBack where FeedBack_Id='"+d+"'")
        return(json.dumps({"Message":"Record Deleted Successfully","MessageCode":"RDS","Service Status":"Success"},indent=4))
    except:
        return("some thing went wrong in delete funtion")

