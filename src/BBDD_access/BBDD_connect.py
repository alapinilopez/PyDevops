import pymongo


uri = "mongodb+srv://admin:admin@cluster0.thpbm.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
client = pymongo.MongoClient(uri)

db = client.PyDevops
collection = db.cars
