import sys
sys.path.append(".") #Para poder debuguear sin tener que quitar el src.logic.
from src.BBDD_access.BBDD_query import BBDD_query

def dict_md(BBDD_query):
    try:
        assert len(BBDD_query) > 0
    except:
        print("Su base de datos está vacía")

    # cada clave hacerla bold y su valor ponerlo al lado en texto plano
    bold = "**"
    key_value = ""
    for car_id, car_info in BBDD_query.items():  # iterar el diccionario anidado
        for key in car_info:
            key_value += bold + key + bold + ': ' + str(car_info[key]) + "\n"
        key_value += "\n"
        # Añadimos los items al archivo md con la funcion open()
        print(key_value)
        f = open("prueba.md", "w")
        f.write(key_value)
        f.close()


dict_md(BBDD_query)
