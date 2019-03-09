import json
import requests

# rather than a hardcoded list, we should probably replace the targets list below
# with a look-up on data/reference_data/ne_towns.json

'''
targets = [2656539, 3333224, 2635630, 2656402, 2642932, 2640351, 2657832, 2657830, 2642692, 2646073, 2646384, 2646157,
           2642459, 2655978, 2634091, 2635329, 2635652, 2636814, 2639992, 2640030, 2640064, 2640253, 2641007, 2641549,
           2641691, 2642430, 2643262, 2645358, 2645836, 2649089, 2650086, 2650601, 2655288, 2655522, 2656405, 2656454,
           2657509, 2657775, 2657839, 6640068]
'''
location = "2656539" #temporary single value


def get_credentials():
    # Load config from JSON
    with open('credentials.json') as data_file:
        my_json = json.load(data_file)

    # Retrieve Open Weather Map credentials
    APPID = my_json['Open_Weather_Map']['APPID']
    return APPID


def test_some_weather(APPID, loc):
    base_query = "http://api.openweathermap.org/data/2.5/weather?id="
    target = base_query + loc + "&APPID=" + APPID
    response = requests.get(target)

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None

def store_vals(location, payload):
    # open a file for writing /data/weather/[location].csv
    # iterate through outer and inner dictionary
    # write vals to CSV appending a line

def main():
    APPID = get_credentials()

    # loop through targets list
    payload = test_some_weather(APPID, location)
    '''
    example returned:
    {'coord': {'lon': -2.71, 'lat': 57.05}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'base': 'stations', 'main': {'temp': 277.85, 'pressure': 992, 'humidity': 81, 'temp_min': 276.48, 'temp_max': 279.15}, 'visibility': 10000, 'wind': {'speed': 4.1, 'deg': 200}, 'rain': {'1h': 0.89}, 'clouds': {'all': 75}, 'dt': 1552071964, 'sys': {'type': 1, 'id': 1440, 'message': 0.004, 'country': 'GB', 'sunrise': 1552027456, 'sunset': 1552067987}, 'id': 2656539, 'name': 'Ballogie', 'cod': 200}
    '''

    store_vals(location, payload)

if __name__ == '__main__':
    main()
