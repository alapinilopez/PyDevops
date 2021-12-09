import sys
sys.path.append(".")  # Para poder debuguear sin tener que quitar el src.logic.
from src.BBDD_access.BBDD_connect import *
from src.BBDD_access.BBDD_query_all import BBDD_query_all



cars = BBDD_query_all(collection)


def cars_all_md(cars):
    # cada clave hacerla bold y su valor ponerlo al lado en texto plano. Listarlo
    md_cars = ""
    for document in cars:
        for key in document:
            if key != "_id" and key != "category":
                md_cars += "* " + "**" + key + "**" + ': ' + str(document[key]) + "\n"
            else:
                continue
        md_cars += "\n"
    assert isinstance(md_cars, str)
    return md_cars
