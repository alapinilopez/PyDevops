import sys
sys.path.append(".")
from src.BBDD_access.BBDD_connect import *
from src.BBDD_access.BBDD_query_lte import BBDD_query_lte
from cars_lte_md import cars_cheaper_md

cars_cheaper = BBDD_query_lte(collection)
md_cars_cheaper = cars_cheaper_md(cars_cheaper)

def write_cars_lte(md_cars_cheaper):
    f = open("hugo\Sites\carrenting\content\posts\precio.md", "w")
    f.write(md_cars_cheaper)
    f.close()
