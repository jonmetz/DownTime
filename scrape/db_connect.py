import datetime
import requests
from pymongo import MongoClient

class Item:
    def __init__(self):
        self.name = None
        self.url = None
        self.tags = []
        self.duration = None
        self.date = None

    def add_tag(self, tag):
        self.tags.append(tag)

def db_connect(ip_addr="10.8.39.84:27018"):
    client = MongoClient('mongodb://%s/' % (ip_addr))
    return client.downtime

"""item should be a list"""
def write_item(item, db=db_connect()):
    collection = db.items
    item.date = datetime.datetime.utcnow()
    if item.name and item.url and item.tags and item.duration:
        collection.insert(item.__dict__)
        #print "Success"
        return "Success"
    else:
        "Fail check to see that all parameters are being detected " + item.name +' '+ item.url +' '+ item.tags +' '+ item.duration        

def write_items(items, db=db_connect()):
    map(lambda item: write_item(item, db), items)

def create_item (duration,name,tag,url):
    item = Item()
    item.duration = duration
    item.name = name
    item.add_tag(tag)
    item.url = url
    return item
                
