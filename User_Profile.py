import json
from flask import Flask,request,jsonify
import re
from sqlwrapper import gensql,dbget,dbput
def insertuser_profile(request):
    try:
        a=request.json
        b = {k : v for k,v in a.items() if k in ('user_name','mobile')}
        if len(b) != 2:
            return(json.dumps({"Message":"Mobile Number and Name not Given","Service_Status":"Failure","Message_Code":"MNNG"},indent=4))
        def isValid(d):
            Pattern = re.compile("[6-9][0-9]{9}")
            return Pattern.match(d)
        d = a['mobile']
        mob_validate = isValid(d)
        if b['mobile'] == ''or mob_validate == None :
           return(json.dumps({"Message":"Invalid Mobile Number ","Service_Status":"Failure","Message_Code":"IMN"},indent=4)) 
        gensql('insert','new.user_profile',a)
        return(json.dumps({"Message":"Record Inserted Successfully","Message_Code":"RIS","Service":"Success"},indent=4))
    except:
        return(json.dumps({"Message":"Record Inserted UnSuccessfully","Message_Code":"RIUS","Service":"UnSuccess"},indent=4))
    
    
def updateuser_profile(request):
    try:
        a=request.json
        mob = json.loads(dbget("select count(*) as mobile from new.user_profile where mobile ='"+a['mobile']+"'"))
        print(mob[0]['mobile'])
        if mob[0]['mobile'] == 0:
             return(json.dumps({'Message': 'Invalid Data', 'MessageCode': 'ID', 'Status': 'Failure',},indent=4))
        else:
            b={k : v for k,v in a.items() if k in ('mobile')}
            c={ k : v for k,v in a.items() if k  not in('mobile')}
            gensql('update','new.user_profile',c,b)
            return(json.dumps({"Message":"Recored Updated Successfully","Message_Code":"RUS","Service":"Success"},indent=4))
    except:
       return(json.dumps({"Message":"Recored Updated UnSuccessfully","Message_Code":"RUUS","Service":"UnSuccess"},indent=4))
def selectuser_profile(request):
    try:
        if request.method == 'GET':
            res=json.loads(gensql('select','new.user_profile','*'))
        elif request.method == 'POST':
            d = request.json
            mob = json.loads(dbget("select count(*) as mobile from new.user_profile where mobile ='"+str(d['mobile'])+"'"))
            if mob[0]['mobile'] == 0:
                return(json.dumps({'Message': 'Invalid Data', 'Message_Code': 'ID', 'Status': 'Failure',},indent=4))
            else:
                res=json.loads(dbget("select * from new.user_profile where mobile = '"+str(d['mobile'])+"'"))
                return(json.dumps({"Message":"Recored Selected Successfully","Message_Code":"RSS","Service":"Success","output":res},indent=4))
    except:
         return(json.dumps({"Message":"Recored Selected UnSuccessfully","Message_Code":"RSUS","Service":"UnSuccess"},indent=4))
def deleteuser_profile(request):
    try:
        d=request.json['user_id']
        dbput("delete from new.User_Profile where user_id='"+str(d)+"'")
        return(json.dumps({"Message":"Record Deleted Successfully","Message_Code":"RDS","Service_Status":"Success"},indent=4))


    except:
        return(json.dumps({"Message":"Record Deleted UnSuccessfully","Message_Code":"RDUS","Service_Status":"UnSuccess"},indent=4)) 

        
        
           

                  
