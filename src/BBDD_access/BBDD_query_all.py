import sys
sys.path.append(".")
from src.BBDD_access.BBDD_connect import *

def BBDD_query_all(collection):
    cars_all = []
    #buscamos todos los documentos de la coleccion 'cars_all' y lo añadimos a un array
    for document in collection.find({}):
        cars_all.append(document)
    return cars_all
