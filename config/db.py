from pymongo import MongoClient

client = MongoClient("mongodb+srv://Maxfree:@learning.xzyzvfd.mongodb.net/?retryWrites=true&w=majority&appName=Learning")

db = client["STJMPDO"]

user_collection = db["users"]