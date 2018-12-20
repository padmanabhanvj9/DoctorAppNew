from flask import Flask,request,jsonify
#------------insertBloodGroup-------#
from Insert_Blood_Group import insertbloodgroup
from Insert_Blood_Group import updatebloodgroup
from Insert_Blood_Group import selectbloodgroup
from Insert_Blood_Group import deletebloodgroup
#----------gender------------#
from Gender import insertgender
from Gender import updategender
from Gender import selectgender

#---------userprofile--------#
from User_profile import insertuser_profile
from User_profile import updateuser_profile
from User_profile import selectuser_profile
from User_profile import deleteuser_profile
#---------marriedstatus---------#
from MarriedStatus import Insert_Married_Status
from MarriedStatus import Update_Married_Status
from MarriedStatus import Select_Married_Status
from MarriedStatus import Delete_Married_Status


#----------city------#
from city import insertcity
from city import updatecity
from city import selectcity
from city import deletecity
#-------loginstatus---------#
from Login_Status import Insert_Login_Status
from Login_Status import Select_Login_Status
from Login_Status import Update_Login_Status
from Login_Status import Delete_Login_Status


#--------Area-------#
from Area import Insertarea
from Area import Updatearea
from Area import Selectarea
from Area import Deletearea
#-------Business Type----------#
from BusinessType import InsertBusinessType
from BusinessType import UpdateBusinessType
from BusinessType import SelectBusinessType
from BusinessType import DeleteBusinessType
#------------Specilization--------------------#
from Specilization import insertspecialization
from Specilization import updatespecialization
from Specilization import selectspecialization
from Specilization import deletespecialization


#-------------Services--------------------------#
from Services import insertservices
from Services import updateservices
from Services import selectservices
from Services import deleteservices

#-------timing-------------#

from Timing  import Insert_Timing
from Timing  import Select_Timing
from Timing  import Update_Timing
from Timing  import Delete_Timing


#---------Week_day----------#

from WeekDay  import Insert_Week_Day
from WeekDay  import Select_Week_Day
from WeekDay  import Update_Week_Day
from WeekDay  import Delete_Week_Day

#------Feedback-------------#


from FeedBack  import Insert_FeedBack
from FeedBack  import Select_FeedBack
from FeedBack  import Update_FeedBack
from FeedBack  import Delete_FeedBack
#---------appionment-------#
from Appoinment import tokengeneration
from Appoinment import selectappoinment
from Appoinment import updatetoken
from Appoinment import orderby
from Appoinment import count
from Appoinment import livefeed


#----------------Token Status------------------#
from Token import insertstatus
from Token import updatestatus
from Token import selectstatus
from Token import deletestatus


##token_no

from Token_No  import Insert_Token_No
from Token_No  import Select_Token_No
from Token_No  import Update_Token_No
from Token_No  import Delete_Token_No

####
from BusinessAndDoctors import insert_BusinessAndDoctors
from BusinessAndDoctors import select_BusinessAndDoctors
from BusinessAndDoctors import update_Businessprofile
from BusinessAndDoctors import update_doctorprofile
from flask_cors import CORS

#------Doctorprofile-------------#
from doctorprofile import insert_Doctorsprofile

#-----------------Average waiting time-----------#
from average_waittime import averagewaittime

#---------------Send Email----------------#
from SendEmailAll2 import sendemailall

#------------Send SMS------------------#
from SendSMS import sendsms

app = Flask(__name__)
CORS(app)
@app.route("/")
def index():
    return "Welcome to dopctorapp"
#------------------Bloodgroup------------------------#
@app.route('/Insert_Blood_Group',methods=['POST'])
def Insert_Blood_Group():
    return insertbloodgroup(request)
@app.route('/Update_Blood_Group',methods=['POST'])
def Update_Blood_Group():
    return updatebloodgroup(request)
@app.route('/Select_Blood_Group',methods=['POST'])
def Select_Blood_Group():
    return selectbloodgroup(request)
@app.route('/Delete_Blood_Group',methods=['POST'])
def Delete_Blood_Group():
    return deletebloodgroup(request)
#-------------Gender--------------------#
@app.route('/Insert_Gender',methods=['POST'])
def Insert_Gender():
    return  insertgender(request)
