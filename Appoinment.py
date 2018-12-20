from sqlwrapper import gensql,dbget,dbput
import json
import datetime
from flask import Flask,request,jsonify
#from datetime import datetime

def tokengeneration(request):
     try:
          d=request.json
          dt = datetime.datetime.strptime(d['appointment_date'],'%Y-%m-%d').date()   #to convert string to date format
          currenttime = datetime.datetime.now()              #to get current datetime
          todaydate = currenttime.date()
          todaytime = currenttime.time()                    #to get current time
          day_id = currenttime.strftime("%w")               #to get current day_id
          doc_id = {k:v for k,v in d.items() if k in ('doctor_id')}
          docidval = doc_id.get("doctor_id")
          b = json.loads(dbget("select * from timing join week_day on\
                timing.day_id = week_day.day_id where doctor_id = '"+str(docidval)+"' and week_day_id = '"+str(day_id)+"'" ))
          etime = b[0]['ed_time']                 #to get value from list
          edconv = datetime.datetime.strptime(etime,"%H%M%S").time()            #to convert string to time format
          if dt == todaydate and edconv>todaytime :
               a = {k:v for k,v in d.items() if k in ('doctor_id','appointment_date')}
               res = json.loads(gensql('select','token_no','count(*)',a))
               print(res,len(res),type(res))     
               if res[0]['count'] == 0:
                   a['token_no'] = 0
                   gensql('insert','token_no',a)
               token = json.loads(gensql('select','token_no','token_no',a))
               no = token[0]['token_no'] + 1
               d['token_no'] = no
               #time=datetime.datetime.now()
              # d['token_time']=time.strftime("%X")
               d['token_time'] = currenttime
               d['token_status_id'] = 1
               gensql('insert','appointment',d)
               doctor_id = request.json['doctor_id']
               business_id = request.json['business_id']
               wt = json.loads(dbget("select average_wait_time from doctorinbusiness where doctor_id='"+str(doctor_id)+"' and business_id='"+str(business_id)+"'"))
               waittime = wt[0]['average_wait_time']
               print(waittime,type(waittime))
               if no ==1:
                    avg_wait=0
               else:
                    avg_wait = (no-1)*waittime
               dbput("update token_no set token_no ='"+str(no)+"' where doctor_id='"+str(d['doctor_id'])+"' and appointment_date = '"+str(a['appointment_date'])+"' ")
               
               return(json.dumps({'Message': 'Token Generated','MessageCode':'TGS', 'Status': 'success','Token_No':no,"Average_wait_time":avg_wait},indent=4))
     
          else:
           return(json.dumps({"Message":"Token should be generated only for today date","Service Status":"Failure",},indent=4))
     except:
          return("something went wrong")     
def selectappoinment(request):
     try:
         d=json.loads(gensql('select','appointment','*'))
         return(json.dumps({"Message":"Record Selected Sucessfully","MessageCode":"RSS","Service Status":"Success","output":d},indent=4))
     except:
          return("something went wrong")
def orderby(request):
     try:
          d = request.json
          print("d",d)
          #a = {k:v for k,v in d.items() if k in ('doctor_id','appointment_date')}
          #print(a)
          output = json.loads(dbget("select appointment.appointment_id,appointment.doctor_id,appointment.token_no,appointment.token_time,\
                                    token_status.status_id,token_status.status_name,user_profile.mobile,user_profile.user_name,user_profile.email,user_profile.birthday,\
                                    user_profile.city_id,user_profile.login_status_id,user_profile.emergency_contact_name,user_profile.emergency_contact_mobile\
                                    from appointment join user_profile on appointment.user_id=user_profile.mobile \
                                    join token_status on appointment.token_status_id=token_status.status_id\
                                   where doctor_id='"+str(d['doctor_id'])+"' and business_id = '"+str(d['business_id'])+"' order by token_no " ))
          #print("output",output)
          return(json.dumps({"Message":"Token number Ordered  Sucessfully","MessageCode":"TNS","Service Status":"Success","output":output},indent=4))
     except:
          return("something went wrong")


def updatetoken(request):
     try:
          d=request.json 
          dbput("update appointment set token_status_id='"+str(d['status_id'])+"'  where appointment_id='"+str(d['appointment_id'])+"'")
          return(json.dumps({"Message":"Record Updated Successfully","MessageCode":"RUS","Service":"Success"},indent=4))
     except:
          return("something went wrong")
def count(request):
     try:
           d=request.json
           b_count = json.loads(dbget("select count(*) as bo_count from appointment \
                                      where token_status_id='1' and doctor_id='"+str(d['doctor_id'])+"' and business_id = '"+str(d['business_id'])+"'"))
           booked_count = b_count[0]['bo_count']
           c_count = json.loads(dbget("select count(*) as can_count from appointment \
                                      where token_status_id='2' and doctor_id='"+str(d['doctor_id'])+"' and business_id = '"+str(d['business_id'])+"'"))
           canceled_count = c_count[0]['can_count']
           co_count = json.loads(dbget("select count(*) as checkout_count from appointment \
                                      where token_status_id='3' and doctor_id='"+str(d['doctor_id'])+"' and business_id = '"+str(d['business_id'])+"'"))
           cheout_count = co_count[0]['checkout_count']
           return(json.dumps({"Message":"Token number Counted  Sucessfully","MessageCode":"TNS","Service Status":"Success","booked_count":booked_count,"canceled_count":canceled_count,"Checked_out":cheout_count},indent=4))
     except:
          return("something went wrong")
def livefeed(request):
     try:
          d = request.json
          output = json.loads(dbget("select appointment.token_no,appointment.token_time,token_status.status_name,user_profile.mobile,user_profile.user_name,user_profile.email, \
                             user_profile.emergency_contact_name,user_profile.emergency_contact_mobile \
                              from appointment join token_status on appointment.token_status_id=token_status.status_id \
                              join user_profile on appointment.user_id= user_profile.mobile\
                              where doctor_id='"+str(d['doctor_id'])+"' and business_id = '"+str(d['business_id'])+"' order by token_time desc limit 4"))
          return(json.dumps({"message":"live feed","output":output},indent = 4))
     except:
          return("something went wrong")

         
