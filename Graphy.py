import matplotlib.pyplot as plt 
import math, json, argparse
from collections import OrderedDict
from datetime import datetime

aparser = argparse.ArgumentParser(description='Plot Luftdaten data from json')
aparser.add_argument(
    '-s', '--sensor', dest='sensor', action='store',
    help='s, format: 12345')
args = aparser.parse_args()

def main():
    json_file = './data/big_dump/'
    if (args.sensor): 
        sensor = args.sensor
    else:
        sensor = '13084'
    
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
        if ("humidity" in d[sensor]["readings"][str(t)]) and ("P2" in d[sensor]["readings"][str(t)]) and ("P1" in d[sensor]["readings"][str(t)]):
            humidity.append(d[sensor]["readings"][str(t)]["humidity"])
            temperature.append(d[sensor]["readings"][str(t)]["temperature"])
            P1.append(d[sensor]["readings"][str(t)]["P1"])
            P2.append(d[sensor]["readings"][str(t)]["P2"])
            timestamp_h.append(datetime.utcfromtimestamp(t))
        
    
    plt.figure(1)
    plt.suptitle(sensor)
    plt.subplot(221)
    plt.plot(humidity, P1, 'ro', ms=1, alpha=.1, label='P1')
    #plt.plot(humidity, P2, 'bo', ms=1, alpha=.1, label='P2')    
    plt.yscale('log')
    plt.xscale('linear')
    plt.ylabel('PM (ug/m^3)')
    plt.xlabel('Rel. Humidity (%)')
    plt.legend()

    plt.subplot(222)
    plt.plot(humidity, P2, 'bo', ms=1, alpha=.1, label='P2')
    #plt.plot(temperature, P1, 'ro', ms=1, alpha=.1, label='P1')
    #plt.plot(temperature, P2, 'bo', ms=1, alpha=.1, label='P2')
    plt.yscale('log')
    plt.xscale('linear')
    plt.ylabel('PM (ug/m^3)')
    #plt.xlabel('Temperature (C)')
    plt.xlabel('Rel. Humidity (%)')
    plt.legend()

    plt.subplot(223)
    plt.plot(humidity, temperature, 'ro', ms=1, alpha=.1)
    plt.yscale('linear')
    plt.xscale('linear')
    plt.ylabel('Temperature (C)')
    plt.xlabel('Rel. Humidity (%)')

    plt.subplot(224)
    plt.plot(P1, P2, 'go', ms=1, alpha=.1)
    plt.yscale('log')
    plt.xscale('log')
    plt.ylabel('P1 (ug/m^3)')
    plt.xlabel('P2 (ug/m^3)')
    
    plt.show()

main()