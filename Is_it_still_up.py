## work in progress

import requests, json


def get_sensor_list():
    with open('last_seen.json') as json_file:
        stored_data = json.load(json_file)
        return stored_data


def query_the_api():
    box = [57.5476, -1.9113, 56.9630, -2.4682]
    strbox = (str(box)[1:-1]).replace(" ", "")
    r = requests.get('https://api.luftdaten.info/v1/filter/box=' + strbox)
    my_json = r.json()
    return my_json


def filter_json(in_list):
    found_list = []
    for device in in_list:
        for key, val in device.items():
            if key == "sensor":
                for k, v in val.items():
                    if k == "id":
                        found_list.append(int(v))

    myset = set(found_list)  # stop duplicate values being added
    unique_list = list(myset)
    return sorted(unique_list)


def check_against_stored():
    # TODO implement this function to check our found values against our stored ones
    # Do we have ones that have disappeared? pass to send_alerts_if_down()
    # Do we have new devices, not seen before? Send them to add_new_to_list()
    # Updated our stored list with last seen values if changed
    pass


def add_new_to_list():
    pass


def send_alerts_if_down():
    pass


def main():
    existing = get_sensor_list()
    whats_up = query_the_api()
    found = filter_json(whats_up)
    print(found)
    check_against_stored()
    add_new_to_list()
    send_alerts_if_down()


if __name__ == '__main__':
    main()
