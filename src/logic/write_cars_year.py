import sys
sys.path.append(".")
from cars_year_md import *

def write_cars_year(key_value):
    f = open("hugo\Sites\carrenting\content\posts\year.md", "w")
    f.write(key_value)
    f.close()