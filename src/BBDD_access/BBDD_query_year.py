import sys
sys.path.append(".")
from src.BBDD_access.BBDD_connect import *

# hacer un find a la bbdd de todos los coches con valor menor a 2017. lt
def BBDD_query_year(collection):
    cars_classics = []
    for document in collection.find({"year": {"$lt": 2017}}):
        cars_classics.append(document)
    if len(cars_classics) == 0:
        print("Su base de datos no tiene coches clásicos")
    return cars_classics
