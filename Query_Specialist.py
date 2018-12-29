from sqlwrapper import gensql, dbget, dbput
import json

def Select_Specialist(request):
    d = request.json
    res = dbget("select doctorinbusiness.docinbus_id,business_profile.*,doctor_profile.*,doctorinbusiness.password,\
          doctorinbusiness.login_status, doctorinbusiness.average_waiting_time\
          from new.doctorinbusiness join\
          new.business_profile on doctorinbusiness.docinbus_id = business_profile.business_id join\
          new.doctor_profile on doctorinbusiness.doctor_id = doctor_profile.doctor_profile_id\
          where new.business_profile.country='India' and new.business_profile.city='Chennai' and\
          new.doctor_profile.country='India' ")
    print(res)
    return (json.dumps({'Message': 'Token Generated',
                        'MessageCode': 'TGS', 'Status': 'success',
                        'Token_No':res}, indent=4))
