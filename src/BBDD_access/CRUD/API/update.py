import sys
sys.path.append(".")
from src.BBDD_access.BBDD_connect import *
from form import *
from bson.objectid import ObjectId

RANGE_NAME = 'Update!B:C' # Rango a solicitar de la hoja de calculo
values = main(RANGE_NAME)
# Valor a modificar
value = values[0]
if values[1] == 'FALSE':
    new_value = False
else:
    new_value = True
# Modificamos la diponibilidad de un vehículo. Lo identificamos por su ID
collection.update_one({'_id':ObjectId(value)}, {'$set': {'available': new_value}})

cars_find = ""
try:
    for document in collection.find({'_id':ObjectId(value)}):
        cars_find += str(document)
    if len(cars_find) != 0: # item encontrado
        collection.update_one({'_id':ObjectId(value)}, {'$set': {'available': new_value}})
        print("Coche modificado con éxito :D") 
    else: # item no encontrado
        print("El coche indicado no existe")
except: # busqueda no realizada mediante _id o insertando el valor del _id erróneo
    print("inserte un id válido. Ejemplo:")
    print("Valor: 61aa4490cfc61872a92fe297")