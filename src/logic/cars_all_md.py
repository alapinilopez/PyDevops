# funcion que pase a md el resultado de BBDD_query_all.py #

def cars_all_md(cars):
    # cada clave hacerla bold y su valor ponerlo al lado en texto plano. Listarlo
    md_cars = ""
    i = 1
    for document in cars:
        md_cars += "\n" + "### Item " + str(i) + "\n"
        i += 1
        for key in document:
            if key != 'category':
                md_cars += "* " + "**" + key + "**" + ': ' + str(document[key]) + "\n"
            elif key == 'category':
                md_cars = category(key, document[key], md_cars)
            else:
                continue
    assert isinstance(md_cars, str)
    return md_cars

def category(key, value, md_cars):
    md_cars += '* **' + key + ':' + '**' + '\n'
    for aspect in value:
        md_cars += '* * ' + aspect + ': ' + str(value[aspect]) + '\n'
    return md_cars
