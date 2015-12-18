import feedparser
import facebook
import re
from time import strftime

feed = "http://spotthestation.nasa.gov/sightings/xml_files/India_None_Chennai.xml"
graph = facebook.GraphAPI(access_token='')

parsed = feedparser.parse(feed)
if parsed.entries:
	next_pass = parsed.entries[0]
	pass_title = next_pass.title
	date_today = strftime("%Y-%m-%d")
	if date_today in pass_title:
		pass_details = next_pass.description
		pass_details = pass_details.replace('<br />', '')
		pass_details = pass_details.encode('utf-8')
		post = "ISS Pass for today!\n" + pass_details
		graph.put_object(parent_object='me', connection_name='feed', 
			message=post)