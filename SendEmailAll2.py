import json
import psycopg2
import json
import psycopg2
import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import Flask,request,jsonify

def callfn(sql):
 try:
      con = psycopg2.connect(user='xcymzcxxbjjeew',password='f431978a86d99ceaf4b114885091d9cc100c9d4ce12d1f6eb5efa80b8e868581',host='ec2-54-75-231-3.eu-west-1.compute.amazonaws.com',port='5432',database='d95ji8upkp95ss')
      cur = con.cursor()
 except psycopg2.Error :
      return (json.dumps({'Status': 'Failure','Message':'DB connection Error'}, sort_keys=True, indent=4))
 sender = request.json['sender']  
 mail = []   
 cur.execute(sql)
 result = cur.fetchall()
 for field in result:
     for test in field:
         if test  not in mail:
            mail.append(test)
 print(mail)
 
 len_mail = len(mail)    

 message_no = request.json['message']
 

 print(message_no)
 val1 = message_no['name']
 val2 = message_no['message']
 val3 = message_no['token_no']
 val4 = message_no['token_status']
 val5 = message_no['wait_time']
 val6 = message_no['bus_hour']
 val7 = message_no['break_time']
 val8 = message_no['address']
 val9 = message_no['hospital']


 subject = request.json['subject']
 msg = MIMEMultipart()
 msg['from'] = sender
 x=0
 #for receiver in email:
 while len_mail != x:
 #for  email in mail[x]:
     #print(mail[x])
     msg['to'] = mail[x]
     msg['subject'] = subject
     # Create the body of the message (a plain-text and an HTML version)
     html = """\
     <html>
      <head></head>
      <body>
        <dl>
        <dt>
        <p><font size="2" color="black">"""+str(val1)+"""</font></p>
        
        <p><font size="4" color="blue">"""+str(val2)+"""</font></p>
        <dd>
        <p><font size="2" color="black">"""+str(val3)+"""</font></p>
        <p><font size="2" color="black">"""+str(val4)+"""</font></p>
        <p><font size="2" color="black">"""+str(val5)+"""</font></p>
        <p><font size="2" color="black">"""+str(val6)+"""</font></p>
        <p><i><font size="2" color="blue">"""+str(val7)+"""</font></i></p>
        <p><font size="4" color="blue">"""+str(val8)+"""</font></p>
 
        </dd>
        </dl>

      </body>
     </html>
     """
     
     #msg.attach(MIMEText(msg['subject'],'plain'))
     msg.attach(MIMEText(html,'html'))
     
     gmailuser = 'infocuit.testing@gmail.com'
     password = 'infocuit@123'
     
     server = smtplib.SMTP('smtp.gmail.com',587)
     server.starttls()
     server.login(gmailuser,password)
     text = msg.as_string()
     server.sendmail(sender,mail[x],text)
     x+=1
     server.quit()
 print ("the message has been sent successfully") 

 return(json.dumps({'Message': 'Message Send Successfully','Returncode':'MSS'}, sort_keys=True, indent=4))
def sendemailall(request):
    d = request.json
    print(len(d))
    if len(d) == 5:
        sql = (" select new.user_profile.email from new.appointment join new.user_profile on new.appointment.mobile=new.user_profile.mobile \
                   where doctor_id='"+str(d['doctor_id'])+"' and business_id='"+str(d['business_id'])+"'")
        print(sql)
        return(callfn(sql))
    else:
        business_id = request.json['business_id']
        doctor_id = request.json['doctor_id']
        business_date = request.json['business_date']
        token_status = request.json['token_status']
        sql = (" select new.user_profile.email from new.appointment join new.user_profile on new.appointment.mobile=new.user_profile.mobile \
                           where business_date='"+str(business_date)+"' and doctor_id='"+str(doctor_id)+"' and business_id='"+str(business_id)+"' and token_status='"+token_status+"'")
        print(sql)
        return(callfn(sql))
             



    
