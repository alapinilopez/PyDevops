from typing import Dict
from BBDD_simulada import BBDD_simulada


def dict_a_tabla(BBDD_simulada):
    try:
        assert len(BBDD_simulada) > 0
    except:
        return "Su base de datos está vacía"
    # cada clave hacerla bold y su valor ponerlo al lado en texto plano

    keys = ""
    values = ""
    for key in BBDD_simulada.keys():
        keys += "### " + key + "\n"
    return keys


#  textfile = open("prueba.md", "a")
#  textfile.write(keys)
#  usar esto para escribir en md

#  for value in list(BBDD_simulada.values()):
#      values += "**" + str(value) + "**" + "\n"
# print(values)


dict_a_tabla(BBDD_simulada)
