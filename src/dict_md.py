from typing import Dict
from BBDD_simulada import BBDD_simulada


def dict_md(BBDD_simulada):
    try:
        assert len(BBDD_simulada) > 0
    except:
        return "Su base de datos está vacía"

    # cada clave hacerla bold y su valor ponerlo al lado en texto plano
    bold = "**"
    key_value = ""
    for ship_id, ship_info in BBDD_simulada.items():  # iterar el diccionario anidado
        for key in ship_info:
            key_value += bold + key + bold + ': ' + str(ship_info[key]) + "\n"
        key_value += "\n"
        # Añadimos los items al archivo md con la funcion open()
        f = open("prueba.md", "w")
        f.write(key_value)
        f.close()


dict_md(BBDD_simulada)
