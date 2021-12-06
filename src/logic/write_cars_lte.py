import sys
sys.path.append(".")
from cars_lte_md import *

def write_cars_lte(key_value):
    f = open("hugo\Sites\carrenting\content\posts\precio.md", "w")
    f.write(key_value)
    f.close()