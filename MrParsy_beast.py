import os, argparse, csv, json, glob, pprint
from dateutil import parser
from datetime import datetime, tzinfo, timezone
sensorvalues= ['P1', 'durP1', 'ratioP1', 'P2', 'durP2', 'ratioP2','humidity', 'temperature', 'pressure', 'pressure_at_sealevel']

#from pathlib import Path

def main ():
	format = "pretty"
	dname = './data/big_dump/'
	input_directory = dname
	if ((input_directory[-1:] != '\\') & (input_directory[-1:] != '/')):
		input_directory = input_directory + "\\"
	file_list = glob.iglob(input_directory +'*.csv')
	for input_file in file_list:
		print ("working on next file...", input_file)
		output_file = dname
		read_csv(input_file, output_file, format)


def read_csv(file, json_file, format):
	csv_rows = []
	with open(file) as csvfile:
		dictionary = csv.DictReader(csvfile, delimiter = ";")
		title = dictionary.fieldnames
		for row in dictionary:
			csv_rows.extend([{title[i]:row[title[i]] for i in range(len(title))}])
		tidy_dict = tidy_values(csv_rows)
		#pp = pprint.PrettyPrinter(indent=1)
		#pp.pprint(tidy_dict)
	write_json(tidy_dict, json_file, format)
	newfile = file.replace("./data/big_dump","./data/big_dump/done")
	print (file, newfile)
	os.rename(file, newfile)

def write_json(data, json_file, format):
	location_id = list(data.keys())[0]
	d = {}
	if (os.path.isfile(json_file + location_id + '.json')):
		with open(json_file + location_id + '.json', "r") as f:
			d = json.load(f)
			d[location_id]['info'].update(
				data[location_id]['info']
				)
			for timestamp in data[location_id]['readings']:
				if (str(timestamp) in d[location_id]['readings']):
					d[location_id]['readings'][str(timestamp)].update(data[location_id]['readings'][timestamp])
				else:
					d[location_id]['readings'].update({str(timestamp):data[location_id]['readings'][timestamp]}) 
		
		with open(json_file + location_id + '.json', "w") as f:
			if format == "pretty":
				f.write(json.dumps(d, sort_keys=True, indent=4))
			else:
				f.write(json.dumps(d))
			print(json_file + location_id + '.json' + " - updated")		
	else:
		with open(json_file + location_id + '.json', "w") as f:
			d[location_id] = data[location_id]
			if format == "pretty":
				f.write(json.dumps(d, sort_keys=True, indent=4))
			else:
				f.write(json.dumps(d))
			print(json_file + location_id + '.json' + " - created")

def tidy_values(our_list):
	#organises ourlist as a dictionary of dictionaries follows:
	new_dict = {}
	location_id = str(our_list[0]['location'])
	reading = our_list[0]
	if (new_dict.get(location_id, None)==None):
			new_dict[location_id] = {}
			new_dict[location_id]['info'] = {
				'latitude':reading['lat'],
				'longitude':reading['lon'],
				'location_id':location_id
				}
			new_dict[location_id]['readings'] = {}
			for option in sensorvalues:
				if (option in reading):
					if (reading[option]):
						new_dict[location_id]['info'].update({
							option: {
								reading['sensor_type']:reading['sensor_id'],
								}
							})
	
	for reading in our_list:
		reading_ts = reading['timestamp']
		if reading_ts.find('+')<0:
			#adds timezone if none given.
			#this is required for timestamp calculation below
			reading_ts = reading_ts + '+00:00'
			reading_ts = parser.parse(reading_ts)
		timestamp = int((reading_ts - datetime(1970, 1, 1, tzinfo=timezone.utc)).total_seconds())
		timestamp = timestamp // 360 * 360 #round to nearest minute
		new_dict[location_id]['readings'][timestamp] = {}
		for option in sensorvalues:
			if (option in reading):
				if (reading[option]):
					new_dict[location_id]['readings'][timestamp].update({
						option : float(reading[option])
						})
	return(new_dict)
main()