@app.route('/Update_Gender',methods=['POST'])
def Update_Gender():
    return updategender(request)
@app.route('/Select_Gender',methods=['POST'])
def Select_Gender():
    return  selectgender(request)
#----------------Userprofile---------------------------
@app.route('/Insert_User_Profile',methods=['POST'])
def Insertuser_profile():
    return insertuser_profile(request)
@app.route('/Update_User_Profile',methods=['POST'])
def Update_User_profile():
    return updateuser_profile(request)
@app.route('/Select_User_Profile',methods=['POST'])
def Select_User_Profile():
    return selectuser_profile(request)
@app.route('/Delete_User_Profile',methods=['POST'])
def Delete_User_Profile():
    return deleteuser_profile(request)

@app.route('/Insert_Married_Status',methods=['POST'])
#----------------Married_status------------------#
def insertmarriedstatus():
    return Insert_Married_Status(request)

@app.route('/Update_Married_Status',methods=['POST'])
def updatemarriedstatus():
    return Update_Married_Status(request)

@app.route('/Select_Married_Status',methods=['POST'])
def selectmarriedstatus():
    return Select_Married_Status(request)

@app.route('/Delete_Married_Status',methods=['POST'])
def deletetmarriedstatus():
    return Delete_Married_Status(request)


#--------------city--------------#
@app.route('/Insertcity',methods=['post'])
def Insertcity():
    return insertcity(request)


@app.route('/Updatecity',methods=['post'])
def Updatecity():
    return updatecity(request)


@app.route('/Selectcity',methods=['post'])
def Selectcity():
    return selectcity(request)
#------------------login------------#
@app.route('/Insert_Login_Status',methods=['post'])
def insertloginstatus():
    return Insert_Login_Status(request)


@app.route('/Select_Login_Status',methods=['post'])
def selectloginstatus():
    return Select_Login_Status(request)

@app.route('/Update_Login_Status',methods=['post'])
def updateloginstatus():
    return Update_Login_Status(request)

@app.route('/Delete_Login_Status',methods=['post'])
def deleteloginstatus():
    return Delete_Login_Status(request)

#-----------Area Route----------------#
@app.route('/Insert_Area',methods=['post'])
def insertarea():
    return Insertarea(request)
@app.route('/Update_Area',methods=['post'])
def updatearea():
    return Updatearea(request)
@app.route('/Select_Area',methods=['post'])
def selectarea():
    return Selectarea(request)
@app.route('/Delete_Area',methods=['post'])
def deletearea():
    return Deletearea(request)

#-----------Business_Route------------#
@app.route('/Insert_Business_Type',methods=['post'])
def insertbusinesstype():
    return InsertBusinessType(request)
@app.route('/Update_Business_Type',methods=['post'])
def updatebusinesstype():
    return UpdateBusinessType(request)
@app.route('/Select_Business_Type',methods=['post'])
def selectbusinesstype():
    return SelectBusinessType(request)
@app.route('/Delete_Business_Type',methods=['post'])
def deletebusinesstype():
    return DeleteBusinessType(request)

#---------------Specilization----------------------------#
@app.route('/Insert_Specialization',methods=['post'])
def Insert_Specialization():
    return insertspecialization(request)


@app.route('/Update_Specialization',methods=['post'])
def Update_Specialization():
    return updatespecialization(request)

@app.route('/Select_Specialization',methods=['post'])
def Select_Specialization():
    return selectspecialization(request)


@app.route('/Delete_Specialization',methods=['post'])
def Delete_Specialization():
    return deletespecialization(request)


#--------------------------Services------------------#
@app.route('/Insert_Services',methods=['post'])
def Insert_Services():
    return insertservices(request)

@app.route('/Update_Services',methods=['post'])
def Update_Services():
    return updateservices(request)

@app.route('/Select_Services',methods=['post'])
def Select_Services():
    return selectservices(request)

@app.route('/Delete_Services',methods=['post'])
def Delete_Services():
    return deleteservices(request)


#-------------------timing-----------#

@app.route('/Insert_Timing',methods=['post'])
def inserttiming():
    return Insert_Timing(request)

