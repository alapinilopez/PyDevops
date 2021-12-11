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

def cars_classics_md(cars_classics):
    # cada clave hacerla bold y su valor ponerlo al lado en texto plano. Listarlo
    md_cars_classics = ""
    i = 1
    for document in cars_classics:
        md_cars_classics += "\n" + "### Item " + str(i) + "\n"
        i += 1
        for key in document:
            if key != "_id" and key != 'category' and key != 'year':
                md_cars_classics += "* " + key + ': ' + str(document[key]) + "\n"
            elif key == 'category':
                md_cars_classics = category(key, document[key], md_cars_classics)
            elif key == 'year':
                md_cars_classics += "* " + "**" + key + ': ' + str(document[key]) + "**" + "\n"
            else:
                continue
    assert isinstance(md_cars_classics, str)
    return md_cars_classics

def category(key, value, md_cars_classics):
    md_cars_classics += '* ' + key + ':' + '\n'
    for aspect in value:
        md_cars_classics += '* * ' + aspect + ': ' + str(value[aspect]) + '\n'
    return md_cars_classics