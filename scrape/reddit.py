import requests
import urllib2


from bs4 import BeautifulSoup
from db_connect import Item
from db_connect import create_item
from db_connect import write_items

#fp=open("out.txt","w")

def n_sanity_check(number):
    """Make sure were not accidentally requesting a number of pages less than 1 or greater than 100"""
    #number = min(99,number)
    #number = max(1,number)
    #return number
    if number > 99: # This is alot clearer no?
        return 99
    elif number < 1:
        return 1
    else:
        return number

def reddit_request(url, params):
    """Adds user-agent=downtime to params and then requests the url from reddit, so you don't have to add in the goddamn user agent each time"""
    payload = params
    keys=payload.keys()
    if 'user-agent' not in keys:
        payload['user-agent'] = 'downtime'
    else:
        pass
    return requests.get(url, params=payload)

def durationfunctionstupid(html):
    soup = BeautifulSoup(html)
    return len(soup.get_text())/30 -200 #Hopefully this works...

        
#def get_times_yahoo(search):
#    payload = {'query':search}
#    return requests.get("http://answers.yahooapis.com/answersservice/v1/questionsearch", params=payload)
        
def get_reddit_search(search, number):
    """Get top 'number' results from redit from from searching 'search'."""
    number = n_sanity_check(number)
    payload = {'q': search, 'limit': number+1}
    return reddit_request('http://www.reddit.com/search.json', payload) 
    
# def get_reddit_searchurls(search, number):
    # number = n_sanity_check(number)
    # r=get_reddit_search(search,number)
    # data=r.json()
    # i=0
    # while (i<number):
        # #fp.write(data["data"]["children"][i]["data"]["url"])
        # print data["data"]["children"][i]["data"]["url"]
        # #fp.write('\n')
        # i+=1

def get_reddit_top(keyword, number):
    """Return the top 'number' age-appropriate pages from the 'keyword' subredit in an Item list. May crash if keyword is not a subredit"""
    number = n_sanity_check(number)
    payload = {'limit': number+1}
    response = reddit_request('http://www.reddit.com/r/'+keyword+'.json', payload)
    data=response.json()
    items=[]
    for i in xrange(0,number):
        #fp.write(data["data"]["children"][i]["data"]["url"])
        #fp.write('\n')
        item_response = data["data"]["children"][i]["data"]
        if item_response["over_18"]: # Get that shit outta here
            continue
        url = item_response["url"]
        name = item_response["title"]
        duration = durationfunctionstupid(requests.get(url).text)
        #print duration
        tag = item_response["subreddit"]
        items.append(create_item(duration,name,tag,url))
    return items


# def getreddittopurls(search, number):
# number=min(99,number);
# number=max(1,number);
# r=get_reddit_top("cat",number)
# data=r.json()
# i=0
# while (i<number):
# fp.write(data["data"]["children"][i]["data"]["url"])
# fp.write('\n')
# i+=1
def get_reddit_top_urls(keyword, number):
    """Returns get_reddit_top, but allows for replacements of the keyword with an appropriate subreddit."""
    if keyword.lower()=="world":
        keyword="worldnews"
    if keyword.lower()=="tech":
        keyword="technology"
    if keyword.lower()=="arts":
        keyword="worldnews"
    #r=get_reddit_top(keyword,number)
    return get_reddit_top(keyword, number)#r.json()


def reddit_best_urls(keyword_list, number_each):
    url_item=[]
    for keyword in keyword_list:
        url_item+=get_reddit_top_urls(keyword,number_each)
    return url_item
    
def reddit_add_db(keyword_list, number_each):
    url_dict=reddit_best_urls(keyword_list, number_each)
    write_items(url_dict);         
            
#data=r.json()
#fp=open("out.txt","w")
#i=10
#for(
#fp.write()
#getreddittop("monkey",6)

#getreddittopurls("monkey",6)

if __name__=='__main__':
    #print reddit_best_urls(["world","cat"],2)
<<<<<<< HEAD
    reddit_add_db(["tech","sports","arts","entertainment","finance","world","cats","politics"], 50)
=======
    reddit_add_db(["cat"], 99)
>>>>>>> c5bdbcd... Added modulized duration function