@app.route('/Select_Timing',methods=['post'])
def selecttiming():
    return Select_Timing(request)

@app.route('/Update_Timing',methods=['post'])
def updatetiming():
    return Update_Timing(request)

@app.route('/Delete_Timing',methods=['post'])
def deletetiming():
    return Delete_Timing(request)

#---------------weekday----------------#

@app.route('/Insert_Week_Day',methods=['post'])
def insertweekday():
    return Insert_Week_Day(request)

@app.route('/Select_Week_Day',methods=['post'])
def selecttweekday():
    return Select_Week_Day(request)

@app.route('/Update_Week_Day',methods=['post'])
def updateweekday():
    return Update_Week_Day(request)

@app.route('/Delete_Week_Day',methods=['post'])
def deleteweekday():
    return Delete_Week_Day(request)

#-----------feedback-------------#

@app.route('/Insert_FeedBack',methods=['post'])
def insertfeedback():
    return Insert_FeedBack(request)


@app.route('/Select_FeedBack',methods=['post'])
def selectfeedback():
    return Select_FeedBack(request)

@app.route('/Update_FeedBack',methods=['post'])
def updatefeedback():
    return Update_FeedBack(request)

@app.route('/Delete_FeedBack',methods=['post'])
def deletefeedback():
    return Delete_FeedBack(request)

#-----------appoinment-------------#
@app.route('/InsertAppoinment',methods=['post'])
def appoinment():
    return tokengeneration(request)
@app.route('/SelectAppoinment',methods=['post'])
def Selectppoinment():
    return selectappoinment(request)

@app.route('/UpdateAppoinment',methods=['post'])
def cancelppoinment():
    return updatetoken(request)
@app.route('/OrderAppoinment',methods=['post'])
def Orderby():
    return orderby(request)
@app.route('/CountAppoinment',methods=['post'])
def Count():
    return count(request)
@app.route('/livefeed',methods=['post'])
def Livefeed():
    return livefeed(request)

#---------------------Token Status------------------#
@app.route('/Insert_Status',methods=['post'])
def Insert_Status():
    return insertstatus(request)

@app.route('/Update_Status',methods=['post'])
def Update_Status():
    return updatestatus(request)

@app.route('/Select_Status',methods=['post'])
def Select_Status():
    return selectstatus(request)

@app.route('/Delete_Status',methods=['post'])
def Delete_Status():
    return deletestatus(request)

#---------------Token_no---------------------------#
@app.route('/Insert_Token_No',methods=['post'])
def inserttokenno():
    return Insert_Token_No(request)

@app.route('/Select_Token_No',methods=['post'])
def selecttokenno():
    return Select_Token_No(request)

@app.route('/Update_Token_No',methods=['post'])
def updatetokenno():
    return Update_Token_No(request)

@app.route('/Delete_Token_No',methods=['post'])
def deletetokenno():
    return Delete_Token_No(request)


#---------------Business And Doctors-----------------------#
@app.route('/insert_BusinessAndDoctors',methods=['post'])
def insert_BusAndDocs():
    return insert_BusinessAndDoctors(request)

@app.route('/select_BusinessAndDoctors',methods=['post'])
def Select_BusAndDocs():
    return select_BusinessAndDoctors()

@app.route('/update_Business_profile',methods=['post'])
def Update_Businessprofile():
    return update_Businessprofile(request)
@app.route('/update_doctor_profile',methods=['post'])
def Update_doctorprofile():
    return update_doctorprofile(request)


#------------------doctorprofile-------#
@app.route('/Insert_Doctor_profile',methods=['post'])
def Insert_Doctorsprofile():
    return insert_Doctorsprofile(request)


#-----------------Average Waiting Time--------------#
@app.route('/Average_waittime',methods=['post'])
def Avg_waittime():
    return averagewaittime(request)


#-----------------Send Email-----------------#
@app.route('/SendEmailall',methods=['post'])
def Sendemailall():
    return sendemailall(request)

#-------------------Send SMS------------------#
@app.route('/SendSMS',methods=['GET'])
def Sendsms():
    return sendsms(request)


if __name__ == '__main__':
   app.run(host="192.168.1.25",port=5000)
