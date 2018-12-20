from flask import Flask,request,jsonify
from sqlwrapper import gensql,dbget,dbput
import json
def Insertarea(request):
    try:
        d=request.json
        print(d)
        gensql('insert','Area',d)
        return(json.dumps({"Message":"Record Inserted Successfully","MessageCode":"RIS","Service":"Success"},indent=4))
    except:
         return("some thing went wrong in input")  


def Updatearea(request):
     try:
         d=request.json
         name = { k : v for k,v in d.items() if k not in ('Area_Id')}
         id={ k : v for k,v in d.items() if k in ('Area_Id')}
         gensql('update','Area',name,id)
         return(json.dumps({"Message":"Record Updated Successfully","MessageCode":"RUS","Service":"Success"},indent=2))
     except:
         return("some thing went wrong in update function")     
        
     
def Selectarea(request):
    try:
        res=json.loads(gensql('select','Area','*'))
        return(json.dumps({"Message":"Record Selected Successfully","MessageCode":"RSS","Service":"Success","output":res},indent=2))
    except:
        return("some thing went wrong in select function")     
   
           

def Deletearea(request):
    try:
        res=request.json['Area_Id']
        dbput("delete from Area where Area_Id='"+res+"'")
        return(json.dumps({"Message":"Record Deleted Successfully","MessageCode":"RDS","Service Status":"Success"},indent=4))
    except:
        return("some thing went wrong in delete function") 
    
    


