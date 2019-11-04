from pymongo import MongoClient
from settings import Cfg
from pprint import pprint

connStr = "mongodb://{}:{}@{}:{}/".format(Cfg.usr, Cfg.pwd, Cfg.url, Cfg.port)

client = MongoClient(connStr)

database = client.get_database(Cfg.database)

collections = []
for collection in Cfg.collections.split(" "):
    collections.append(database[collection])

for collection in collections:
    print(collection.full_name)
    for doc in collection.find():
        pprint(doc)
