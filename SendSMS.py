import urllib.request
import time
import json
import psycopg2
from flask import Flask,request,jsonify 
def sendsms(request):
    
    
    count = []
    message = request.json['message']
    
    con = psycopg2.connect(user='xcymzcxxbjjeew',password='f431978a86d99ceaf4b114885091d9cc100c9d4ce12d1f6eb5efa80b8e868581',host='ec2-54-75-231-3.eu-west-1.compute.amazonaws.com',port='5432',database='d95ji8upkp95ss')
    cur = con.cursor()
    appointment_date= request.json['appointment_date']
    business_id = request.json['business_id']
    token_status_id = request.json['token_status_id']
    doctor_id = request.json['doctor_id']
    sql = "select user_id  from appointment where business_id='"+str(business_id)+"' and doctor_id='"+doctor_id+"' and appointment_date= '"+appointment_date+"' and token_status_id = '"+str(token_status_id)+"'"
    cur.execute(sql)
    
    results = cur.fetchall()
    for result in results:
        for i in result:
            count.append(i)
            
    for mobile in count:
        print(mobile)
        time.sleep(2)
        url = "https://control.msg91.com/api/sendhttp.php?authkey=195833ANU0xiap5a708d1f&mobiles="+mobile+"&message="+message+"&sender=Infoit&route=4&country=91"
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            the_page = response.read()
            the_page = the_page[1:]
            print(the_page)
            the_page = str(the_page)
    con.close()
    
    return(json.dumps({"Message":"SMS Sent Successfully","Key":the_page},indent =2))
        
    
