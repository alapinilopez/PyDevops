import sys
sys.path.append(".")
from src.BBDD_access.BBDD_connect import *

#def BBDD_query(collection):
array = []
dict = {}
for document in collection.find({}):
    array.append(document)
print(array)
#    f = open("BBDD.py", "w")
#    f.write(document)
#    f.close()
#BBDD_query(collection)