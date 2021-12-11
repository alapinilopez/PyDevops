import pymongo


uri = 'mongodb+srv://admin:admin@cluster0.thpbm.mongodb.net/PyDevops?retryWrites=true&w=majority'
def connection(uri):
    global collection, db
    try:
        #Utilizamos una funcion de pymongo para conectarnos a la base de datos
        client = pymongo.MongoClient(uri)
        #client.server_info()
        db = client.PyDevops
        collection = db.cars
    except:
        print("El servidor está caído o no estas conectado a la red")
        exit()



connection(uri)

