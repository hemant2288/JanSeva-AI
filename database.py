from pymongo import MongoClient

client = MongoClient("YOUR_MONGODB_URL")
db = client["grievance_db"]
collection = db["complaints"]

def save_complaint(data):
    collection.insert_one(data)
