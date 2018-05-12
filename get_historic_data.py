from dateutil import rrule, parser

start_date = '2018-01-01'
end_date = '2018-05-10'

date_list = list(rrule.rrule(rrule.DAILY, dtstart=parser.parse(start_date), until=parser.parse(end_date)))

sensor_ids = ["5331", "7889", "8544", "8733"]

def create_urls (sid):

	for dy in date_list:
		url_to_fetch = "http://archive.luftdaten.info/" + dy.strftime('%Y_%m_%d') + "/"+ dy.strftime('%Y_%m_%d') + "_sds011_sensor_" + sid+ ".csv"
		print(url_to_fetch)

for sid in sensor_ids:
	create_urls (sid)


# target string format http://archive.luftdaten.info/2018-05-10/2018-05-10_sds011_sensor_7789.csv 


#http://archive.luftdaten.info/2018-05-10/2018-05-10_sds011_sensor_5331.csv
#http://archive.luftdaten.info/2018-05-10/2018-05-10_sds011_sensor_7789.csv
#http://archive.luftdaten.info/2018-05-10/2018-05-10_sds011_sensor_8544.csv
#http://archive.luftdaten.info/2018-05-10/2018-05-10_sds011_sensor_8733.csv

# https://www.madavi.de/sensor/csvfiles.php?sensor=esp8266-3654427
