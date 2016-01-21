import feedparser
import facebook
import re
from time import strftime

with open('mercury/mercury/access_token', 'r') as file:
	access_token = file.read()

graph = facebook.GraphAPI(access_token=access_token)

feed = "http://spotthestation.nasa.gov/sightings/xml_files/India_None_Chennai.xml"
parsed = feedparser.parse(feed)

if parsed.entries:
	for entry in parsed.entries:
		pass_title = entry.title
		date_today = strftime("%Y-%m-%d")
		if date_today in pass_title:
			pass_details = entry.description
			pass_details = pass_details.replace('<br />', '')
			pass_details = pass_details.encode('utf-8')
			post = "ISS Pass for today!\n" + pass_details
			graph.put_object(parent_object='me', connection_name='feed', message=post)