import sys
sys.path.append(".")
from cars_all_md import *

def write_cars_all(key_value):
    f = open("hugo\Sites\carrenting\content\posts\main.md", "w")
    f.write(key_value)
    f.close()

write_cars_all(key_value)