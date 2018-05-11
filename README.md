# abdn_air_quality
Analysis of Aberdeen Air Quality sensor data

This project aims to analyse and visualise the data generated from [the project](https://wiki.57north.org.uk/index.php/Projects:Air_Quality_Monitor) led by the 57 North hacklab to help citizens deploy their own air quality sensors. 

Once done, we should look at data from the [official monitoring equipment](http://www.scottishairquality.co.uk/latest/site-info.php?site_id=ABD0&view=latest).


| Sensor  | Madavi_ID | Luftdaten_ID |
| :------ |:----------| :---------- |
| one     | 3654427   | 5331         |
| two     | tbc       | 7789         |
| three   | 12017738  | 8554         |
| four    | 3654335   | 8733         |


The Madavi URLs are in the format: https://www.madavi.de/sensor/csvfiles.php?sensor=esp8266-3654427  

This links to a page of data CSVs for the current month and Zip files for past months.  

The Luftdated URLs are in the format: http://archive.luftdaten.info/2018-05-10/2018-05-10_sds011_sensor_5331.csv  
These can be drilled down from http://archive.luftdaten.info into a date directory, then the CSV for a particular sensor from the table above. 