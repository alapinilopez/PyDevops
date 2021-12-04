import sys
sys.path.append(".")
from src.BBDD_access.BBDD_connect import *

def BBDD_query_all(collection):
    array = []
    for document in collection.find({}):
        array.append(document)
    return array

