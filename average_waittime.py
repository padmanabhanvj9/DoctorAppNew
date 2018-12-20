import json
from flask import Flask,request,jsonify
import datetime
from sqlwrapper import gensql,dbget,dbput
def averagewaittime(request):
        try:
            business_id = request.json['business_id']
            doctor_id = request.json['doctor_id']
            user_id = request.json['user_id']
            #i = {business_id : request.json['business_id'],doctor_id : request.json['doctor_id']}
            wt = json.loads(dbget("select average_wait_time from doctorinbusiness where doctor_id='"+str(doctor_id)+"' and business_id='"+str(business_id)+"'"))
        except:
                return("some thing went wrong in query")
        try:
                waittime = wt[0]['average_wait_time']
                print(waittime,type(waittime))
                Token_no = json.loads(dbget("select  token_no from appointment where doctor_id='"+str(doctor_id)+"' and user_id='"+str(user_id)+"' and token_status_id = '1'"  ))
                #Token_no = json.loads(dbget("select count(*) as tk_no from appointment where doctor_id='"+str(doctor_id)+"' and token_status_id = '1'"  ))
                token = Token_no[0]['token_no']
                print(token,type(token))
                #status = token_no[0]['token_status_id']
                #print(status,type(status))
                total_avg = waittime * token
                return(json.dumps({'Status': 'Success', 'StatusCode': '200','Average_Wait_Time':total_avg}, sort_keys=True, indent=4))
        except:
                return("some thing went wrong in query")
        
        
