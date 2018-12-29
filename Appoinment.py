from sqlwrapper import gensql,dbget,dbput
import json
import datetime
import time
from time import mktime
from flask import Flask,request,jsonify
#from datetime import datetime
def tokengeneration(request):
    try:
     
          d=request.json
          dt = datetime.datetime.strptime(d['business_date'],'%Y-%m-%d').date()   #to convert string to date format
          currenttime = datetime.datetime.now()              #to get current datetime
          todaydate = currenttime.date()
          todaytime = currenttime.strftime('%H:%M')      #to get current time
          doc_id = {k:v for k,v in d.items() if k in ('doctor_id','business_id')}
          docidval = doc_id.get("doctor_id")
          bus_id = doc_id.get("business_id")
          b = json.loads(dbget("select * from new.timing where doctor_id = '"+str(docidval)+"' and business_id = '"+str(bus_id)+"'" ))
          etime = b[0]['end_timing']                 #to get value from list
          if dt == todaydate and etime>todaytime :
               a = {k:v for k,v in d.items() if k in ('doctor_id','business_id','business_date')}
               res = json.loads(gensql('select','new.token_no','count(*)',a))
               if res[0]['count'] == 0:
                   a['token_no'] = 1
                   gensql('insert','new.token_no',a)
               token = json.loads(gensql('select','new.token_no','token_no',a))
               no = token[0]['token_no'] + 1
               d['token_no'] = no
               d['token_time'] = currenttime
               gensql('insert','new.appointment',d)
               dbput("update new.token_no set token_no ='"+str(no)+"' where doctor_id='"+str(a['doctor_id'])+"' and business_id = '"+str(bus_id)+"' ")
               return(json.dumps({'Message': 'Token Generated','MessageCode':'TGS', 'Status': 'success','Token_No':no},indent=4))
     
          else:
             return(json.dumps({"Message":"Token should be Generated only for Today Date","Message Code":"TGTD","Service Status Status":"Failure"},indent=4))
    except:
        return(json.dumps({"Message":"Token Generation UnSuccessful","Message Code":"TGUS","Service Status":"Failure"},indent=4))
            
       
def selectappointment(request):
               #try:
                   d = request.json
                   output = json.loads(dbget("select new.token_no.*,new.appointment.*,new.user_profile.* from new.appointment \
                                            join new.user_profile on new.appointment.mobile = new.user_profile.mobile\
                                           join new.token_no on new.appointment.token_no=new.token_no.token_no where\
                                           new.appointment.doctor_id = '"+str(d['doctor_id'])+"' and new.appointment.business_id = '"+str(d['business_id'])+"'\
                                           and new.appointment.business_date = '"+str(d['business_date'])+"' order by new.appointment.token_no" ))
                   return(json.dumps({"Message":"Appointments Selected Sucessfully","MessageCode":"ASS","Service Status Status":"Success","output":output},indent=4))
              # except:
                   # return(json.dumps({"Message":"Appointments Selected Unsuccessful","Message Code":"ASUS","Service Status":"Failure"},indent=4))
                                           join new.token_no on new.appointment.token_no=new.token_no.token_no where doctor_id='"+str(d['doctor_id'])+"' and business_id = '"+str(d['business_id'])+"'\
                                          order by new.appointment.token_no" ))
                   return(json.dumps({"Message":"Appointments Selected Sucessfully","MessageCode":"ASS","Service Status Status":"Success","output":output},indent=4))
               except:
                    return(json.dumps({"Message":"Appointments Selected Unsuccessful","Message Code":"ASUS","Service Status":"Failure"},indent=4))


def updatetoken(request):
     try:
          d=request.json 
          dbput("update new.appointment set token_status='"+str(d['token_status'])+"'  where appointment_id='"+str(d['appointment_id'])+"'")
          return(json.dumps({"Message":"Record Updated Successfully","MessageCode":"RUS","Service Status":"Success"},indent=4))
     except:
          return(json.dumps({"Message":"Appointments Updated Unsuccessful","Message Code":"AUUS","Service Status":"Failure"},indent=4))
def count(request):
     try:
           d=request.json
           b_count = json.loads(dbget("select count(*) as bo_count from new.appointment \
                                      where token_status='Booked' and doctor_id='"+str(d['doctor_id'])+"' and business_id = '"+str(d['business_id'])+"'\
                                       and new.appointment.business_date = '"+str(d['business_date'])+"'"))
           booked_count = b_count[0]['bo_count']
           c_count = json.loads(dbget("select count(*) as can_count from new.appointment \
                                      where token_status='Canceled' and doctor_id='"+str(d['doctor_id'])+"' and business_id = '"+str(d['business_id'])+"'\
                                       and new.appointment.business_date = '"+str(d['business_date'])+"'"))
           canceled_count = c_count[0]['can_count']
           co_count = json.loads(dbget("select count(*) as checkout_count from new.appointment \
                                      where token_status='Checkout' and doctor_id='"+str(d['doctor_id'])+"' and business_id = '"+str(d['business_id'])+"' \
                                      and new.appointment.business_date = '"+str(d['business_date'])+"'"))
           cheout_count = co_count[0]['checkout_count']
           return(json.dumps({"Message":"Token number Counted  Sucessfully","MessageCode":"TNS","Service Status":"Success"
                               ,"booked_count":booked_count,"canceled_count":canceled_count,"Checked_out":cheout_count},indent=4))
     except:
          return(json.dumps({"Message":"Token number Counted Unsuccessful","Message Code":"TNUS","Service Status":"Failure"},indent=4))
def livefeed(request):
     try:
          d = request.json
          output = json.loads(dbget("select new.token_no.*,new.appointment.*,new.user_profile.* from new.appointment \
                                join new.user_profile on new.appointment.mobile = new.user_profile.mobile \
                               join new.token_no on new.appointment.token_no=new.token_no.token_no where new.appointment.doctor_id='"+str(d['doctor_id'])+"' and new.appointment.business_id = '"+str(d['business_id'])+"'\
                                and new.appointment.business_date = '"+str(d['business_date'])+"' order by new.appointment.token_no desc limit 4"))
          return(json.dumps({"message":"livefeed Successful","Message Code":"LS","output":output},indent = 4))
     except:
          return(json.dumps({"Message":"Livefeed Unsuccessful","Message Code":"LUS","Service Status":"Success"},indent=4))
                 

                 
                 
                 


