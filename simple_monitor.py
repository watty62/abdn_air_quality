## work in progress

import requests
from datetime import datetime

def get_data(box = '57.5476,-1.9113,56.9630,-2.4682'):
    #gets luftdaten data for all sensors within a givin lat/log box
    # box = 'lat_0,long_0,lat_1,long_1'
    #where lat/long_0 is north-west corner and lat/long_1 is south-east corner
    #box variable defaults if not given to east side of Aberdeenshire
    r = requests.get('https://api.luftdaten.info/v1/filter/box='+box)
    my_json = r.json()
    return my_json


def extract_values(our_list):
    for sensor in our_list:
        for key, val in sensor.items():
            print(f"Key = {key} // Value = {val}")
        print('===================')

def test_values(our_list):
    for sensor in our_list:
        #set up check variable
        check = {}
        check['id'] = Device_ID = sensor['id']
        check['timestamp'] = False
        check['humidity'] = False
        check['temperature'] = False
        check['PM2.5'] = False
        check['PM10'] = False

        #check timestamp
        time_now = datetime.now()
        delta_time = datetime.strptime(sensor['timestamp'], '%Y-%m-%d %H:%M:%S') - time_now
        delta_time = divmod(delta_time.days * 86400 + delta_time.seconds, 60)
        if (delta_time[0]>-15): #check <15min since last report
            check['timestamp'] = True

        #check humidity
        #if humidity if >80% skip other tests    
        print(sensor['sensordatavalues'])

def main():
    box = '57.5476,-1.9113,56.9630,-2.4682'
    our_list = get_data(box)
    # our_list is a list of dictionaries
    extract_values(our_list)
    #test_values(our_list)


if __name__ == '__main__':
    main()
