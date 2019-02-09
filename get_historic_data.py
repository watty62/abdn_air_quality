import requests
from requests.exceptions import HTTPError
from dateutil import rrule, parser
import os

start_date = '2017-10-01'
end_date = '2018-05-12'

date_list = list(rrule.rrule(rrule.DAILY, dtstart=parser.parse(start_date), until=parser.parse(end_date)))

sensor_ids = ["5331", "7789", "8554", "8733"]

def create_urls (sid):

	for dy in date_list:
		file_add = "http://archive.luftdaten.info/" + dy.strftime('%Y-%m-%d') + "/"+ dy.strftime('%Y-%m-%d') + "_sds011_sensor_" + sid+ ".csv"
		fname = dy.strftime('%Y-%m-%d') + "_sds011_sensor_" + sid+ ".csv"
		
		try:
			r = requests.get(file_add)
			r.raise_for_status()
		except HTTPError:
			print ('Could not download page (' + fname + ')')
		else:
			
			# Save the string to a file
			r = requests.get(file_add, stream=True)
			with open(fname, 'wb') as f:
				for chunk in r.iter_content(chunk_size=1024): 
					if chunk: # filter out keep-alive new chunks
						f.write(chunk)
            

for sid in sensor_ids:
	create_urls (sid)


