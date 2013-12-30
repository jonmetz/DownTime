from urllib2 import urlopen
import requests
from json import load 
from db_connect import Item
from db_connect import write_items
from reddit import durationfunctionstupid
def search_npr(url_num):
	url = 'http://api.npr.org/query?apiKey=' 
	key = 'MDEyNTYyODg1MDEzODM5ODAxNTIzYjc2ZQ001'
	url = url + key
	url += '&numResults=1&format=json&id='
	url += str(url_num)

	#open our url, load the JSON
	response = urlopen(url)
	json_obj = load(response)

	items = []
	textLength=0.
	#parse our story

	item = Item()

	for story in json_obj['list']['story']:
		title = story['title']['$text']
		link = story['link'][0]['$text']
		
        item.name = title
        item.url = link
        print link
        item.add_tag("world")
    
	for paragraph in story['textWithHtml']['paragraph']:
		text = paragraph['$text']
		textLength +=len(text)

	time = durationfunctionstupid(requests.get(url).text)
	item.duration = time
	items.append(item)
	return items

if __name__ == "__main__":
	write_items(search_npr(1003))
