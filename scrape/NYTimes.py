import requests
from bs4 import BeautifulSoup
from db_connect import Item
from db_connect import write_items
from reddit import durationfunctionstupid

dev_key = # Fill me in
nytimes_url = "http://api.nytimes.com/svc/news/v3/content/all/all/48.json?api-key="+dev_key
r = requests.get(nytimes_url)
response = r.json()

def nytimes_urls(category):
	url_list = []
	for item in response["results"]:
            if item["section"] == category:
                article = Item()
                article.name = item["title"].encode('utf-8')
                html = requests.get(item["url"].encode('utf-8')).text
                article.url = item["url"].encode('utf-8')
                article.duration = durationfunctionstupid(html)
                article.add_tag(category)
                url_list.append(article)
	return url_list

def main():
    all_items = []
    #NYTimes sections corresponding to Downtime categories
    #Categories = Arts, Sports, Tech, Entertainment, Finance, World
    #Corresponding to NYTimes sections = Arts, ___,  Technology, Style, Business, World
    for x in nytimes_urls("Arts"): all_items.append(x)
    for x in nytimes_urls("Sports"): all_items.append(x)
    for x in nytimes_urls("Technology"): all_items.append(x)
    for x in nytimes_urls("Style"): all_items.append(x)
    for x in nytimes_urls("Business"): all_items.append(x)
    for x in nytimes_urls("World"): all_items.append(x)

    #print all_items
    #write all items
    write_items(all_items)
    dir(all_items)
    return all_items



