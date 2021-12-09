import sys
sys.path.append(".")  # Para poder debuguear sin tener que quitar el src.logic.
from src.BBDD_access.BBDD_connect import *
from src.BBDD_access.BBDD_query_year import BBDD_query_year


cars_classics = BBDD_query_year(collection)

def cars_classics_md(cars_classics):
    # cada clave hacerla bold y su valor ponerlo al lado en texto plano. Listarlo
    md_cars_classics = ""
    for document in cars_classics:
        # for car_id, car_info in document:  # iterar el diccionario anidado
        for key in document:
            if key != "_id" and key != "category":
                md_cars_classics += "* " + "**" + key + "**" + ': ' + str(document[key]) + "\n"
            else:
                continue
        md_cars_classics += "\n"
    return md_cars_classics
