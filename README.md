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

### Madavi

The Madavi URLs are in the format: https://www.madavi.de/sensor/csvfiles.php?sensor=esp8266-3654427  

This links to a page of data CSVs for the current month and Zip files for past months.  

**Update 13-May-2018** The *get_madavi.py* now retrieves 73 CSV files from the Madavi site to 12-May-2018. These are the current month CSVs. *Next* to grab the zips for previous files, download and extract these. 

There is an issue with the Madavi data in that the header has two fewer columns than it has data. It is not yet clear if the header is missing attribute names, or the data contains superfluous columns. 



## To be done
We should look at data from the [official monitoring equipment](http://www.scottishairquality.co.uk/latest/site-info.php?site_id=ABD0&view=latest).