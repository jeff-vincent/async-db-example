import pymongo

conn_str = 'mongodb://mongo:27017'
client = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)
db = client.events_db
events = db.events

def insert_into_mongo(data):
    events.insert_one(data)