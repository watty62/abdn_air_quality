## work in progress

import requests
from datetime import datetime
import pprint
import get_weather
import math

def get_data(box ):
    #gets luftdaten data for all sensors within a givin lat/log box
    #box = 'lat_0,long_0,lat_1,long_1'
    r = requests.get('https://api.luftdaten.info/v1/filter/box='+box)
    my_json = r.json()
    return my_json

def tidy_values(our_list):
    #organises ourlist as a dictionary of dictionaries follows:

    new_dict = {}
    for sensor in our_list:
            location_id = str(sensor['location']['id'])
            if (new_dict.get(location_id, None)==None):
                new_dict[location_id] = {}
                new_dict[location_id]['location'] = sensor['location']
            for sensordata in sensor['sensordatavalues']:
                new_dict[location_id][sensordata['value_type']] = {
                    'value' : float(sensordata['value']),
                    'timestamp' : sensor['timestamp'],
                    'id':sensor['id'],
                    'sensor_type' : sensor['sensor']['sensor_type']}
    return(new_dict)

def test_values(sensor_list, weather_data):
    #test that:
    #1. timestamps are fairly recent (within the last X minutes)
    #2. check if humidity is >80% flag PM readings as invalid
    #3. flag high P1/P2 readings (based on hard limits)
    #4. flag high P1/P2 readings based on group medium/std

    #timestamps test
    current_time = datetime.now()
    for location_id in sensor_list:
        for param in sensor_list[location_id]:
            try:
                sense_time = sensor_list[location_id][param]['timestamp']
                delta_time = current_time - datetime.strptime(sense_time, "%Y-%m-%d %H:%M:%S")
                delta_time = divmod(delta_time.days * 86400 + delta_time.seconds, 60)
                if (delta_time[0]>15): #check >15min since last report
                    print ('timestamp fail! - ' + str(sensor_list[location_id][param]['id']) + ', ' + param)
            except:
                #no timestamp on this paramater
                False
    #PM test
    for location_id in sensor_list:
        #first find nearest weather city from weather_data 
        #tbd but required for bigbox test
        min_dist = 1000000
        for city in weather_data['list']:
            dist = math.sqrt(
                math.pow(city['coord']['Lat'] - float(sensor_list[location_id]['location']['latitude']) ,2) +
                math.pow(city['coord']['Lon'] - float(sensor_list[location_id]['location']['longitude']) ,2)
                )
            if (dist < min_dist):
                min_dist = dist
                local_city = city

        #for param in sensor_list[location_id]:
        #    try:
        #        sense_time = sensor_list[location_id][param]['timestamp']
        #        delta_time = current_time - datetime.strptime(sense_time, "%Y-%m-%d %H:%M:%S")
        #        delta_time = divmod(delta_time.days * 86400 + delta_time.seconds, 60)
        #        if (delta_time[0]>15): #check >15min since last report
        #            print ('timestamp fail! - ' + str(sensor_list[location_id][param]['id']) + ', ' + param)
        #    except:
        #        #no timestamp on this paramater
        #       False 

def main():
    box = [57.5476,-1.9113,56.9630,-2.4682]
    bigbox = [100,-1,20,-50]
    box = bigbox #test
    strbox = (str(box)[1:-1]).replace(" ", "")
    our_list = get_data(strbox)
    #our_list is a list of dictionaries
    
    tidy_list = tidy_values(our_list)
    #tidy_list is a list of dictionaries that is easier to work with.
    
    weather_data = get_weather.main(box)
    #adds weather data to each sensor

    pp = pprint.PrettyPrinter(indent=1)
    pp.pprint (tidy_list)
    pp.pprint (weather_data)
    test_values(tidy_list, weather_data)

    return()

if __name__ == '__main__':
    main()