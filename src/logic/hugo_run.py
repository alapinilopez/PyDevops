#funcion para realizar un comando
from os import system, chdir
import webbrowser



def hugo_run():
    try:
        chdir("hugo/Sites/carrenting") #Le indicamos la ruta relativa donde se tiene que realizar el comando
    except:
        print('Situate en el directorio correcto') #si no esta en esa ruta, se lo indicamos
        exit()
    webbrowser.open_new_tab('http://localhost:1313/') #Abrimos la web en el navegador
    system("hugo server") #comando para lanzar hugo
