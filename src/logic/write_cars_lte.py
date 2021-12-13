import sys
sys.path.append(".")
from src.BBDD_access.BBDD_connect import *
from src.BBDD_access.BBDD_query_lte import BBDD_query_lte
from cars_lte_md import cars_cheaper_md
from src.logic.check_file_md_created import check_file_exists


cars_cheaper = BBDD_query_lte(collection)
md_cars_cheaper = cars_cheaper_md(cars_cheaper)

file_path_posts = r"C:\Users\asorp\Documents\proyecto\PyDevops\PyDevops\hugo\Sites\carrenting\content\posts\precio.md"
file_path_content = r"C:\Users\asorp\Documents\proyecto\PyDevops\PyDevops\hugo\Sites\carrenting\content\precio.md"

def write_cars_lte_posts(md_cars_cheaper):
    f = open("hugo\Sites\carrenting\content\posts\precio.md", "w")
    f.write("Hola tu, aqui encontraras los coches mas baratos" + "<!--more-->" + md_cars_cheaper)
    f.close()
    if check_file_exists(file_path_posts):
        print('archivos md creados correctamente')
    else:
        print('No se han podido crear los archivos markdown')

def write_cars_lte_content(md_cars_cheaper):
    f = open("hugo\Sites\carrenting\content\precio.md", "w")
    f.write(md_cars_cheaper)
    f.close()
    if check_file_exists(file_path_content):
        print('archivos md creados correctamente')
    else:
        print('No se han podido crear los archivos markdown')