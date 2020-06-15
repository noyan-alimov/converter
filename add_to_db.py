import json
from pymongo import MongoClient

client = MongoClient('mongodb+srv://noyan123:noyan123@cluster0.svs8u.mongodb.net/SteelMinesDB?retryWrites=true&w=majority')
db = client.SteelMinesDB


def addToDatabase(name):
  collection = db[name]
  with open('./json_files/{}.json.'.format(name)) as f:
      file_data = json.load(f)

  collection.insert_many(file_data)

  client.close()
