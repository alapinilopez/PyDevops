import sys
sys.path.append(".")
from src.BBDD_access.BBDD_connect import *
from form import *
from bson.objectid import ObjectId

RANGE_NAME = 'Delete!A:B' # Rango a solicitar de la hoja de calculo
values = main(RANGE_NAME)



key = '_id'
value = values[1]
cars_find = ""

# intentamos buscar y eliminar el objeto usando sí o sí _id.
# buscamos el item en la base de datos. Si lo encuentra lo borra. Si no lo encuentra nos lo indica
try:
    for document in collection.find({key:ObjectId(value)}):
        cars_find += str(document)
    if len(cars_find) != 0: # item encontrado
        collection.delete_one({key:ObjectId(value)})
        print("Coche borrado con éxito :D") 
    else: # item no encontrado
        print("El coche no existe o ya ha sido borrado")
except: # busqueda no realizada mediante _id o insertando el valor del _id erróneo
    print("inserte un id válido. Ejemplo:")
    print("Valor: 61aa4490cfc61872a92fe297")

