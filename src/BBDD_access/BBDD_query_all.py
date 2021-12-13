import sys
sys.path.append(".")
from src.BBDD_access.BBDD_connect import *

def BBDD_query_all(collection):
    cars_all = []
    #buscamos todos los documentos de la coleccion y lo añadimos a un array
    for document in collection.find({}):
        cars_all.append(document)
    if len(cars_all) == 0:
        print('Su base de datos esta vacia')
    return cars_all

if __name__ == "__main__":
    assert BBDD_query_all(collection) != -1 #Comprobamos que hay una colección