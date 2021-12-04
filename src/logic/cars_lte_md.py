# funcion que pase a md BBDD_query_lte.py
import sys
sys.path.append(".")  # Para poder debuguear sin tener que quitar el src.logic.
from src.BBDD_access.BBDD_connect import *
from src.BBDD_access.BBDD_query_lte import BBDD_query_lte



cars_cheaper = BBDD_query_lte(collection)


def cars_cheaper_md(cars_cheaper):
    try:
        assert len(cars_cheaper) > 0
        print("Base de datos OK")
    except:
        print("Su base de datos está vacía")

    # cada clave hacerla bold y su valor ponerlo al lado en texto plano. Listarlo
    key_value = ""
    for document in cars_cheaper:
        for key in document:
            if key != "_id" and key != "category":
                key_value += "* " + "**" + key + "**" + ': ' + str(document[key]) + "\n"
            else:
                continue
        key_value += "\n"
        # Añadimos los items al archivo md con la funcion open()
        f = open("hugo\Sites\carrenting\content\posts\precio.md", "w")
        f.write(key_value)
        f.close()
cars_cheaper_md(cars_cheaper)