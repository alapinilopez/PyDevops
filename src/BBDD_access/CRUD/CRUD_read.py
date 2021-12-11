#modulo por si el usuario quiere buscar por consola algunos documentos en concreto
import sys
sys.path.append(".")
from src.BBDD_access.BBDD_connect import *
from bson.objectid import ObjectId

# hacer un find a la bbdd de las especificaciones que quiera el usuario
def BBDD_read(collection):
    cars_find = ''
    key = input('Llave: ')
    value = input('Valor: ')
    if value.isdigit(): #convertir el valor a un entero si el valor es numero en formato str
        value = int(value)
    if value == 'True': #convertir el valor a un booleano si el valor es la palabra True en formato str
        value = True
    if value == 'False': #convertir el valor a un booleano si el valor es la palabra False en formato str
        value = False
    for document in collection.find({key: value}):
        for key in document: #Añadimos los documentos encontrados a la variable cars_find
            cars_find += "* " + "**" + key + "**" + ': ' + str(document[key]) + "\n"
        cars_find += "\n"
    if len(cars_find) == 0: #Si no ha encontrado ningun documento se lo indicamos en la variable cars_find  
        cars_find = "Su base de datos no tiene coches con los parametros indicados"
    #Añadimos el resultado de la buscado a un archivo md para que el usuario lo pueda visualizar de manera mas bonita
    f = open("consulta.md", "w")
    f.write(cars_find)
    f.close()

BBDD_read(collection)