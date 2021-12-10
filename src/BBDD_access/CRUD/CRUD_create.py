import sys
sys.path.append(".")
from src.BBDD_access.BBDD_connect import *

value_model = input("Valor Model: ")

value_brand = input("Valor Brand: ")
value_brand = value_brand.lower()
if value_brand != ("renault" or "volkswagen" or "seat" or "ford" or "toyota" or "audi"):
    print("Introduzca una marca válida")
    print("Marcas válidas: renault, volkswagen, seat, ford, toyota y audi")
    exit()
    
value_category_name = input("Valor Categoria: ")
value_category_name = value_category_name.lower()
if value_category_name != ("common" or "classic" or "premium"):
    print("Introduzca una categoría válida")
    print("Categorías válidas: common, classic y premium")
    exit()

value_category_discounttax = input("Valor Tasa de descuento: ")
value_category_name = int(value_category_name)
if value_category_name != (20 or 40 or 60):
    print("introduzca uno de los siguientes números según su categoría")
    print("common: 60")
    print("classic: 40")
    print("premium: 20")
    exit()

value_passengers = input("Valor Passengers: ")
value_passengers = int(value_passengers)
if value_passengers > 10:
    print("Introduzca un número de pasajeros creíble. Inferior o igual a 10")
    exit()

value_year = input("Valor Year: ")
value_year = int(value_year)
if value_year < 1914:
    print("Introduzca un coche del 1914 en adelante")
    exit()

value_price = input("Valor Price: ")
value_price = int(value_price)

print("Si está disponible ponga True")
print("Si no lo está ponga False")
value_available = input("Valor Available: ")
if value_available == "True":
    value_available = True
if value_available == "False":
    value_available = False


my_dict = [{"model": value_model, 
"brand":value_brand, 
"category": {"name": value_category_name, "discountTax": value_category_discounttax},
"passengers": value_passengers,
"year": value_year,
"price": value_price,
"available": value_available}]

collection.insert_one(my_dict)
