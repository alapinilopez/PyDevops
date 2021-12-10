import sys
sys.path.append(".")
from src.BBDD_access.BBDD_connect import *
from src.BBDD_access.BBDD_query_all import BBDD_query_all
from cars_all_md import cars_all_md

cars_all = BBDD_query_all(collection)
md_cars = cars_all_md(cars_all)

#con la función write creamos el markdown y lo completamos
def write_cars_all(md_cars):
    f = open("hugo\Sites\carrenting\content\posts\main.md", "w")
    f.write("Hola mundo, aqui encontraras todos los coches que tenemos en nuestra BBDD" + "<!--more-->" + md_cars)
    f.close()

def write_cars_all_2(md_cars):
    f = open("hugo\Sites\carrenting\content\main.md", "w")
    f.write(md_cars)
    f.close()