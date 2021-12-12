import sys
sys.path.append(".")
from src.BBDD_access.BBDD_connect import *
from form import *


RANGE_NAME = 'Create!B:H' # Rango a solicitar de la hoja de calculo
values = main(RANGE_NAME)

# Le indicamos el valor que va a tener cada llave
value_model = values[0]
value_brand = values[1]
value_category_name = values[2]
if value_category_name == 'common':
    value_category_discounttax = 60
elif value_category_name == 'classic':
    value_category_discounttax = 40
else:
    value_category_discounttax = 20
value_passengers = int(values[3])
value_year = int(values[4])
value_price = int(values[5])
value_available = bool(values[6])
if values[6] == 'TRUE':
    value_available = True
else:
    value_available = False

document = {"model": value_model, 
"brand":value_brand, 
"category": {"name": value_category_name, "discountTax": value_category_discounttax},
"passengers": value_passengers,
"year": value_year,
"price": value_price,
"available": value_available}
# Insertamos el documento(en formato dict) con los valores correspondientes a la colección de la BBDD
collection.insert_one(document)
print('Coche insertado con éxito :D')
