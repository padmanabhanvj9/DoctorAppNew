import json
from flask import Flask,request,jsonify
import datetime
from sqlwrapper import gensql,dbget,dbput
def insertuser_profile(request):
    try:
        a=request.json
    
        b = {k : v for k,v in a.items() if k in ('user_name','mobile')}
        print(b)
        print(len(b))
        if len(b) != 2:
            return(json.dumps({"ServiceStatus":"Failure","ServiceMessage":"Failure"},indent=4))
    
            gensql('insert','new.user_profile',a)
        return(json.dumps({"Message":"Record Inserted Successfully","MessageCode":"RIS","Service":"Success"},indent=4))
    except:
        return(json.dumps({"Message":"Record Inserted UnSuccessfully","MessageCode":"RIUS","Service":"UnSuccess"},indent=4))
    
    
def updateuser_profile(request):
    try:
        a=request.json
        b={k : v for k,v in a.items() if k in ('mobile')}
        c={ k : v for k,v in a.items() if k  not in('mobile')}
        gensql('update','new.user_profile',c,b)
        return(json.dumps({"Message":"Recored Updated Successfully","MessageCode":"RUS","Service":"Success"},indent=4))
        
    except:
        return(json.dumps({"Message":"Recored Updated UnSuccessfully","MessageCode":"RUUS","Service":"UnSuccess"},indent=4))
def selectuser_profile(request):
    try:
        if request.method == 'GET':
            res=json.loads(gensql('select','new.user_profile','*'))
        elif request.method == 'POST':
            d = request.json
            print(d)
            res=json.loads(dbget("select * from new.user_profile where mobile = '"+str(d['mobile'])+"'"))
            print(res)
        
        return(json.dumps({"Message":"Recored Selected Successfully","MessageCode":"RSS","Service":"Success","output":res},indent=4))


    except:
        return(json.dumps({"Message":"Recored Selected UnSuccessfully","MessageCode":"RSUS","Service":"UnSuccess"},indent=4))
def deleteuser_profile(request):
    try:
        d=request.json['user_id']
        dbput("delete from new.User_Profile where user_id='"+str(d)+"'")
        return(json.dumps({"Message":"Record Deleted Successfully","MessageCode":"RDS","Service Status":"Success"},indent=4))


    except:
        return(json.dumps({"Message":"Record Deleted UnSuccessfully","MessageCode":"RDUS","Service Status":"UnSuccess"},indent=4)) 

        
        
           

                  
