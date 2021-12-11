import sys
sys.path.append(".")
from src.BBDD_access.BBDD_connect import *
from bson.objectid import ObjectId
# hacer que se borre un item solo por su id
def CRUD_delete(collection):
    print("inserte el id del coche que desea borrar en 'Valor: '")
    key = input('Llave: ')
    value = input('Valor: ')
    cars_find = ""
    
    try: # intentamos buscar el objeto usando sí o sí _id. Si no se usa ese campo printea que hagas la busqueda mediante _id
        for document in collection.find({key:ObjectId(value)}): # buscamos item en la base de datos. Si lo encuentra lo borra. Si no lo encuentra lo printea
            cars_find += str(document)
        if len(cars_find) != 0:
            collection.delete_one({key:ObjectId(value)}) # item encontrado
            print("Coche borrado con éxito :D") 
        else:
            print("El coche no existe o ya ha sido borrado") # item no encontrado
    except: # busqueda no realizada mediante _id o insertando el valor del _id erróneo
        print("inserte un id válido. Ejemplo:")
        print("Llave: _id")
        print("Valor: 61aa4490cfc61872a92fe297")
CRUD_delete(collection)
