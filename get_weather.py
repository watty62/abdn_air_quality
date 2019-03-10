import json
import requests
import pprint 

def get_credentials():
    # Load config from JSON
    with open('credentials.json') as data_file:
        my_json = json.load(data_file)

    # Retrieve Open Weather Map credentials
    APPID = my_json['Open_Weather_Map']['APPID']
    return APPID


def get_some_weather(APPID, box):
    base_query = "http://api.openweathermap.org/data/2.5/box/city?"
    target = (base_query 
        + 'bbox=' + str(box[0]) +','+ str(box[1]) +','+ str(box[2]) +','+ str(box[3]) + '&'
        + 'units=metric' + '&'
        + 'APPID=' + APPID
        )
    response = requests.get(target)

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None

def store_vals(payload):
    pp = pprint.PrettyPrinter(indent=1)
    pp.pprint (payload)
    # open a file for writing /data/weather/[location].csv
    # iterate through outer and inner dictionary
    # write vals to CSV appending a line

def main(box = [57.5476,-1.9113,56.9630,-2.4682]):
    #openweathermap box is reversed from luftdaten.
    box = [box[3],box[2],box[1],box[0]]
    APPID = get_credentials()
    weather_data = get_some_weather(APPID, box)
    '''
    example returned:
    {'coord': {'lon': -2.71, 'lat': 57.05}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'base': 'stations', 'main': {'temp': 277.85, 'pressure': 992, 'humidity': 81, 'temp_min': 276.48, 'temp_max': 279.15}, 'visibility': 10000, 'wind': {'speed': 4.1, 'deg': 200}, 'rain': {'1h': 0.89}, 'clouds': {'all': 75}, 'dt': 1552071964, 'sys': {'type': 1, 'id': 1440, 'message': 0.004, 'country': 'GB', 'sunrise': 1552027456, 'sunset': 1552067987}, 'id': 2656539, 'name': 'Ballogie', 'cod': 200}
    '''

    #store_vals(weather_data)
    return(weather_data)

if __name__ == '__main__':
    main(box)