import argparse, time
from bs4 import BeautifulSoup
import requests
from requests.exceptions import HTTPError
from urllib.request import urlopen
import re
import zipfile, io
from dateutil import rrule, parser
import os

aparser = argparse.ArgumentParser(description='Scrape data from madavi')
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

zip_file_data = 0
zip_file_url = 0

def main ():
	if (args.start_date): 
		start_date = args.start_date
	else:
		#start_date = time.strftime(str(int("%Y")-1 + "-%m-%d")) not working
		start_date = '2017-10-01' 
		print ('INFO: using default start date, ' + start_date)
	if (args.end_date):
		end_date = args.end_date
	else:
		end_date = time.strftime("%Y-%m-%d")
		#end_date = '2018-05-12'
		print ('INFO: using default end date, ' + end_date)

	date_list = list(rrule.rrule(rrule.DAILY, dtstart=parser.parse(start_date), until=parser.parse(end_date)))
	if (not(date_list)):
		print ('ERROR: dates not valid')
		exit()

	sensor_ids = ['3654427', '12017738','3654335']

	for sid in sensor_ids:
		print('INFO: downloading from SID ' + sid)
		dir = "data/madavi/"+ sid
		try:
			os.makedirs(dir)
		except FileExistsError:
			# directory already exists
			pass
		N = 0
		for dy in date_list:
			N += 1
			create_urls (sid, dy, dir)


def create_urls (sid, dy, dir):
	csv_add = "https://www.madavi.de/sensor/data_csv/data-esp8266-" + sid + "-" + dy.strftime('%Y-%m-%d') + ".csv"
	csv_file = "data-esp8266-" + sid + "-" + dy.strftime('%Y-%m-%d') + ".csv"
	#https://www.madavi.de/sensor/data_csv/data-esp8266-3654427-2019-02-13.csv
	zip_add = "https://www.madavi.de/sensor/data_csv/"+ dy.strftime('%Y/%m') +"/data-esp8266-" + sid + "-" + dy.strftime('%Y-%m') + ".zip"
	#https://www.madavi.de/sensor/data_csv/2018/02/data-esp8266-3654427-2018-02.zip
	fname = dir + "/" + csv_file
	
	#could add check if file already exists here?
	#if it did normally skip

	#try to get csv files directly
	file_add = csv_add
	zip_file_url = csv_add
	try:
		r = requests.get(file_add)
		r.raise_for_status()
		if (args.verbose):
			print ('INFO: completed file (' + fname + ')')
	except HTTPError:
		#try to the zip of the whole month
		file_add = zip_add
		try:
			if (zip_file_url != file_add):
				zip_file_url = file_add
				r = requests.get(file_add)
				r.raise_for_status()
				zip_file_data = zipfile.ZipFile(io.BytesIO(r.content))
			try:
				zip_file_data.extract(csv_file, path = dir)
				print ('INFO: completed file (' + fname + ')')
			except:
				print ('ERROR: Could not download file (' + fname + ')')
		except HTTPError:
			print ('ERROR: Could not download file (' + fname + ')')
		
	else:	
		# Save the string to a file
		r = requests.get(file_add, stream=True)
		with open(fname, 'wb') as f:
			for chunk in r.iter_content(chunk_size=1024): 
				if chunk: # filter out keep-alive new chunks
					f.write(chunk)

#----------
#	html_page = urlopen(file_add)
#	soup = BeautifulSoup(html_page, "lxml")
#	for link in soup.findAll('a'):
#		
#		if link.get('href')[-14:] == dy.strftime('%Y-%m-%d') + ".csv":
#			#csv files contain data for just one day
#			target = "https://www.madavi.de/sensor/" + link.get('href')[9:]
#			r = requests.get(target)
#			r.raise_for_status()
#			r = requests.get(target, stream=True)
#			with open(fname  + link.get('href'), 'wb') as f:
#				for chunk in r.iter_content(chunk_size=1024): 
#					if chunk: # filter out keep-alive new chunks
#						f.write(chunk)
#			pass
#		elif link.get('href')[-11:] == dy.strftime('%Y-%m') + ".zip":
#			#zip files contain a whole month of data
#			zip_file_url =  "https://www.madavi.de/sensor/" + link.get('href')
#			# fetch and extract zip files
#			r = requests.get(zip_file_url)
#			z = zipfile.ZipFile(io.BytesIO(r.content))
#			z.extractall(fname)
#			print ('INFO: completed file ('+ link.get('href') + ')')
main()


