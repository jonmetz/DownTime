import requests
import urllib2

from bs4 import BeautifulSoup
from reddit import n_sanity_check
from reddit import create_item
from reddit import durationfunctionstupid
from db_connect import Item
from db_connect import write_items

def clear_html(soup):
    for tag in soup.findAll(True): 
        tag.attrs = None
    return soup

def get_yahoo_top(keyword, number):
    url1="http://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20rss%20where%20url%3D%22http%3A%2F%2Frss.news.yahoo.com%2Frss%2F"
    url2="%22&format=json&callback="
    number = n_sanity_check(number)
    response = requests.get(url1+keyword+url2)
    data = response.json()
    items=[]
    for i in xrange(0,number):
        #print data.keys()
        item_response = data["query"]["results"]["item"][i]
        url = item_response["link"]
        name = item_response["title"]
        duration = durationfunctionstupid(requests.get(url).text)
        tag = keyword
        items.append(create_item(duration,name,tag,url))
    return items

                       
def yahoo_best_urls(keyword_list, number_each):
    url_item=[]
    for keyword in keyword_list:
        url_item+=get_yahoo_top(keyword,number_each)
    return url_item
           
def yahoo_add_db(keyword_list, number_each):
    url_dict=yahoo_best_urls(keyword_list, number_each)
    write_items(url_dict);           
   
 
if __name__=='__main__':
    #yahoo_add_db(["tech","world","politics"], 5)
    get_yahoo_top("tech", 5)
 