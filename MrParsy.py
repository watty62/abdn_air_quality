import os, argparse, csv, json, glob
#from pathlib import Path
aparser = argparse.ArgumentParser(description='convert csv to json')
aparser.add_argument(
    '-f', '--file', dest='fname', action='store',
    help='file name for csv to be parsed')
aparser.add_argument(
    '-d', '--dir', dest='dname', action='store',
    help='directory name for all csv files to be parsed')
args = aparser.parse_args()

def main ():
	format = "pretty"
	if (args.fname): 
		input_file = args.fname
		output_file = input_file[:len(input_file)-3] + "json"
		read_csv(input_file, output_file, format)
	elif (args.dname):
		input_directory = args.dname
		if ((input_directory[-1:] != '\\') & (input_directory[-1:] != '/')):
			input_directory = input_directory + "\\"
		file_list = glob.iglob(input_directory +'*.csv')
		for input_file in file_list:
			output_file = input_file[:len(input_file)-3] + "json"
			read_csv(input_file, output_file, format)
	else:
		print ('ERROR: no file given to parse')
		exit()

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
		print(json_file + " - complete")		

main()