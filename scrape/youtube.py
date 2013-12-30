from sys import argv
import re
import requests
from db_connect import Item
from db_connect import write_items

def search_youtube(query):    
    search_url = "https://gdata.youtube.com/feeds/api/videos?alt=json"
    #id_start = len('http://gdata.youtube.com/feeds/api/videos/')
    response = requests.get(search_url, params={"q":query})
    #print response.url
    #print str(response.text)
    response = response.json()
    videos = response["feed"]["entry"]
    items = []
    for video in videos:
        # Lets get the title
        title = video["title"]["$t"]
        # Now lets get tags
        tag = video["category"][1]["term"]
        # We need to contact another api to get the length
        vid_id_long = video["id"]["$t"]
        key =  # Fill me in
        id_start = len('http://gdata.youtube.com/feeds/api/videos/')
        api_url_base = "https://www.googleapis.com/youtube/v3/videos?part=contentDetails%2Cstatistics&key="
        api_url_base += key
        vid_id = vid_id_long[id_start:]
        response = requests.get(api_url_base, params={"id": vid_id})
        response = response.json()
        duration = response["items"][0]["contentDetails"]["duration"] # Warning google is returning duration in this bullshit-ass form: PT5M29S
        duration = fmt_num(get_number(duration))#parse_google_time(duration)
        url = "https://www.youtube.com/watch?"+vid_id
        item = Item()
        item.duration = duration
        item.name = title
        item.add_tag(tag)
        item.url = url
        #if duration:
        items.append(item)
    return items
        
         


"""def parse_google_time(time_str):
    print time_str
    ms_regex = re.compile("PT(?P<M>\d*)M(?P<S>\d*)")    
    r = ms_regex.search(time_str)
    time_dict = r.groupdict()
    time_dict["H"] = 0
    if "H" in time_str:
        regex = re.compile("PT(?P<H>\d*)H")
        r = regex.search(string)
        time_dict["H"] = r.groupdict()["H"]
    if time_dict["M"]:
        time_dict["M"]=int(time_dict["M"])
    else:
        time_dict["M"]=0
    if time_dict["S"]:
        time_dict["S"]=int(time_dict["S"])
    else:
        time_dict["M"]=0
        return 60*60*time_dict["H"]+60*time_dict["M"]*time_dict["S"]
"""
"""def parse_google_time(time_str):
    #time_str = 
    time = 0
    time_tuple = find_time("H", time_str)
    time += time_tuple[1]
    time_str[until:]
    
def find_time(val, time_str):
    if val not in time_str:
        return (time_str, 0)
    else:
        try:
            until = c.index(val)
        except ValueError:
            return (time_str,0)
        finally:
            return (time_str[until:], int(time_str[:until]))
"""

def is_number(x):
    return (ord(x)>=ord('0') and ord(x)<=ord('9'))

def get_number(s):
    out={"H":0,"M":0,"S":0}
    i=0
    a=0
    while (i<len(s)): 
        #print is_number(not "1"[0])
        while (is_number(s[i])):
            #print s[i]
            #print a
            a*=10
            a+=ord(s[i])-ord('0')
            i+=1
        out[s[i]]=a
        a=0
        i+=1
    return out    

def fmt_num(num):
    return 360**num["H"]+60*num["M"]+num["S"]

            
if __name__=='__main__':
    items = search_youtube(sys.argv[0])
    write_items(items)


    
      
      
    
    
    

    
