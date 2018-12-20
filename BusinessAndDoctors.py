import json
from flask import Flask,request,jsonify
import datetime
from sqlwrapper import gensql,dbget,dbput

def insert_BusinessAndDoctors(request):
    try:
    
        doctors = request.json['doctors']
        business = request.json['business']
        password = request.json['password']
        #print(doctors)
       # print(business)
        
        for doc in doctors:
            print("doc",doc,type(doc))
            doc_record = {k : v for k,v in doc.items() if k not in ('Specialization','services')}
            
            doc_id = json.loads(gensql('select','doctor_id','doc_id'))
            
            doc_id = doc_id[0]['doc_id']+1
            print(doc_id,type(doc_id))
            a = {"doc_id":doc_id}
            dbput("update doctor_id set doc_id='"+str(doc_id)+"' ")
            print("docname",doc['doctor_name'])
            doc_record['doctor_id'] = doc['doctor_name'][:4]+str(doc_id)
            
            gensql('insert','doctor_profile',doc_record)
            
            speclaization = doc['Specialization']
            service = doc['services']
            for sep in speclaization:
                i = {}
                i['doctor_id'] = doc['doctor_name'][:4]+str(doc_id)
                i['specilization_id'] = sep
                gensql('insert','doctor_specilization',i)
            for ser in service:
                i = {}
                i['doctor_id'] = doc['doctor_name'][:4]+str(doc_id)
                i['service_id'] = ser
                gensql('insert','doctor_service',i)
                
        gensql('insert','business_profile',business)
        
        business_id = json.loads(gensql('select','business_profile','business_id',business))
        #print(business_id,type(business_id))
        docandbus = {"business_id":business_id[0]['business_id'],"doctor_id":doc['doctor_name'][:4]+str(doc_id),"doc_password":password}
        
        gensql('insert','doctorinbusiness',docandbus)
        docinbus_id = json.loads(gensql('select','doctorinbusiness','docinbus_id',docandbus))
        #print(docinbus_id,type(docinbus_id))
        
        return(json.dumps({"Message":"Record Inserted Successfully",
                           "MessageCode":"RIS","Service":"Success","docinbus_id":docinbus_id,
                           "docandbus":docandbus},indent=4))
    except:
        return("something went wrong")
def select_BusinessAndDoctors():
    try:
        
        dandb_output = json.loads(gensql('select','doctorinbusiness','*'))
        return(json.dumps({"Message":"Record Inserted Successfully",
                           "MessageCode":"RIS","Service":"Success","doctorinbusiness":dandb_output},indent=4))
    except:
        return("something went wrong")
def update_Businessprofile(request):
    try:
        d = request.json
        b={k : v for k,v in d.items() if k in ('business_id')}
        c={ k : v for k,v in d.items() if k  not in('business_id')}
        gensql('Update','business_profile',b,c)
        return(json.dumps({"Message":"Recored Updated Successfully","MessageCode":"RUS","Service":"Success"},indent=4))
    except:
        return("something went wrong")
def update_doctorprofile(request):
    try:
        d = request.json
        print(d)
        dbput("update doctorinbusiness set login_status_id='"+str(d['login_status_id'])+"' where docinbus_id='"+str(d['docinbus_id'])+"'")
        return(json.dumps({"Message":"Recored Updated Successfully","MessageCode":"RUS","Service":"Success"},indent=4))
    except:
        return("something went wrong")
   
     
    

