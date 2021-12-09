import sys
sys.path.append(".")
from src.BBDD_access.BBDD_connect import *
from src.BBDD_access.BBDD_query_all import BBDD_query_all
from cars_all_md import cars_all_md

cars_all = BBDD_query_all(collection)
md_cars = cars_all_md(cars_all)

def write_cars_all(md_cars):
    f = open("hugo\Sites\carrenting\content\posts\main.md", "w")
    f.write(md_cars)
    f.close()
