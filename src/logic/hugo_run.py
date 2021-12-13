#funcion para realizar un comando
from os import system, chdir
import webbrowser



def hugo_run():
    check_hugo_installed() # Comprobamos que hugo esta instalado
    try:
        chdir("hugo/Sites/carrenting") # Le indicamos la ruta relativa donde se tiene que realizar el comando
    except:
        print('Situate en el directorio correcto') # si no esta en esa ruta, se lo indicamos
        exit()
    webbrowser.open_new_tab('http://localhost:1313/') # Abrimos la web en el navegador
    system("hugo server") # Comando para lanzar hugo

def check_hugo_installed():
    try:
        system("hugo version") # Comando que nos indica la verion de hugo y en caso de no estar instalado correctamente daría error
    except:
        print('Hugo no esta instalado correctamente')
        exit()
    else:
        return True
