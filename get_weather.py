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
location = "2656539"


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


def main():
    APPID = get_credentials()
    payload = test_some_weather(APPID, location)
    print((payload))


if __name__ == '__main__':
    main()
