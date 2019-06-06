## work in progress

import requests
from datetime import datetime
import pprint
import get_weather
import math
from math import sin, cos, sqrt, atan2, radians

def get_data(box):
    # gets luftdaten data for all sensors within a given lat/log box
    # box = 'lat_0,long_0,lat_1,long_1'
    r = requests.get('https://api.luftdaten.info/v1/filter/box=' + box)
    my_json = r.json()
    return my_json


def tidy_values(our_list):
    # organises ourlist as a dictionary of dictionaries follows:

    new_dict = {}
    for sensor in our_list:
        location_id = str(sensor['location']['id'])
        if (new_dict.get(location_id, None) == None):
            new_dict[location_id] = {}
            new_dict[location_id]['location'] = sensor['location']
        for sensordata in sensor['sensordatavalues']:
            new_dict[location_id][sensordata['value_type']] = {
                'value': float(sensordata['value']),
                'timestamp': sensor['timestamp'],
                'id': sensor['id'],
                'sensor_type': sensor['sensor']['sensor_type'],
                'sensor_id' : str(sensor['sensor']['id'])}
    return (new_dict)


def test_values(sensor_list, weather_data):
    # test that:
    # 1. timestamps are fairly recent (within the last X minutes)
    # 2. check if humidity is >80% flag PM readings as invalid
    # 3. flag high P1/P2 readings (based on hard limits)
    # 4. flag high P1/P2 readings based on group medium/std

    # timestamps test
    current_time = datetime.now()
    for location_id in sensor_list:
        for param in sensor_list[location_id]:
            try:
                sense_time = sensor_list[location_id][param]['timestamp']
                delta_time = current_time - datetime.strptime(sense_time, "%Y-%m-%d %H:%M:%S")
                delta_time = divmod(delta_time.days * 86400 + delta_time.seconds, 60)
                if (delta_time[0] > 15):  # check >15min since last report
                    print ('timestamp fail!, id = ' + str(sensor_list[location_id][param]['id']) + ', ' + param)
            except:
                # no timestamp on this paramater
                False

    # PM test
    for location_id in sensor_list:
        # first find nearest weather city from weather_data
        min_dist = 1000000
        lat1a = float(sensor_list[location_id]['location']['latitude'])
        lon1a = float(sensor_list[location_id]['location']['longitude'])
        lat1 = radians(lat1a)
        lon1 = radians(lon1a)
        for city in weather_data['list']:
            lat2 = city['coord']['Lat']
            lon2 = city['coord']['Lon']
            # see https://stackoverflow.com/questions/19412462/getting-distance-between-two-points-based-on-latitude-longitude/43211266#43211266 for details

            R = 6373.0 #radius of earth
            lat2 = radians(lat2)
            lon2 = radians(lon2)
            dlon = lon2 - lon1
            dlat = lat2 - lat1
            a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
            c = 2 * atan2(sqrt(a), sqrt(1 - a))
            dist = R * c

            if (dist < min_dist):
                min_dist = dist
                local_city = city
        # lat2 = local_city['coord']['Lat']
        # lon2 = local_city['coord']['Lon']
        # print (lat1a, lon1a, " || " ,  lat2, lon2, " || ", min_dist, local_city['name'])

        # check local humidity level is within range based on weather
        # NB sensor humidity not used as not all sensors have this.
        if (local_city['main']['humidity'] > 70):
            # humidity is too high, PM readings should be ignored
            False
        else:
            try:
                # ref: http://ec.europa.eu/environment/air/quality/standards.htm
                sense_P1 = sensor_list[location_id]['P1']['value']
                if (sense_P1 > 40):  # check PM10 >40 ug/m^3
                    print ('[WARNING] PM1 high reading!, id = ' + str(
                        sensor_list[location_id]['P1']['id']) + ', ' + 'PM1 = ' + str(sense_P1))
                    print (' -[info] Distance to weather station (' + local_city['name'] + ') = ' + str(int(min_dist)) + 'km')
                sense_P2 = sensor_list[location_id]['P2']['value']
                if (sense_P2 > 20):  # check PM2.5 >20 ug/m^3
                    print ('[WARNING] PM2 high reading!, id = ' + str(
                        sensor_list[location_id]['P2']['id']) + ', ' + 'PM2 = ' + str(sense_P2))
                    print (' -[info] Distance to weather station (' + local_city['name'] + ') = ' + str(int(min_dist)) + 'km')

            except:
                # no PM1 or PM2 readings
                False


def main():
    Aberdeen = [57.25, -2.40, 57.00, -2.00]
    Aberdeenshire = [57.75, -4.00, 56.74, -1.70]
    WesternEurope = [60, -10, 40, 20] 
    box = WesternEurope
    strbox = (str(box)[1:-1]).replace(" ", "")
    our_list = get_data(strbox)
    # our_list is a list of dictionaries

    tidy_list = tidy_values(our_list)
    # tidy_list is a list of dictionaries that is easier to work with.

    weather_data = get_weather.main(box)

    # pp = pprint.PrettyPrinter(indent=1)
    # pp.pprint (tidy_list)
    # pp.pprint (weather_data)
    test_values(tidy_list, weather_data)

    return ()


if __name__ == '__main__':
    main()
