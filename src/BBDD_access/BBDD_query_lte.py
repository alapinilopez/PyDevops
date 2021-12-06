# hacer un find a la bbdd de todos los coches con valor menor a 25. lte
import sys
sys.path.append(".")
from src.BBDD_access.BBDD_connect import *

def BBDD_query_lte(collection):
    cars_cheaper = []
    for document in collection.find({"price": {"$lte": 25}}):
        cars_cheaper.append(document)
    return cars_cheaper
