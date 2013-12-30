import requests
from db_connect import Item

#fp=open("out.txt","w")
#i=10
#for(


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

def get_times_yahoo(search):
    payload = {'query':search}
    return requests.get("http://answers.yahooapis.com/answersservice/v1/questionsearch", params=payload)
        
def get_reddit_search(search, number):
    number = n_sanity_check(number)
    payload = {'q': search, 'limit': number+1}
    return reddit_request('http://www.reddit.com/search.json', payload) 
    
def get_reddit_searchurls(search, number):
    number = n_sanity_check(number)
    r=get_reddit_search("cat",number) # Is this an example you've hard coded?
    data=r.json()
    i=0
    while (i<number):
        #fp.write(data["data"]["children"][i]["data"]["url"])
        print data["data"]["children"][i]["data"]["url"]
        #fp.write('\n')
        i+=1

def get_reddit_top(keyword, number):
    number = n_sanity_check(number)
    payload = {'limit': number+1}
    response = reddit_request('http://www.reddit.com/r/'+keyword+'.json', payload)
    for i in xrange(0,number):
        #fp.write(data["data"]["children"][i]["data"]["url"])
        #fp.write('\n')
        item_response = response["data"]["children"][i]["data"]
        if item_response["over_18"]: # Get that shit outta here
            break
        url = item_response["url"]
        name = item_response["title"]
        duration = ""
        tag = item_response["subreddit"]
        item = Item()
        item.duration = duration
        item.name = name
        item.add_tag(tag)
        item.url = url
        items.append(item)
    return items

def reddit_request(url, params):
    """So you don't have to add in the goddamn user agent each time"""
    payload = params
    keys=payload.keys()
    if 'user-agent' not in keys:
        payload['user-agent'] = 'downtime'
    else:
        pass
    return requests.get(url, params=payload)
    
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
    number = n_sanity_check(number)
    if keyword.lower()=="world":
        keyword="worldevents"
    #r=get_reddit_top(keyword,number)
    return get_reddit_top(keyword, number)#r.json()
                        
def reddit_best_urls(keyword_list, number_each):
    url_dict={}
    for keyword in keyword_list:
        url_dict[keyword]=get_reddit_top_urls(keyword,number_each)
    return url_list
        
			
#data=r.json()
#fp=open("out.txt","w")
#i=10
#for(
#fp.write()
#getreddittop("monkey",6)

#getreddittopurls("monkey",6)

if __name__=='__main__':
    print reddit_best_urls(["world","cat"],2)
