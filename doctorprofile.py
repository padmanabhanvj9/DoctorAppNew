import json
from flask import Flask,request,jsonify
import datetime
from sqlwrapper import gensql,dbget,dbput

def insert_businessprofile(request):
    try:
        business = request.json
        gensql('insert','new.business_profile',business)
        bus_id = json.loads(gensql('select','new.business_profile','business_id',business))
        business_id =bus_id[0]['business_id']
        return(json.dumps({"Message":"Record Inserted Successfully",
                                   "MessageCode":"RIS","Service":"Success",'business_id':business_id},indent=4))
    except:
        return(json.dumps({"Message":"Record Inserted Unsuccessful","Message Code":"RIUS","Service Status":"Success"},indent=4))  

        


def insert_Doctorsprofile(request):
    try:

        doctors = request.json['doctors']
        business = request.json['business_id']
        password = request.json['password']
        login_status = request.json['login_status']
        doc_record = {k : v for k,v in doctors.items() if k not in ('Specialization','services')}
        doc_id = json.loads(dbget("select max(doctor_id) as doc_id from new.doctor_profile"))
        doctor_id = int(doc_id[0]['doc_id'])+1
        doc_record['doctor_profile_id'] = doctors['doctor_name'][:4]+str(doctor_id)
        gensql('insert','new.doctor_profile',doc_record)
        speclaization = doctors['Specialization']
        service = doctors['services']
        for sep in speclaization:
            i = {}
            i['doctor_id'] = doctors['doctor_name'][:4]+str(doctor_id)
            i['specialization_id'] = sep
            gensql('insert','new.doctor_specialization',i)
            
    
        for ser in service:
            i = {}
            i['doctor_id'] = doctors['doctor_name'][:4]+str(doctor_id)
            i['service_id'] = ser
            gensql('insert','new.doctor_services',i)
        business = request.json['business_id']  
        doctor_id = doctors['doctor_name'][:4]+str(doctor_id)    
        docandbus = {'business_id':business,'doctor_id':doctor_id,'password':password,'login_status':login_status}
        gensql('insert','new.doctorinbusiness',docandbus)
        return(json.dumps({"Message":"Record Inserted Successfully",
                       "MessageCode":"RIS","Service":"Success","doctor_id":doctor_id},indent=4))
    except:
        return(json.dumps({"Message":"Record Inserted Unsuccessful","Message Code":"RIUS","Service Status":"Success"},indent=4))  

def update_Businessprofile(request):
    try:
        d = request.json
        b={k : v for k,v in d.items() if k in ('business_id')}
        c={ k : v for k,v in d.items() if k  not in('business_id')}
        gensql('Update','new.business_profile',b,c)
        return(json.dumps({"Message":"Recored Updated Successfully","MessageCode":"RUS","Service Status":"Success"},indent=4))
    except:
        return(json.dumps({"Message":"Record Updated Unsuccessful","Message Code":"RUUS","Service Status":"Success"},indent=4))  

def update_doctorprofile(request):
    try:
        doctors = request.json
        doc_record = {k : v for k,v in doctors.items() if k not in ('Specialization','services')}
        print(doc_record)
        doctor = {k : v for k,v in doctors.items() if k  in ('doctor_id')}
        print(doctor)
        doc = doctor.get('doctor_id')
        print("doc",doc)
        doc_record['doctor_profile_id'] = doctors['doctor_name'][:4]+str(doctor.get('doctor_id'))
        gensql('update','new.doctor_profile',doc_record,doctor)
        doc_profile_id = doc_record['doctor_profile_id']
        print("dpi",doc_profile_id)
        speclaization = doctors['Specialization']
        print("dpi",speclaization)
        service = doctors['services']
        print("dpi",service)
        d = {'doctor_id':doc_profile_id}
        dbput("delete from new.doctor_specialization where doctor_id='"+str(d)+"'")
        for sep in speclaization:
            i = {}
            i['specialization_id'] = sep
            i['doctor_id'] = doc_profile_id
            gensql('insert','new.doctor_specialization',i)
        dbput("delete from new.doctor_services where doctor_id='"+str(d)+"'")    
        for ser in service:
            i = {}
            i['doctor_id'] = doc_profile_id
            i['service_id'] = ser
            gensql('insert','new.doctor_services',i)
        return(json.dumps({"Message":"Recored Updated Successfully","MessageCode":"RUS","Service Status":"Success"},indent=4))
    except:
        return(json.dumps({"Message":"Record Updated Unsuccessful","Message Code":"RUUS","Service Status":"Success"},indent=4))  

    
def update_businessanddoctors(request):
    try:
        d = request.json
        print(d)
        b={k : v for k,v in d.items() if k in ('docinbus_id')}
        c={ k : v for k,v in d.items() if k  not in('docinbus_id')}
        gensql('Update','new.doctorinbusiness',b,c)
        return(json.dumps({"Message":"Recored Updated Successfully","MessageCode":"RUS","Service":"Success"},indent=4))
    except:
        return(json.dumps({"Message":"Record Updated Unsuccessful","Message Code":"RUUS","Service Status":"Success"},indent=4))
def updatedocspecialization(request):
    try:
        d=request.json
        a= { k : v for k,v in d.items() if k not in ('specialization_id')}
        e={ k : v for k,v in d.items() if k in ('specialization_id')}
        gensql('update','new.doctor_specialization',a,e)
        return(json.dumps({"Message":"Record Updated Successfully","Message Code":"RUS","Service Status":"Success"},indent=4))
    except:
        return(json.dumps({"Message":"Record Updated Unsuccessful","Message Code":"RUUS","Service Status":"Success"},indent=4))               
            
def updatedocservices(request):
    try:
        d=request.json
        a= { k : v for k,v in d.items() if k not in ('service_id')}
        e={ k : v for k,v in d.items() if k in ('service_id')}
        gensql('update','new.doctor_services',a,e)
        return(json.dumps({"Message":"Record Updated Successfully","Message Code":"RUS","Service Status":"Success"},indent=4))
    except:
        return(json.dumps({"Message":"Record Updated Unsuccessful","Message Code":"RUUS","Service Status":"Success"},indent=4))

