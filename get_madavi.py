from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen
import re
import zipfile, io
 
mad_ids = ['3654427', '12017738','3654335']

def get_links(url):
	html_page = urlopen(url)
	soup = BeautifulSoup(html_page, "lxml")
	for link in soup.findAll('a'):
		
		if link.get('href')[-3:] == "csv":
			target = "https://www.madavi.de/sensor/" + link.get('href')
			
			# download the current month's CSV Madavi data
			r = requests.get(target, stream=True)
			with open(link.get('href'), 'wb') as f:
				for chunk in r.iter_content(chunk_size=1024): 
					if chunk: # filter out keep-alive new chunks
						f.write(chunk)
			
			pass
		elif link.get('href')[-3:] == "zip":
			zip_file_url =  "https://www.madavi.de/sensor/" + link.get('href')
		
			# fetch and extract zip files
			r = requests.get(zip_file_url)
			z = zipfile.ZipFile(io.BytesIO(r.content))
			z.extractall()


for mi in mad_ids:

	get_links("https://www.madavi.de/sensor/csvfiles.php?sensor=esp8266-" + mi)



