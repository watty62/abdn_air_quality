## work in progress

import requests, json, datetime
import smtplib, ssl, tweepy


def get_current_datetime():
    return datetime.datetime.now()


def get_sensor_dict():
    """Returns a prev. stored dictionary of sensor IDs and dates, and a unique list of IDs."""

    with open('last_seen.json') as json_file:
        stored_dict = json.load(json_file)

    new_list = []
    for dev in stored_dict['devices']:
        new_list.append(dev['id'])
        unique_list = list(set(new_list))

    return stored_dict, unique_list


def query_the_api():
    """ Using a bounding box, retrieve a json list of sensor devices found"""

    box = [57.74, -2.97, 56.4, -1.7]
    strbox = (str(box)[1:-1]).replace(" ", "")
    r = requests.get('https://api.luftdaten.info/v1/filter/box=' + strbox)
    my_json_list = r.json()

    return my_json_list


def filter_json(in_list):
    """ filters and returns the list of unique sensors found"""

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


def lost_new_stillthere(existing, found, ex_dic, dat_tim):
    """Check which sensors gone missing, new ones, or still up """
    exist_set = set(existing)
    found_set = set(found)

    unchanged = list(exist_set & found_set)
    new_found = list(found_set - exist_set)

    # print (f"Unchanged = {unchanged}")
    # print(f"new_found = {new_found}")
    update_stored(unchanged, new_found, ex_dic, dat_tim)

    lost = list(exist_set - found_set)

    if len(lost) > 0:
        # print(lost)
        send_alerts_if_down(lost)


def lookup_host(sensor_id):
    h_email = ""
    with open('hosts_contacts.json') as json_file:
        host_list = json.load(json_file)

    for dev in host_list['devices']:
        if str(dev['id']) == str(sensor_id):
            h_email = dev['contact_email']
            break
        else:
            h_email = "unknown"

    return (h_email)


def update_stored(unchanged, new_found, ex_dic, dat_tim):
    """ Updates our stored list of sensors to add new ones, and update existing ones with DT last seen """

    for sensor in unchanged:
        for dev in ex_dic['devices']:
            if sensor == dev['id']:
                dev['last_seen'] = str(dat_tim)

    for newbie in new_found:
        new_dict = dict()
        new_dict['id'] = newbie
        new_dict['first_seen'] = str(dat_tim)
        new_dict['last_seen'] = str(dat_tim)
        ex_dic['devices'].append(new_dict)
    if len(new_found) > 0:
        send_tweet(new_found)
        pass
    with open('last_seen.json', 'w') as out_file:
        json.dump(ex_dic, out_file, indent=4)


def send_tweet(in_list):
    """Receive a list of new devices. Send a tweet for each."""

    with open('credentials.json') as json_file:
        creds = json.load(json_file)

    twit_creds = creds['twitter']
    consumer_key = twit_creds['consumer_key']
    consumer_secret = twit_creds['consumer_secret']
    access_token = twit_creds['access_token']
    access_token_secret = twit_creds['access_token_secret']

    for dev in in_list:
        to_tweet = f"New #Aberdeen AQ device found. ID = {dev}. See it on a map: http://uk.maps.luftdaten.info/#9/57.3406/-1.9226 "
        # tweet the message
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        tweepyapi = tweepy.API(auth)
        tweepyapi.update_status(to_tweet)
        # print("Tweeted")


def send_alerts_if_down(in_list):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "airaberdeen@gmail.com"

    with open('credentials.json') as json_file:
        creds = json.load(json_file)
    gmail_creds = creds['gmail']
    password = gmail_creds['password']

    # print (type(in_list))
    # print (in_list)

    for sens in in_list:
        receiver_email = lookup_host(sens)  # get recipient address
        if receiver_email != "unknown":
            sensor_id = str(sens)
            # Todo add last_seen date_time

            message = f"""\
            Subject: It looks like your Air Quality sensor {sensor_id} is offline
    
            TEST EMAIL PLEASE IGNORE
    
            Our automated test has detected that your AQ device {sensor_id} has gone offline. It was last seen more than an hour ago.
    
            See http://deutschland.maps.luftdaten.info/#10/57.1568/-1.9007 
    
            Please check if it needs rebooted, or if it has a power or wifi problem.
    
            The Aberdeen AQ team. """

            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message)


def main():
    """ Main programme execution - calls other functions"""
    right_now = get_current_datetime()
    # print(right_now)
    existing_dict, unique_exist = get_sensor_dict()
    # print(type(existing_dict))
    # print()
    # print(sorted(unique_exist))
    whats_up_list = query_the_api()
    # print(whats_up_list)
    found = filter_json(whats_up_list)
    # print(found)
    lost_new_stillthere(sorted(unique_exist), found, existing_dict, right_now)


if __name__ == '__main__':
    main()
