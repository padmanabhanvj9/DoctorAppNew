import json
from flask import Flask,request,jsonify
import datetime
from sqlwrapper import gensql,dbget,dbput
def insertuser_profile(request):
    try:
        a=request.json
    
        b = {k : v for k,v in a.items() if k in ('User_Name','Mobile')}
        print(b)
        print(len(b))
        if len(b) != 2:
            return(json.dumps({"ServiceStatus":"Failure","ServiceMessage":"Failure"},indent=4))
    
        d = json.loads(dbget("select count(*) as rec_count from user_Profile where Mobile='"+str(a['Mobile'])+"' "))
        
        if d[0]['rec_count'] != 0:
             dbput("update User_Profile set Login_Status_Id='3' where Mobile='"+str(a['Mobile'])+"' ")
             return(json.dumps({"Message":"Login  Successfully","MessageCode":"LS","Service":"Success"},indent=4))   
        else:
            gensql('insert','User_Profile',a)
        return(json.dumps({"Message":"Record Inserted Successfully","MessageCode":"RIS","Service":"Success"},indent=4))
    except:
        return("some thing went wrong in insert profile function")  
    
    
def updateuser_profile(request):
    try:
        a=request.json
        b={k : v for k,v in a.items() if k in ('Mobile')}
        c={ k : v for k,v in a.items() if k  not in('Mobile')}
        gensql('Update','User_Profile',b,c)
        return(json.dumps({"Message":"Recored Updated Successfully","MessageCode":"RUS","Service":"Success"},indent=4))
    except:
        return("some thing went wrong in update profile function")  
def selectuser_profile(request):
     try:
         res=json.loads(dbget("select user_profile.user_Id,user_profile.Mobile,user_profile.User_Name,user_profile.Email,user_profile.Birthday,\
                               user_profile.Height,user_profile.Weight,user_profile.Emergency_Contact_Name,user_profile.Emergency_Contact_Mobile,\
                               Gender.type_of_gender, Gender.gender_id,Blood_Group.blood_group_name,Blood_Group.Blood_Group_Id,\
                               Married_Status.Status,Married_Status.married_status_id,city.city_name,city.city_id,\
                               Login_Status.status_name,Login_Status.status_id\
                               from user_profile join gender on user_profile.gender_id=gender.gender_id\
                               join blood_group on user_profile.blood_group_id=blood_group.blood_group_id\
                               join married_status on user_profile.married_status_id=married_status.married_status_id\
                               join city on user_profile.city_id=city.city_id\
                               join login_status on user_profile.login_status_id=login_status.status_id")) 
         
         return(json.dumps({"Message":"Recored Selected Successfully","MessageCode":"RSS","Service":"Success","output":res},indent=4))
     except:
         return("some thing went wrong in update profile function")  
def deleteuser_profile(request):
    try:
        d=request.json['user_id']
        dbput("delete from User_Profile where user_id='"+str(d)+"'")
        return(json.dumps({"Message":"Record Deleted Successfully","MessageCode":"RDS","Service Status":"Success"},indent=4))
    except:
        return("some thing went wrong in delete profile function")  

        
        
           

                  
