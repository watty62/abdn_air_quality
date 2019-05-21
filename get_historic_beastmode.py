from bs4 import BeautifulSoup
import os.path
import pprint
import requests

def get_all_historic_data(sensor_list):
	print('requesting...')
	r  = requests.get("http://archive.luftdaten.info/")
	print('got request!')
	data = r.text
	soup = BeautifulSoup(data, 'html.parser')
	for link in reversed(soup.find_all('a')):
		print('requesting2...')
		date = link.get('href')
		r2  = requests.get("http://archive.luftdaten.info/" + date)
		print('got request2!', date)
		data2 = r2.text
		soup2 = BeautifulSoup(data2, 'html.parser')
		print('checking for matches...')
		for link2 in soup2.find_all('a'):
			linkname = link2.get('href')
			full_link = "http://archive.luftdaten.info/" + date + linkname
			if full_link[-3:]=="csv":
				for sensor in sensor_list:
					if ((full_link.find('_'+sensor+'.')>0) or (full_link.find('_'+sensor+'_')>0)):
						print("  downloading...", sensor, full_link)
						downloader(full_link, linkname)

def downloader (full_link, name):
	fname = "./data/big_dump" + "/" + name
	if not (os.path.isfile(fname)):
		try:
			r = requests.get(full_link)
			r.raise_for_status()
			print ("  complete!")
		except HTTPError:
			print ('  ERROR: Could not download file (' + fname + ')')
		else:	
			# Save the string to a file
			r = requests.get(full_link, stream=True)
			with open(fname, 'wb') as f:
				for chunk in r.iter_content(chunk_size=1024): 
					if chunk: # filter out keep-alive new chunks
						f.write(chunk)
	else:
		print ("  already exists")

def get_data(box):
	# gets luftdaten data for all sensors within a given lat/log box
	# box = 'lat_0,long_0,lat_1,long_1'
	r = requests.get('https://api.luftdaten.info/v1/filter/box=' + box)
	my_json = r.json()
	return my_json


def tidy_values(our_list):
	# organises ourlist as a dictionary of dictionaries follows:

	new_dict = {}
	for sensor in our_list:
		location_id = str(sensor['location']['id'])
		if (new_dict.get(location_id, None) == None):
			new_dict[location_id] = {}
			new_dict[location_id]['location'] = sensor['location']
		for sensordata in sensor['sensordatavalues']:
			new_dict[location_id][sensordata['value_type']] = {
				'value': float(sensordata['value']),
				'timestamp': sensor['timestamp'],
				'id': sensor['id'],
				'sensor_type': sensor['sensor']['sensor_type'],
				'sensor_id' : str(sensor['sensor']['id'])}
	return (new_dict)

def main():
	Aberdeen = [57.25, -2.40, 57.00, -2.00]
	Aberdeenshire = [57.75, -4.00, 56.74, -1.70]
	WesternEurope = [60, -10, 40, 20] 
	box = Aberdeenshire
	strbox = (str(box)[1:-1]).replace(" ", "")
	print('getting list')
	our_list = get_data(strbox)
	print('got list')
	#our_list is a list of dictionaries
	print ('tidying list')
	tidy_list = tidy_values(our_list)
	sensor_list = []
	for location_id in tidy_list:
		for sensordata in tidy_list[location_id]:
			if sensordata != 'location':
				sensor_list.append(tidy_list[location_id][sensordata]['sensor_id'])
	sensor_list = list(set(sensor_list))
	print("looking for the following sensors:")
	print(sensor_list)
	# tidy_list is a list of dictionaries that is easier to work with.
	#weather_data = get_weather.main(box)
	#pp = pprint.PrettyPrinter(indent=1)
	#pp.pprint (tidy_list)
	# pp.pprint (weather_data)
	print('getting historic data')
	get_all_historic_data(sensor_list)
	return ()


if __name__ == '__main__':
	main()