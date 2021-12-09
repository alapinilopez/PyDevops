import pymongo


uri = 'mongodb+srv://admin:admin@cluster0.thpbm.mongodb.net/PyDevops?retryWrites=true&w=majority'
def connection(uri):
    # client = pymongo.MongoClient(uri) #Utilizamos una funcion de pymongo para conectarnos a la base de datos
    global collection, db
    try:
        client = pymongo.MongoClient(uri)
        client.server_info()
    except pymongo.errors.ServerSelectionTimeoutError:
        print("El servidor está caído")
        exit()

    db = client.PyDevops
    collection = db.cars

connection(uri)

