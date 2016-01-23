import feedparser
import facebook
import re
from fly import ISS
from datetime import date, timedelta

with open('mercury/mercury/access_token', 'r') as file:
	access_token = file.read()

graph = facebook.GraphAPI(access_token=access_token)
flyer = ISS() 

feed = "http://spotthestation.nasa.gov/sightings/xml_files/India_None_Chennai.xml"
parsed = feedparser.parse(feed)

if parsed.entries:
	for entry in parsed.entries:
		pass_title = entry.title
		date_tomorrow = date.today() + timedelta(days=2)
		date_tomorrow_string = date_tomorrow.strftime("%Y-%m-%d")
		if date_tomorrow_string in pass_title:
			pass_details = entry.description
			pass_details = pass_details.replace('<br />', '')
			pass_details = pass_details.replace('\t', '')
			pass_details = pass_details.encode('utf-8')
			post = "Upcoming ISS Pass!\n" + pass_details
			poster = flyer.fly(pass_details)
			graph.put_photo(image=open(poster), message=post)