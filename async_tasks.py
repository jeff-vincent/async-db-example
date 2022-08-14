import pymongo
import os

MONGO_HOST = os.environ.get('MONGO_HOST')
MONGO_PORT = os.environ.get('MONGO_PORT')

conn_str = f'mongodb://{MONGO_HOST}:{MONGO_PORT}'
client = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)
db = client.events_db
events = db.events

def insert_into_mongo(data):
    events.insert_one(data)