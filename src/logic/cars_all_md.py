import sys
sys.path.append(".")  # Para poder debuguear sin tener que quitar el src.logic.
from src.BBDD_access.BBDD_connect import *
from src.BBDD_access.BBDD_query_all import BBDD_query_all



cars = BBDD_query_all(collection)


def cars_all_md(cars):
    try:
        assert len(cars) > 0
        print("Base de datos OK")
    except:
        print("Su base de datos está vacía")
        return "Su base de datos está vacía"

    # cada clave hacerla bold y su valor ponerlo al lado en texto plano. Listarlo
    global key_value
    key_value = ""
    for document in cars:
        for key in document:
            if key != "_id" and key != "category":
                key_value += "* " + "**" + key + "**" + ': ' + str(document[key]) + "\n"
            else:
                continue
        key_value += "\n"
    assert isinstance(key_value, str)
    return key_value


cars_all_md(cars)
