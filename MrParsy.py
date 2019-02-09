import os, argparse, csv, json
#from pathlib import Path
aparser = argparse.ArgumentParser(description='convert csv to json')
aparser.add_argument(
    '-f', '--file', dest='fname', action='store',
    help='file name for csv to be parsed')
args = aparser.parse_args()

def main ():
	if (args.fname): 
		input_file = args.fname
	else:
		print ('ERROR: no file given to parse')
		exit()
	#read csv file
	#input_file = csv.DictReader(open(fname, "r"), delimiter = ";")

	output_file = input_file[:len(input_file)-3] + "json"
	format = "pretty"
	read_csv(input_file, output_file, format)

def read_csv(file, json_file, format):
	csv_rows = []
	with open(file) as csvfile:
		reader = csv.DictReader(csvfile, delimiter = ";")
		title = reader.fieldnames
		for row in reader:
			csv_rows.extend([{title[i]:row[title[i]] for i in range(len(title))}])
		write_json(csv_rows, json_file, format)	

def write_json(data, json_file, format):
	with open(json_file, "w") as f:
		if format == "pretty":
			f.write(json.dumps(data, sort_keys=False, indent=4,))
		else:
			f.write(json.dumps(data))		

main()