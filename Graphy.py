import matplotlib.pyplot as plt 
import math
import json
from collections import OrderedDict
from datetime import datetime
def main():
    json_file = './data/tempdata/'
    sensor = '8320'
    json_file = json_file + sensor + '.json'
    with open(json_file, "r") as f:
        d = json.load(f, object_pairs_hook=OrderedDict)
    humidity = []
    timestamp_h = []
    temperature = []
    timestamp_t = []
    P1 = []
    timestamp_P1 = []
    P2 = []
    timestamp_P2 = []
    P1P2 = []
    timestamp_P1P2 = []
    old_i = 0
    all_time = []
    for i in d[sensor]["readings"]:
        all_time.append(int(i))
    all_time.sort()
    for t in all_time:
        if "humidity" in d[sensor]["readings"][str(t)]:
            humidity.append(math.exp(d[sensor]["readings"][str(t)]["humidity"]/10)/100)
            timestamp_h.append(datetime.utcfromtimestamp(t))
        if "temperature" in d[sensor]["readings"][str(t)]:
            temperature.append(d[sensor]["readings"][str(t)]["temperature"])
            timestamp_t.append(datetime.utcfromtimestamp(t))
        if "P1" in d[sensor]["readings"][str(t)]:
            P1.append(d[sensor]["readings"][str(t)]["P1"])
            timestamp_P1.append(datetime.utcfromtimestamp(t))
        if "P2" in d[sensor]["readings"][str(t)]:
            P2.append(d[sensor]["readings"][str(t)]["P2"])
            P1P2.append(math.log(d[sensor]["readings"][str(t
            )]["P1"]+0.001) - math.log((d[sensor]["readings"][str(t)]["P2"]+0.001)))
            timestamp_P2.append(datetime.utcfromtimestamp(t))
    
    plt.figure(1)
    plt.subplot(411)
    plt.plot(timestamp_h, humidity)
    plt.subplot(412)
    plt.yscale('linear')
    plt.plot(timestamp_t, temperature)
    plt.subplot(413)
    plt.yscale('log')
    plt.plot(timestamp_P1, P1, timestamp_P2, P2, timestamp_h, humidity)
    plt.subplot(414)
    plt.yscale('linear')
    plt.plot(timestamp_P2, P1P2)
    plt.show()

main()