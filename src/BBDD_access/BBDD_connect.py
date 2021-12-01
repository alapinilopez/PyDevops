import pymongo

uri = 'mongodb+srv://admin:admin@cluster0.thpbm.mongodb.net/PyDevops?retryWrites=true&w=majority'
client = pymongo.MongoClient(uri) #Utilizamos una funcion de pymongo para conectarnos a la base de datos

db = client.PyDevops 
collection = db.cars
