from pymongo import MongoClient

Mongo = MongoClient("mongodb+srv://dbAdmin:dbAdmin@cluster0.e93in.mongodb.net/?retryWrites=true&w=majority")

db = Mongo.db