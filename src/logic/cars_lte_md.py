# funcion que pase a md BBDD_query_lte.py
import sys
sys.path.append(".")  # Para poder debuguear sin tener que quitar el src.logic.
from src.BBDD_access.BBDD_connect import *
from src.BBDD_access.BBDD_query_lte import BBDD_query_lte



cars_cheaper = BBDD_query_lte(collection)


def cars_cheaper_md(cars_cheaper):
    # cada clave hacerla bold y su valor ponerlo al lado en texto plano. Listarlo
    md_cars_cheaper = ""
    for document in cars_cheaper:
        for key in document:
            if key != "_id" and key != "category":
                md_cars_cheaper += "* " + "**" + key + "**" + ': ' + str(document[key]) + "\n"
            else:
                continue
        md_cars_cheaper += "\n"
    return md_cars_cheaper
