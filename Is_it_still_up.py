## work in progress

import requests, json, datetime


def get_current_datetime():
    return datetime.datetime.now()


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
    # print (sorted(unique_list))
    return sorted(unique_list)


def check_against_stored(existing, found, right_now):
    new_list = []  # to hold new and updated values

    for fd in found:
        added = False
        for dev in existing['devices']:
            x = dev['id']
            if x == fd:
                new_dict = dict()
                new_dict['id'] = fd
                new_dict['first_seen'] = dev['first_seen']
                new_dict['last_seen'] = str(right_now)
                added = True
                new_list.append(new_dict)
            else:
                if not added:
                    new_dict = dict()
                    new_dict['id'] = fd
                    new_dict['first_seen'] = str(right_now)
                    new_dict['last_seen'] = str(right_now)
                    added = True
                    new_list.append(new_dict)
    return new_list


def update_stored_list(in_list):
    my_dict = dict()
    my_dict['devices'] = in_list

    with open ('last_seen.json', 'w') as out_file:
        json.dump(my_dict, out_file, indent=4)


def send_alerts_if_down():
    pass


def main():
    right_now = get_current_datetime()
    existing = get_sensor_list()
    whats_up = query_the_api()
    found = filter_json(whats_up)
    new_list = check_against_stored(existing, found, right_now)
    update_stored_list(new_list)
    # TODO Have some disappeared? check_if missing then pass to send_alerts_if_down()
    # send_alerts_if_down()


if __name__ == '__main__':
    main()
