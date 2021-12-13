import sys
sys.path.append(".")
from src.BBDD_access.BBDD_connect import *
from src.BBDD_access.BBDD_query_year import BBDD_query_year
from cars_year_md import cars_classics_md
from src.logic.check_file_md_created import check_file_exists


cars_classics = BBDD_query_year(collection)
md_cars_classics = cars_classics_md(cars_classics)

file_path_posts = r"C:\Users\asorp\Documents\proyecto\PyDevops\PyDevops\hugo\Sites\carrenting\content\posts\year.md"
file_path_content = r"C:\Users\asorp\Documents\proyecto\PyDevops\PyDevops\hugo\Sites\carrenting\content\year.md"

def write_cars_year_posts(md_cars_classics):
    f = open("hugo\Sites\carrenting\content\posts\year.md", "w")
    f.write("Hola de nuevo, aqui estan los clasicos" + "<!--more-->" + md_cars_classics)
    f.close()
    if check_file_exists(file_path_posts):
        print('archivos md creados correctamente')
    else:
        print('No se han podido crear los archivos markdown')

def write_cars_year_content(md_cars_classics):
    f = open("hugo\Sites\carrenting\content\year.md", "w")
    f.write(md_cars_classics)
    f.close()
    if check_file_exists(file_path_content):
        print('archivos md creados correctamente')
    else:
        print('No se han podido crear los archivos markdown')