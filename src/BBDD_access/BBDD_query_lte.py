import sys
sys.path.append(".")
from src.BBDD_access.BBDD_connect import *

# hacer un find a la bbdd de todos los coches con valor menor a 25. lte
def BBDD_query_lte(collection):
    cars_cheaper = []
    for document in collection.find({"price": {"$lte": 25}}):
        cars_cheaper.append(document)
    if len(cars_cheaper) == 0:
        print("Su base de datos no tiene coches con un precio inferior o igual a 25")
    return cars_cheaper
