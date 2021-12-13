import sys
sys.path.append(".")
from src.BBDD_access.BBDD_connect import *
from src.BBDD_access.BBDD_query_all import BBDD_query_all
from src.logic.cars_all_md import cars_all_md
from src.logic.check_file_md_created import check_file_exists

cars_all = BBDD_query_all(collection)
md_cars = cars_all_md(cars_all)

# Rutas absolutas a checkear
file_path_posts = r"hugo\Sites\carrenting\content\posts\main.md"
file_path_content = r"hugo\Sites\carrenting\content\main.md"

## Creamos el archivo markdown y lo escribimos con los documentos de la BBDD formateados ##
def write_cars_all_posts(md_cars):
    f = open("hugo\Sites\carrenting\content\posts\main.md", "w") # Ruta relativa
    f.write("Aqui encontrara todos los coches listados en la BBDD" + "<!--more-->" + md_cars)
    f.close()
    if check_file_exists(file_path_posts): # Comprobamos que se han crado los archivos
        print('archivos md creados correctamente')
    else:
        print('No se han podido crear los archivos markdown')

# Creamos dos archivos md con los mismo items de la BBDD, por el 'theme' que usamos en hugo 
def write_cars_all_content(md_cars):
    f = open("hugo\Sites\carrenting\content\main.md", "w")
    f.write(md_cars)
    f.close()
    if check_file_exists(file_path_content):
        print('archivos md creados correctamente')
    else:
        print('No se han podido crear los archivos markdown')



