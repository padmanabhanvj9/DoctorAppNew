from sqlwrapper import gensql, dbget, dbput
import json
import datetime
import time
from time import mktime
from flask import Flask, request, jsonify


def tokengeneration(request):
    try:

        d = request.json
        dt = datetime.datetime.strptime(d['business_date'], '%Y-%m-%d').date()  # to convert string to date format
        currenttime = datetime.datetime.now()  # to get current datetime
        todaydate = currenttime.date()
        todaytime = currenttime.strftime('%H:%M')  # to get current time
        doc_id = {k: v for k, v in d.items() if k in ('doctor_id', 'business_id')}
        docidval = doc_id.get("doctor_id")
        bus_id = doc_id.get("business_id")
        b = json.loads(dbget(
            "select * from new.timing where doctor_id = '" + str(docidval) + "' and business_id = '" + str(
                bus_id) + "'"))
        etime = b[0]['end_timing']  # to get value from list
        if dt == todaydate and etime > todaytime:
            a = {k: v for k, v in d.items() if k in ('doctor_id', 'business_id', 'business_date')}
            res = json.loads(gensql('select', 'new.token_no', 'count(*)', a))
            if res[0]['count'] == 0:
                a['token_no'] = 0
                gensql('insert', 'new.token_no', a)
            token = json.loads(gensql('select', 'new.token_no', 'token_no', a))
            no = token[0]['token_no'] + 1
            d['token_no'] = no
            d['token_time'] = currenttime
            gensql('insert', 'new.appointment', d)
            wt = json.loads(dbget("select average_waiting_time from new.doctorinbusiness where doctor_id = '" + str(
                docidval) + "' and business_id = '" + str(bus_id) + "'"))
            waittime = wt[0]['average_waiting_time']
            if no == 1:
                avg_wait = 0
            else:
                avg_wait = (no - 1) * waittime
            dbput("update new.token_no set token_no ='" + str(no) + "' where doctor_id='" + str(
                a['doctor_id']) + "' and business_id = '" + str(bus_id) + "' ")
            return (json.dumps(
                {'Message': 'Token Generated', 'MessageCode': 'TGS', 'Status': 'success Status', 'Token_No': no,
                 'waiting_time': avg_wait}, indent=4))

        else:
            return (json.dumps({"Message": "Token should be Generated only for Today Date", "Message Code": "TGTD",
                                "Service Status Status": "Failure"}, indent=4))
    except:
        return (json.dumps(
            {"Message": "Token Generation UnSuccessful", "Message Code": "TGUS", "Service Status": "Failure"},
            indent=4))


def selectappointment(request):
    try:
        d = request.json
        output = json.loads(dbget("select new.appointment.*,new.user_profile.* from new.appointment \
                                            join new.user_profile on new.appointment.mobile = new.user_profile.mobile where\
                                           new.appointment.doctor_id = '" + str(
            d['doctor_id']) + "' and new.appointment.business_id = '" + str(d['business_id']) + "'\
                                           and new.appointment.business_date = '" + str(
            d['business_date']) + "' order by new.appointment.token_no"))
        return (json.dumps(
            {"Message": "Appointments Selected Sucessfully", "MessageCode": "ASS", "Service Status Status": "Success",
             "output": output}, indent=4))
    except:
        return (json.dumps(
            {"Message": "Appointments Selected Unsuccessful", "Message Code": "ASUS", "Service Status": "Failure"},
            indent=4))


def updatetoken(request):
    try:
        d = request.json
        dbput("update new.appointment set token_status='" + str(d['token_status']) + "'  where appointment_id='" + str(
            d['appointment_id']) + "'")
        return (
            json.dumps({"Message": "Record Updated Successfully", "MessageCode": "RUS", "Service Status": "Success"},
                       indent=4))
    except:
        return (json.dumps(
            {"Message": "Appointments Updated Unsuccessful", "Message Code": "AUUS", "Service Status": "Failure"},
            indent=4))


def count(request):
    try:
        d = request.json
        b_count = json.loads(dbget("select count(*) as bo_count from new.appointment \
                                      where token_status='Booked' and doctor_id='" + str(
            d['doctor_id']) + "' and business_id = '" + str(d['business_id']) + "'\
                                       and new.appointment.business_date = '" + str(d['business_date']) + "'"))
        booked_count = b_count[0]['bo_count']
        c_count = json.loads(dbget("select count(*) as can_count from new.appointment \
                                      where token_status='Cancel' and doctor_id='" + str(
            d['doctor_id']) + "' and business_id = '" + str(d['business_id']) + "'\
                                       and new.appointment.business_date = '" + str(d['business_date']) + "'"))
        canceled_count = c_count[0]['can_count']
        co_count = json.loads(dbget("select count(*) as checkout_count from new.appointment \
                                      where token_status='Checkout' and doctor_id='" + str(
            d['doctor_id']) + "' and business_id = '" + str(d['business_id']) + "' \
                                      and new.appointment.business_date = '" + str(d['business_date']) + "'"))
        cheout_count = co_count[0]['checkout_count']
        return (json.dumps(
            {"Message": "Token number Counted  Sucessfully", "MessageCode": "TNS", "Service Status": "Success"
                , "booked_count": booked_count, "canceled_count": canceled_count, "Checked_out": cheout_count},
            indent=4))
    except:
        return (json.dumps(
            {"Message": "Token number Counted Unsuccessful", "Message Code": "TNUS", "Service Status": "Failure"},
            indent=4))


def livefeed(request):
    try:
        d = request.json
        output = json.loads(dbget("select new.appointment.*,new.user_profile.* from new.appointment \
                                join new.user_profile on new.appointment.mobile = new.user_profile.mobile \
                                where new.appointment.doctor_id='" + str(
            d['doctor_id']) + "' and new.appointment.business_id = '" + str(d['business_id']) + "'\
                                and new.appointment.business_date = '" + str(
            d['business_date']) + "' order by new.appointment.token_no desc limit 4"))
        return (json.dumps({"message": "livefeed Successful", "Message Code": "LS", "output": output}, indent=4))
    except:
        return (json.dumps({"Message": "Livefeed Unsuccessful", "Message Code": "LUS", "Service Status": "Failure"},
                           indent=4))


def average_waiting_time(request):
    try:
        d = request.json
        wt = json.loads(dbget("select average_waiting_time from new.doctorinbusiness where doctor_id = '" + str(
            d['doctor_id']) + "' and business_id = '" + str(d['business_id']) + "'"))
        waittime = wt[0]['average_waiting_time']
        print(waittime)
        tk_time = json.loads(dbget("select token_time from new.appointment where doctor_id = '" + str(
            d['doctor_id']) + "' and business_id = '" + str(d['business_id']) + "'\
                                  and mobile = '" + str(d['mobile']) + "'and business_date = '" + str(
            d['business_date']) + "'"))
        token_time = tk_time[0]['token_time']
        print(tk_time, token_time)
        count = json.loads(
            dbget("select count(*) as count from new.appointment where  token_time <'" + str(token_time) + "' and\
                                 business_id = '" + str(d['business_id']) + "' and business_date = '" + str(
                d['business_date']) + "'\
                                 and token_status = 'Booked'"))
        avg_wait = count[0]['count'] * waittime
        return (json.dumps(
            {"message": "Average Waittime Calculated Sucessfully ", "Message Code": "AWCS", "Wait_time": avg_wait},
            indent=4))
    except:
        return (json.dumps({"Message": "Average Waittime Calculated  Unsuccessful", "Message Code": "AWCUS",
                            "Service Status": "Failure"}, indent=4))









