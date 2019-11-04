from pymongo import MongoClient
from settings import Cfg
from pathlib import Path
from pprint import pprint
from bson import json_util
import json


def writeToJSONFile(collection):
    file = open("{}.json".format(collection.full_name), "w")
    file.write('[')

    cursor = collection.find()
    qnt_cursor = 0
    for document in cursor:
        file.write(json.dumps(document, indent=4))

        qnt_cursor += 1
        num_max = cursor.count()
        if (num_max == 1):
            file.write(json.dumps(document, indent=4))
        elif (num_max >= 1 and qnt_cursor <= num_max-1):
            file.write(json.dumps(document, indent=4))
            file.write(',')
        elif (qnt_cursor == num_max):
            file.write(json.dumps(document, indent=4))
    file.write(']')
    return file



connStr = "mongodb://{}:{}@{}:{}/".format(Cfg.usr, Cfg.pwd, Cfg.url, Cfg.port)

client = MongoClient(connStr)

database = client.get_database(Cfg.database)

collections = []
for collection in Cfg.collections.split(" "):
    collections.append(database[collection])

for collection in collections:
    for doc in collection.find():
        j = json_util.dumps(doc)
        # json.dump(
        #     json_util.dumps(doc),
        #     open(Path('.') / "docs" / "{}_{}.json".format(
        #         collection.full_name, doc['_id']
        #     ), "w"),
        #     indent=4
        # )
        print(json.dumps(json.loads(j), indent=4))
