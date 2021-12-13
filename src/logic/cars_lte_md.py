# funcion que pase a md BBDD_query_lte.py #

def cars_cheaper_md(cars_cheaper):
    # cada clave hacerla bold y su valor ponerlo al lado en texto plano. Listarlo
    md_cars_cheaper = ""
    i = 1
    for document in cars_cheaper:
        md_cars_cheaper += "\n" + "### Item " + str(i) + "\n"
        i += 1
        for key in document:
            if key != 'category' and key != 'price':
                md_cars_cheaper += "* " + key + ': ' + str(document[key]) + "\n"
            elif key == 'category':
                md_cars_cheaper = category(key, document[key], md_cars_cheaper)
            elif key == 'price':
                md_cars_cheaper += "* " + "**" + key + ': ' + str(document[key]) + "**" + "\n"
            else:
                continue
    assert isinstance(md_cars_cheaper, str)
    return md_cars_cheaper

def category(key, value, md_cars_cheaper):
    md_cars_cheaper += '* ' + key + ':' + '\n'
    for aspect in value:
        md_cars_cheaper += '* * ' + aspect + ': ' + str(value[aspect]) + '\n'
    return md_cars_cheaper