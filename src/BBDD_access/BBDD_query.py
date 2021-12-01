import sys
sys.path.append(".")
from src.BBDD_access.BBDD_connect import *

def BBDD_query(collection):
    array = []
    for document in collection.find({}):
        array.append(document)
    return array
#    f = open("BBDD.py", "w")
#    f.write(document)
#    f.close()
