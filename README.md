# abdn_air_quality
Analysis of Aberdeen Air Quality sensor data

## Introduction 
This project aims to analyse and visualise the data generated from [the project](https://wiki.57north.org.uk/index.php/Projects:Air_Quality_Monitor) led by the 57 North hacklab to help citizens deploy their own air quality sensors. 


## Community Sensors 
There are currently four community sensors:  

| Luftdaten_ID | Madavi_ID |latitude| longitude|
| :------ |:----------|:--------|:--------|
| 5331    | 3654427   |57.138  |-2.077   |
| 7789    | **tbc**   |57.130  |-2.087   |
| 8554    | 12017738  |57.146  |-2.114   |
| 8733    | 3654335   |57.136  |-2.107   |


The sensors generate data which is uploaded to two sites: Luftdaten and Madavi. 

## Data locations

### Luftdaten

The Luftdaten URLs are in the format: http://archive.luftdaten.info/2018-05-10/2018-05-10_sds011_sensor_5331.csv  
These can be drilled down from http://archive.luftdaten.info into a date directory, then the CSV for a particular sensor from the table above. 

**Update 12-May-2018** The *get_historic_data.py* now retrieves 505 CSV files from the Luftdaten site to 10-May-2018

**Update 09-Feb-2019** The *get_historic_data.py* now has command line arguments for date range (-sd start date, -ed end date), it defaults to the previous dates if none are given. 

By using -v (verbose) argument the full download & errors are visible at the command line.

It also sorts the files into directories automatically. 

### Madavi

The Madavi URLs are in the format: https://www.madavi.de/sensor/csvfiles.php?sensor=esp8266-3654427  

This links to a page of data CSVs for the current month and Zip files for past months.  

**Update 14-May-2018** 
The *get_madavi.py* script now retrieves 
* the CSV files from the Madavi site to the day before the current date. At the time of writing these 73 files are for May, up to 12-May-2018.
* Then it downloads and extracts the zip files for previous months. These contain 300+ CSVs for previous months.

At present all of these downloads end up in the root directory from where I am moving them manually to the following structure.

```
\root
     \data
          \Luftdaten
                   \sensor_ID
                   \sensor_id
                   \etc
          \madavi
                 \sensor_ID
                 \sensor_id
                   \etc

```

## The data

Our next task it to make sense of the data
There is an issue with the Madavi data in that the header has two fewer columns than it has data. It is not yet clear if the header is missing attribute names, or the data contains superfluous columns. 


## To be done - priorities
Ideally we should download and extract the CSV / Zip files to their correct sub-folders.

## To be done - sometime
We should look at data from the [official monitoring equipment](http://www.scottishairquality.co.uk/latest/site-info.php?site_id=ABD0&view=latest).

## Getting Started

You will need Python 3 installed, you will also need a number of python modules, these can be installed via the command line use "pip install":
* pip install requests
* pip install python-dateutil
