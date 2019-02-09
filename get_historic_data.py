import requests, argparse
from requests.exceptions import HTTPError
from dateutil import rrule, parser
import os

aparser = argparse.ArgumentParser(description='Scrape data from luftdaten')
aparser.add_argument(
    '-sd', '--startdate', dest='start_date', action='store',
    help='start date for scrape, format: yyyy-mm-dd')
aparser.add_argument(
    '-ed', '--enddate', dest='end_date', action='store',
    help='end date for scrape, format: yyyy-mm-dd')
aparser.add_argument(
    '-v', '--v', dest='verbose', action = 'store_true',
    help='verbose output')
args = aparser.parse_args()

def main ():
	if (args.start_date): 
		start_date = args.start_date
	else:
		print ('INFO: using default start date, 2017-10-01')
		start_date = '2017-10-01'
	if (args.end_date):
		end_date = args.end_date
	else:
		print ('INFO: using default end date, 2018-05-12')
		end_date = '2018-05-12'

	date_list = list(rrule.rrule(rrule.DAILY, dtstart=parser.parse(start_date), until=parser.parse(end_date)))
	if (not(date_list)):
		print ('ERROR: dates not valid')
		exit()

	sensor_ids = ["5331", "7789", "8554", "8733"]

	for sid in sensor_ids:
		print('INFO: downloading from SID ' + sid)
		N = 0
		L = str(0)
		for dy in date_list:
			N += 1
			create_urls (sid, dy)


def create_urls (sid, dy):
	file_add = "http://archive.luftdaten.info/" + dy.strftime('%Y-%m-%d') + "/"+ dy.strftime('%Y-%m-%d') + "_sds011_sensor_" + sid+ ".csv"
	fname = dy.strftime('%Y-%m-%d') + "_sds011_sensor_" + sid+ ".csv"
		
	try:
		r = requests.get(file_add)
		r.raise_for_status()
		if (args.verbose):
			print ('INFO: completed file (' + fname + ')')
	except HTTPError:
		print ('ERROR: Could not download file (' + fname + ')')
	else:	
		# Save the string to a file
		r = requests.get(file_add, stream=True)
		with open(fname, 'wb') as f:
			for chunk in r.iter_content(chunk_size=1024): 
				if chunk: # filter out keep-alive new chunks
					f.write(chunk)
main()

