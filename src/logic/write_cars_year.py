import sys
sys.path.append(".")
from src.BBDD_access.BBDD_connect import *
from src.BBDD_access.BBDD_query_year import BBDD_query_year
from cars_year_md import cars_classics_md

cars_classics = BBDD_query_year(collection)
md_cars_classics = cars_classics_md(cars_classics)

def write_cars_year(md_cars_classics):
    f = open("hugo\Sites\carrenting\content\posts\year.md", "w")
    f.write(md_cars_classics)
    f.close()