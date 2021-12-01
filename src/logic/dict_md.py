import sys
sys.path.append(".") #Para poder debuguear sin tener que quitar el src.logic.
from src.BBDD_access.BBDD_query import BBDD_query
from src.BBDD_access.BBDD_connect import *

cars = BBDD_query(collection)

def dict_md(cars):
    try:
        assert len(cars) > 0
        print("Base de datos OK")
    except:
        print("Su base de datos está vacía")

    # cada clave hacerla bold y su valor ponerlo al lado en texto plano
    bold = "**"
    key_value = ""
    for document in cars:
        #for car_id, car_info in document:  # iterar el diccionario anidado
        for key in document:
            if key == "_id":
                continue
            else:
                key_value += bold + key + bold + ': ' + str(document[key]) + "\n"
        key_value += "\n"
        # Añadimos los items al archivo md con la funcion open()
        f = open("prueba.md", "w")
        f.write(key_value)
        f.close()


dict_md(cars)
