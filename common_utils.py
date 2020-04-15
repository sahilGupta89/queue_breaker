from math import radians, sin, cos, sqrt, asin
import datetime
import requests

def distance(slat,slon,elat,elon):
    # The math module contains a function named
    # radians which converts from degrees to radians.
    lon1 = radians(float(slon))
    lon2 = radians(float(elon))
    lat1 = radians(float(slat))
    lat2 = radians(float(elat))

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2

    c = 2 * asin(sqrt(a))

    # Radius of earth in kilometers. Use 3956 for miles
    r = 6371

    # calculate the result
    return (c * r)


def divideIntoTimeSlots(interval, data_dict):
    # check the number of slots in given duration
    start = datetime.datetime.strptime(data_dict['start_time'],'%Y-%m-%d %H:%M:%S.%f%z')
    end = datetime.datetime.strptime(data_dict['end_time'],'%Y-%m-%d %H:%M:%S.%f%z')
    day = data_dict['day']
    timeslot = []

    while start < end:

        timeslot.append({
            "provider": data_dict['provider'],
            "start_time": start,
            "end_time": start + datetime.timedelta(minutes=interval),
            "day": day,
            'home_delivery': data_dict['home_delivery']
        })
        start = start + datetime.timedelta(minutes=interval)

    return timeslot



def sendsms(to,msg):
    url = "https://www.fast2sms.com/dev/bulk"
    payload = "sender_id=FSTSMS&message={}&language=english&route=p&numbers={}".format(msg,to)
    print('payload',payload)
    headers = {
        'authorization': "ite4PV78TMHLldRvZcBU0CmpsDbqXfYNK65wkoW1hngjuFIES26L4vx3jNYgebmwWlhBpHZifRd0nquQ",
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache",
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    return response

