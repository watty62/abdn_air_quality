## work in progress

import requests


def get_data():
    r = requests.get('https://api.luftdaten.info/v1/filter/box=57.5476,-1.9113,56.9630,-2.4682')
    my_json = r.json()
    return my_json


def extract_values(our_list):
    for sensor in our_list:
        for key, val in sensor.items():
            print(f"Key = {key} // Value = {val}")
        print('===================')


def main():
    our_list = get_data()
    # our_list is a list of dictionaries
    extract_values(our_list)


if __name__ == '__main__':
    main()
