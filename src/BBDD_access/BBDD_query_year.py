import sys
sys.path.append(".")
from src.BBDD_access.BBDD_connect import *

def BBDD_query_year(collection):
    cars_classics = []
    for document in collection.find({"year": {"$lte": 2017}}):
        cars_classics.append(document)
    return cars_classics

if __name__ == "__main__":
    assert BBDD_query_year(collection) != -1 #Comprobamos que hay una colección