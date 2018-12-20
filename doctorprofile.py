import json
from flask import Flask,request,jsonify
import datetime
from sqlwrapper import gensql,dbget,dbput

def insert_Doctorsprofile(request):
    try:
        doctors = request.json['doctors']
    
        business = request.json['business_id']
        password = request.json['password']
        print(doctors)
        print(business)
        #print("doc",type(doc))
        doc_record = {k : v for k,v in doctors.items() if k not in ('Specialization','services')}
        doc_id = json.loads(gensql('select','doctor_id','doc_id'))
        doc_id = doc_id[0]['doc_id']+1
        print(doc_id,type(doc_id))
        a = {"doc_id":doc_id}
        dbput("update doctor_id set doc_id='"+str(doc_id)+"' ")
        print("docname",doctors['doctor_name'])
        doc_record['doctor_id'] = doctors['doctor_name'][:4]+str(doc_id)
        gensql('insert','doctor_profile',doc_record)
        speclaization = doctors['Specialization']
        service = doctors['services']
        for sep in speclaization:
            try:
                i = {}
                i['doctor_id'] = doctors['doctor_name'][:4]+str(doc_id)
                i['specilization_id'] = sep
                gensql('insert','doctor_specilization',i)
            except:
                return("some thing went wrong speclaization  for loop ")
    
        for ser in service:
            try:
                i = {}
                i['doctor_id'] = doctors['doctor_name'][:4]+str(doc_id)
                i['service_id'] = ser
                gensql('insert','doctor_service',i)
            except:
                return("some thing went wrong service  for loop ")
                
            
        #gensql('insert','business_profile',business)
    
        #business_id = json.loads(gensql('select','business_profile','business_id',business))
        #print(business_id,type(business_id))
        docandbus = {"business_id":business,"doctor_id":doctors['doctor_name'][:4]+str(doc_id),"doc_password":password}
        gensql('insert','doctorinbusiness',docandbus)
        docinbus_id = json.loads(gensql('select','doctorinbusiness','docinbus_id',docandbus))
        #print(docinbus_id,type(docinbus_id))
    
        return(json.dumps({"Message":"Record Inserted Successfully",
                       "MessageCode":"RIS","Service":"Success","docinbus_id":docinbus_id,
                       "docandbus":docandbus},indent=4))
    except:
         return("some thing went wrong in update funtion")
