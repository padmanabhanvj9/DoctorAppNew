from flask import Flask,request,jsonify
from sqlwrapper import gensql,dbget,dbput
import json
def Insert_Token_No(request):
    try:
        d=request.json
        print(d)
        gensql('insert','Token_No',d)
        return(json.dumps({"Message":"Record Inserted Successfully","MessageCode":"RIS","Service":"Success"},indent=4))
    except:
        return("some thing went wrong in input")  


def Update_Token_No(request):
    try:
        d=request.json
        name = { k : v for k,v in d.items() if k not in ('token_id')}
        id={ k : v for k,v in d.items() if k in ('token_id')}
        gensql('update','Token_No',name,id)
        return(json.dumps({"Message":"Record Updated Successfully","MessageCode":"RUS","Service":"Success"},indent=2))
    except:
        return("some thing went wrong in update token number function")  


def Select_Token_No(request):
    try:
        res=json.loads(gensql('select','Token_No','*'))
        return(json.dumps({"Message":"Record Selected Successfully","MessageCode":"RSS","Service":"Success","output":res},indent=2))
    except:
        return("some thing went wrong in select token number function")  

           

def Delete_Token_No(request):
     try:
         res=request.json['token_id']
         dbput("delete from Area where Token_No='"+res+"'")
         return(json.dumps({"Message":"Record Deleted Successfully","MessageCode":"RDS","Service Status":"Success"},indent=4))
     except:
        return("some thing went wrong in delete token number function")  




