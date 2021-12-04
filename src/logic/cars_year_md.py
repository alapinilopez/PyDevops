import sys
sys.path.append(".")  # Para poder debuguear sin tener que quitar el src.logic.
from src.BBDD_access.BBDD_connect import *
from src.BBDD_access.BBDD_query_year import BBDD_query_year


cars_year = BBDD_query_year(collection)

def cars_year_md(cars_year):
    try:
        assert len(cars_year) > 0
        print("Base de datos OK")
    except:
        print("Su base de datos está vacía")

    # cada clave hacerla bold y su valor ponerlo al lado en texto plano. Listarlo
    key_value = ""
    for document in cars_year:
        # for car_id, car_info in document:  # iterar el diccionario anidado
        for key in document:
            if key != "_id" and key != "category":
                key_value += "* " + "**" + key + "**" + ': ' + str(document[key]) + "\n"
            else:
                continue
        key_value += "\n"
    
    f = open("hugo\Sites\carrenting\content\posts\year.md", "w")
    f.write(key_value)
    f.close()

cars_year_md(cars_year)