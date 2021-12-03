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

    # cada clave hacerla bold y su valor ponerlo al lado en texto plano. Listarlo
    key_value = ""
    for document in cars:
        # for car_id, car_info in document:  # iterar el diccionario anidado
        for key in document:
            if key != "_id" and key != "category":
                key_value += "* " + "**" + key + "**" + ': ' + str(document[key]) + "\n"
            else:
                continue
        key_value += "\n"
        # Añadimos los items al archivo md con la funcion open()
        f = open("hugo\Sites\carrenting\content\posts\main.md", "w")
        f.write(key_value)
        f.close()


cars_all_md(cars)
