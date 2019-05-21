import os, argparse, csv, json, glob, pprint
from dateutil import parser
from datetime import datetime, tzinfo, timezone
sensorvalues= ['P1', 'durP1', 'ratioP1', 'P2', 'durP2', 'ratioP2','humidity', 'temperature', 'pressure', 'pressure_at_sealevel']

#from pathlib import Path

def main ():
	format = "pretty"
	dname = './data/lil_dump/'
	input_directory = dname
	if ((input_directory[-1:] != '\\') & (input_directory[-1:] != '/')):
		input_directory = input_directory + "\\"
	file_list = glob.iglob(input_directory +'*.csv')
	for input_file in file_list:
		print ("working on next file...")
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
		write_json(tidy_dict, json_file, format)	

def write_json(data, json_file, format):
	location_id = list(data.keys())[0]
	d = {}
	if (os.path.isfile(json_file + location_id + '.json')):
		with open(json_file + location_id + '.json', "r") as f:
			d = json.load(f)
			for option in sensorvalues:
				d[location_id][option].update(data[location_id][option])
			d[location_id]['location'].update(data[location_id]['location'])
		with open(json_file + location_id + '.json', "w") as f:
			if format == "pretty":
				f.write(json.dumps(d, sort_keys=False, indent=4,))
			else:
				f.write(json.dumps(d))
			print(json_file + location_id + '.json' + " - updated")		
	else:
		with open(json_file + location_id + '.json', "w") as f:
			d[location_id] = data[location_id]
			if format == "pretty":
				f.write(json.dumps(d, sort_keys=False, indent=4,))
			else:
				f.write(json.dumps(d))
			print(json_file + location_id + '.json' + " - created")

def tidy_values(our_list):
	#organises ourlist as a dictionary of dictionaries follows:
	new_dict = {}
	location_id = str(our_list[0]['location'])
	if (new_dict.get(location_id, None)==None):
			new_dict[location_id] = {}
			new_dict[location_id]['location'] = {}
			for option in sensorvalues:
				new_dict[location_id][option] = {}
	
	for reading in our_list:
		timestamp = int((parser.parse(reading['timestamp']) - datetime(1970, 1, 1, tzinfo=timezone.utc)).total_seconds())
		new_dict[location_id]['location'].update({
			timestamp: {
				'latitude':reading['lat'],
				'longitude':reading['lon'],
				'timestamp' :reading['timestamp']
				}
			}) 
		for option in sensorvalues:
			if (option in reading):
				if (reading[option]):
					new_dict[location_id][option].update({
						timestamp: {
							'value' : float(reading[option]),
							'id':reading['sensor_id'],
							'sensor_type' : reading['sensor_type'],
							'timestamp' :reading['timestamp']
							}
						})
	return(new_dict)
main()