import sys
sys.path.append(".")
from src.BBDD_access.BBDD_connect import *

def BBDD_query_year(collection):
    cars_year = []
    for document in collection.find({"year": {"$gte": 2020}}):
        cars_year.append(document)
    return cars_year

if __name__ == "__main__":
    assert BBDD_query_year(collection) != -1