# PyDevops

Proyecto de primero de DAW DUAL

## INTRODUCCIÓN

_Alessandro Lapini y Andreu Sorell, de 1º DAW DUAL_

¿En qué consiste nuestro proyecto? El documento "Repte PyDevops" compartido por David lo explica de manera clara:



> La empresa tiene una web que muestra una colección de items que están en stock. Actualmente, usan un wordpress donde añaden nueva información a mano. La información que aparece en la web está desactualizada porque nadie en la empresa ha estudiado tiene la capacidad de modificar estas antiguas plantillas.

El proyecto consiste en implementar un sistema de integración y entrega contínua empleando los siguientes metodos:

- Desarrollar una aplicación **Python** para extraer los datos de **MongoDB Atlas**. Diseñando así una especificación del esquema de los documentos **JSON**.
- Los documentos **JSON** se han de formatear a ficheros **Markdown** con una aplicación Python.
- Generar los ficheros MarkDown en la estructura de directorios que establece el generador de sitios estáticos **HUGO**, también mediante una aplicación Python.
- Customizar los estilos **CSS** que utiliza HUGO para darle a la web un estilo único.

De este modo, cada vez que se añada, actualice o elimine un item de la base de datos, solo tendremos que lanzar esta "aplicación" y la web se actualizará de manera autómatica con los modificaciones realizadas en la base de datos.

## METODOLOGÍA

¿Qué son las metodologías de **desarrollo de software**? Las metodologías de desarrollo de software son el conjunto de técnicas y métodos organizativos que se utilizan para diseñar una solución de software informático con el fin de optimizar los recursos a tu alcance.
Trabajar con una metodología es imprescindible por una cuestión de organización, ya que los factores tienen que estar ordenados y saber cómo se van a utilizar.

Para el desarrollo de esta aplicación la metodología utilizada ha sido **scrum**. ¿Por qué scrum? Porque este marco de desarrollo es heurístico. Se basa en el aprendizaje continuo y en la adaptación a los factores fluctuantes. Reconoce que el equipo no lo sabe todo al inicio de un proyecto y evolucionará a través de la experiencia. Scrum está estructurado para ayudar a los equipos a adaptarse de forma natural a las condiciones cambiantes y a los requisitos de los usuarios, con el cambio de prioridades integrado en el proceso y ciclos de lanzamiento breves para que tu equipo pueda aprender y mejorar constantemente.

Para que el marco de trabajo sea efectivo ha de tener los siguientes factores como núcleo:
- Comunicación
- Transparencia
- Mejora continua

Dentro del Scrum encontramos tres integrantes diferentes, o _“user role”_. Estos son: 
Scrum team: El Equipo Scrum consiste en un Dueño de Producto (Product Owner), el Equipo de Desarrollo (Development Team) y un Scrum Master. Los Equipos Scrum son autoorganizados y multifuncionales. Los equipos autoorganizados eligen la mejor forma de llevar a cabo su trabajo y no son dirigidos por personas externas al equipo. El modelo de equipo en Scrum está diseñado para optimizar la flexibilidad, la creatividad y la productividad.

Funcionalidades de los roles:
- _Product Owner_: El Dueño de Producto es el responsable de maximizar el valor del producto y del trabajo del Equipo de Desarrollo. El cómo se lleva a cabo esto podría variar ampliamente entre distintas organizaciones, Equipos Scrum e individuos. 
- _Development Team_: El Equipo de Desarrollo está formado por los profesionales que desempeñan el trabajo de entregar un incremento de producto “Terminado”, que potencialmente pueda ponerse en producción, al final de cada Sprint. Solo los miembros del Equipo de Desarrollo participan en la creación del incremento. 
- _Scrum Master_: El Scrum Master es el responsable de asegurar que Scrum es entendido y adoptado. Los Scrum Masters hacen esto asegurándose de que el Equipo Scrum trabaja ajustándose a la teoría, prácticas y reglas de Scrum. 

En este proyecto los roles han sido distribuidos de la siguiente manera:
- _Product Owner_: nuestro tutor David. Como Dueño de Producto (Product Owner) él ha sido el responsable de maximizar el valor del producto y del trabajo del Equipo de Desarrollo.
- _Development Team_: Andreu Sorell y Alessandro Lapini. 
- _Scrum Master_: no ha habido al tratarse de un proyecto desarrollado en parejas. Las sesiones consistían en un diálogo dinámico entre los compañeros del _Development Team_.

La **Lista de Producto** es una lista ordenada de todo lo que podría ser necesario en el producto, y es la única fuente de requisitos para cualquier cambio a realizarse en el producto. El Dueño de Producto (Product Owner) es el responsable de la Lista de Producto, incluyendo su contenido, disponibilidad y ordenación. En este caso el **backlog** lo hemos organizado el Development Team bajo la supervisación del Product Owner.

**Sprint** 
El sprint es el corazón del Scrum. El sprint es un bloque de tiempo el cual se crea un incremento de producto “Terminado”, utilizable y potencialmente desplegable. Es más conveniente si la duración de los Sprints es consistente a lo largo del esfuerzo de desarrollo, en nuestra caso un sprint duraba entre 3 días y una semana. Cada nuevo Sprint comienza inmediatamente después de la finalización del Sprint previo. En este proyecto los sprints se ideaban a partir de las **historias de usuario**.

## ANÁLISIS
Hemos analizado el proyecto mediante historias de usuario. Tras un período de análisis llegamos a la conclusión que el desarrollo de esta aplicación la llevaríamos a cabo en 5 historias de usuario, **5 épicas**:
1. Creación de la BBDD: El usuario quiere disponer de una BBDD, con una estructura especifica.
2. Consultar la BBDD: El usuario quiere que los elementos de la BBDD sean accesibles.
3. Programar en Python: El usuario quiere pasar la BBDD a un formato web.
4. Utilizar HUGO para convertir un archivo MarkDown a html: El usuario quiere crear la web con un generador estático de contenidos.
5. Darle estilo a la página web con CSS: El usuario quiere una página web de los elementos de la BBDD bonita.

Para este proyecto las tecnologías a utilizar ya nos fueron "asignadas", por así decirlo. Como ya he comentado anteriormente para la base de datos utilizamos **MongoDB Atlas**. El lenguaje de programación es **Python**. Y el generador estático de contenido es **Hugo**.

Otras tecnologías que podríamos haber usado si el proyecto fuera "libre" son:
- Bases de Datos: Apache Cassandra, MySQL y PostgreSQL entre otros.
- Lenguajes de Programación: java, C# y C++ entre otros.
- Generador de Sitios Estáticos: Jekyll, Pelican y Go entreo otros.

## DISEÑO

![Mapa Conceptual](/images/mapa_conceptual.png)

La arquitectura de la aplicación se basa en el uso de estas tres tecnologías: MongoDB Atlas, Python y Hugo. Cada una tiene las siguientes características:

- MongoDB Atlas: Database-as-a-Service (DBaaS) es un servicio que permite configurar, implementar y expandir una base de datos sin preocuparnos por el hardware físico local, las actualizaciones de software y los detalles de configuración para el rendimiento. Con DBaaS, un proveedor de nube hace todo esto y lo pone en funcionamiento de inmediato.
MongoDB Atlas es una base de datos en la nube que maneja toda la complejidad de implementar, administrar y reparar implementaciones.

- Python: Python es un lenguaje de programación de alto nivel que se utiliza para desarrollar aplicaciones de todo tipo. Este se trata de un lenguaje interpretado, es decir, que no es necesario compilarlo para ejecutar las aplicaciones escritas en Python, sino que se ejecutan directamente por el ordenador utilizando un programa denominado interpretador, por lo que no es necesario “traducirlo” a lenguaje máquina. Python es un lenguaje sencillo de leer y escribir debido a su alta similitud con el lenguaje humano. Además, se trata de un lenguaje multiplataforma de código abierto y, por lo tanto, gratuito, lo que permite desarrollar software sin límites.

- Hugo: Hugo es un moderno framework para creación de sitios web de propósito general. Se ubica en la categoría de los nuevos generadores de sitios estáticos,2​ basados en la arquitectura dinámica JAMstack y es escrito completamente en Go.

### **Estructura de directorios**
La estructura de directorios utilizada es la siguiente:
![Directorios](/images/directorios.png)

- PyDevops: carpeta raíz del proyecto.
- hugo: carpeta que contiene todos los componentes necesarios para ejecutar Hugo. La estructura de directorios interna a esta carpeta la genera Hugo **automáticamente**.
- imagenes: contiene las imágenes de este ***README.md***
- src: contiene toda la lógica programada en Python. Colocamos cada fichero Python en una carpeta diferente según su funcionalidad.
    - BBDD_access: lógica Python que conecta a la base de datos. También contiene una carpeta dentro.
        - CRUD: lógica Python que hace modificaciones a la base de datos por consola. También contiene una carpeta.
            - API: lógica Python que hace modificaciones a la base de datos mediante formularios de Google.
    - logic: contiene la lógica Python que convierte los items de la base de datos a formato MarkDown.
- test: carpeta que contiene todos los casos test ideados para comprobar la efectividad de nuestro código.

### **Arquitectura de la aplicación**

![Arquitectura Aplicación](/images/arquitectura_aplicacion.png)

La arquitectura de nuestra aplicación está dividia en tres capas.
- CAPA de DATOS: capa en la que consulta la base de datos y se accede a ella.
- CAPA de NEGOCIO: capa que incluye toda la lógica que hace funcionar al programa.
- CAPA de PRESENTACIÓN: capa en la que el usuario puede interactuar con la aplicación.
### **Diagrama de componentes**

![Diagrama Componentes](/images/diagrama_componentes.png)

Este diagrama de componentes representa las siguientes interacciones:
El componente **main** es el encargado de ejecutar el restode componentes y arrancar la aplicación. El componente main empieza llamando a los componentes: **write_cars_all**, **write_cars_lte** y **write_cars_year**. Estos tres para poder darle a **main** el valor que solicita han de llamar: **cars_all_md**, **cars_lte_md** y **cars_year_md**. 
A su vez, estos llaman a **BBDD_query_all**, **BBDD_query_lte** y **BBDD_query_year**. Todos estos dependen del componente **BBDD_connect**. Este componente lo que hace es conectarse a **MongoDB** y obtener la información de la colección que necesitan el resto de funciones.

Una vez realizado todo este proceso el componente **main** ejecuta el componente **hugo_run**, encargado de inicializar la página web y mostrarla en el navegador.
### **Esquema de la Base de Datos**
El esquema nos fue provisto por un compañero de 2º de DAW. Tanto el Equipo de Desarrollo como el compañero de segundo decidimos hacer una web sobre alquiler de coches. El esquema es el siguiente:
```json 
{
"model": "string",
"brand": "enumType<renault |    volkswagen | seat | ford | toyota | audi>",
"category": {
    "name": "string",
    "discountTax": "int"
},
"passengers": "int",
"year": "int",
"price": "int",
"available": "boolean"
}
```


- model: el valor de model será el modelo del vehículo.
- brand: marca del vehículo que tendrá que ser un Renault, Volkswagen, Seat, Ford, Toyota o Audi.
- category: esta tiene un diccionario como valor.
    - name: el vehículo insertado ha de pertenecer a una gama. Puede ser common, premium o classic
    - discounttax: según la gama se le aplicará una tasa u otra. Common: 60, premium: 20 y classic: 40.
- passengers: número de asientos que tiene el vehículo.
- year: fecha de fabricación del vehículo.
- price: precio (número real) del alquiler del vehículo por día.
- available: booleano que indica si el vehículo está disponible para ser alquilado.

## IMPLEMENTACIÓN

### **Herramientas utilizadas**
Las herramientas utilizadas han sido las siguientes:
- Visual Studio Code: Explicación de qué es de Wikipedia.
> Visual Studio Code es un editor de código fuente desarrollado por Microsoft para Windows, Linux, macOS y Web. Incluye soporte para la depuración, control integrado de Git, resaltado de sintaxis, finalización inteligente de código, fragmentos y refactorización de código. También es personalizable, por lo que los usuarios pueden cambiar el tema del editor, los atajos de teclado y las preferencias. Es gratuito y de código abierto, aunque la descarga oficial está bajo software privativo e incluye características personalizadas por Microsoft.

Hemos elegido programar en VSCode por los siguientes motivos:
1. El primer motivo es porque es gratuito.
2. Cómodo y fácil de utilizar
3. Infintas extensiones desarrollados tanto por la comunidad como por empresas.
4. Se puede utilizar para varios lenguajes de programación sin ningún tipo de dificultad.

- MongoDBCompass: aplicación oficial de MongoDB Atlas que sirve para acceder a nuestra base de datos y hacer modificaciones tanto por GUI como por consola.

- Clockify: Clockify es una aplicación simple de seguimiento del tiempo y planilla de horarios que les permite a ti y a tu equipo realizar el seguimiento de las horas trabajadas en los proyectos. Y es gratuito.

- GitHub: GitHub es un proveedor para alojar proyectos utilizando el sistema de control de versiones Git. Se utiliza principalmente para la creación de código fuente de programas de ordenador. Al realizar un proyecto en Git el equipo debe decidir que **GitFlow** seguir. **¿Qué es GitFlow?** En la web de Atlassian encontramos la siguiente definición:

> Gitflow es una especie de idea abstracta de un flujo de trabajo de Git. Esto quiere decir que ordena qué tipo de ramas se deben configurar y cómo fusionarlas. Explicaremos brevemente los objetivos de las ramas a continuación

En este proyecto hemos utilizado la extensión *Conventional Commits* para tener un GitFlow adecuado y sencillo de comprender para el equipo. La disposición de las ramas es la siguiente:

    - Rama main: rama predefinida al crearse el repositorio. Aquí añadimos lo que necesitábamos al principio.
    - Rama develop: rama principal para el desarrollo del proyecto. Siempre que desarollamos una nueva **feature** (característica) la fusionamos a esta rama.
    - Rama feature: las ramas feature las hemos ido creando por cada característica que desarrollábamos para el proyecto. Ejemplo: feature_hugo. Rama característica en la que se trabaja en hugo.
![Git Graph](/images/git_graph.png)



## **BackEnd**
Para el ejemplo de código de cómo funciona la aplicación usaremos un solo caso de uso. Simularemos que la función **main** de la aplicación solo corre ciertos módulos.

### ***Fichero main***
Es el encargado de llamar al resto de ficheros para hacer funcionar la aplicación. Termina ejecutando **Hugo** y abriendo la web en el navegador predefinido del sistema. 
```python
from write_cars_all import *
from write_cars_lte import *
from write_cars_year import *
from hugo_run import *


write_cars_all_posts(md_cars)
write_cars_all_content(md_cars)

write_cars_lte_posts(md_cars_cheaper)
write_cars_lte_content(md_cars_cheaper)

write_cars_year_posts(md_cars_classics)
write_cars_year_content(md_cars_classics)

hugo_run()
```
### ***Ejecución de Hugo***
Sirve para lanzar Hugo en el navegador predefinido de manera automática. Se ejecuta una vez se han generado los ficheros markDown con las consultas a la base de datos.
```python
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

```

### ***Módulo que escribe los items en un fichero***
Es el encargado de crear el directorio **posts** dentro de de la estructura de directorios de Hugo. Dentro de **posts** generamos el archivo markDown que incluye los items solicitados.
```python
import sys
sys.path.append(".")
from src.BBDD_access.BBDD_connect import *
from src.BBDD_access.BBDD_query_all import BBDD_query_all
from src.logic.cars_all_md import cars_all_md
from src.logic.check_file_md_created import check_file_exists

cars_all = BBDD_query_all(collection)
md_cars = cars_all_md(cars_all)

# Rutas absolutas a checkear
file_path_posts = r"hugo\Sites\carrenting\content\posts\main.md"
file_path_content = r"hugo\Sites\carrenting\content\main.md"

## Creamos el archivo MarkDown y lo escribimos con los documentos de la BBDD formateados ##
def write_cars_all_posts(md_cars):
    f = open("hugo\Sites\carrenting\content\posts\main.md", "w") # Ruta relativa
    f.write("Aqui encontrara todos los coches listados en la BBDD" + "<!--more-->" + md_cars)
    f.close()
    if check_file_exists(file_path_posts): # Comprobamos que se han crado los archivos
        print('archivos md creados correctamente')
    else:
        print('No se han podido crear los archivos MarkDown')

# Creamos dos archivos md con los mismo items de la BBDD, por el 'theme' que usamos en hugo 
def write_cars_all_content(md_cars):
    f = open("hugo\Sites\carrenting\content\main.md", "w")
    f.write(md_cars)
    f.close()
    if check_file_exists(file_path_content):
        print('archivos md creados correctamente')
    else:
        print('No se han podido crear los archivos MarkDown')
```
### ***Fichero que pasa los items a MD***
Es el encargado de generar una lista en markDown a partir de la colección que hemos solicitado mediante código.
```python
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
    return md_cars

def category(key, value, md_cars):
    md_cars += '* **' + key + ':' + '**' + '\n'
    for aspect in value:
        md_cars += '* * ' + aspect + ': ' + str(value[aspect]) + '\n'
    return md_cars
```
### ***Buscamos los documentos en la colección***
Este es el encargado de recoger los datos que nos interesan de la base de datos.
```python
import sys
sys.path.append(".")
from src.BBDD_access.BBDD_connect import *

def BBDD_query_all(collection):
    cars_all = []
    #buscamos todos los documentos de la coleccion y lo añadimos a un array
    for document in collection.find({}):
        cars_all.append(document)
    if len(cars_all) == 0:
        print('Su base de datos esta vacia')
    return cars_all
```
### ***Conexión a MongoDB***
Es el encargado de establecer la conexión a nuestra base de datos en **MongoDB**
```python
import pymongo
 
uri = 'mongodb+srv://****:****@cluster0.thpbm.mongodb.net/PyDevops?retryWrites=true&w=majority'
def connection(uri):
    global collection, db
    try:
        #Utilizamos una funcion de pymongo para conectarnos a la base de datos
        client = pymongo.MongoClient(uri)
        client.server_info() # Fuerza la conexion, si no se conecta pasa al except
        db = client.PyDevops
        collection = db.cars
    except:
        print("El servidor está caído o la uri es incorrecta")
        exit()
    else:
        return True
        
connection(uri)
```

## **Testing**

![Casos Test](/images/casos_test.png)

Hemos realizado diez casos test que comprueban la fiabilidad de nuestro código. Al trabajar hemos aplicado la TDD: Test-Driven Development (desarrollo dirigido por tests) es una práctica de programación que consiste en escribir primero las pruebas (generalmente unitarias), después escribir el código fuente que pase la prueba satisfactoriamente y, por último, refactorizar el código escrito. 

No siempre hemos hecho clean testing y hemos acabado recurriendo al dirty testing. Ya que a la hora de programar no siempre se nos ocurrían los casos test ideales para las funciones que estábamos programando.
### ***Test all cars***
Este caso test sirve para comprobar si los items de la BBDD se han pasado a MarkDown correctamente.
```python
from src.logic.cars_all_md import cars_all_md
from tests import *
import pytest


@pytest.mark.cars_all_md
def test_correcto():
    assert cars_all_md(doc_correct) == '\n### Item 1\n* **model**: clio\n* **brand**: renault\n* **category:**\n* * name: common\n* * discountTax: 60\n* **passengers**: 5\n* **year**: 2018\n* **price**: 20\n* **available**: True\n'

@pytest.mark.cars_all_md
def test_incorrecto1():
    assert not cars_all_md(doc_incorrect1) == '* **model**: clio\n* **brand**: renault\n* **passengers**: 5\n* **year**: 2018\n* **price**: 20\n* **available**: True\n\n'
```
### ***Comprueba instalación de Hugo***
Test que comprueba si Hugo está instalado en el ordenador.
```python
from src.logic.hugo_run import *
import pytest


@pytest.mark.hugo_installed
def test_correct_installation():
    assert check_hugo_installed() == True
```
### ***Test conexión a la BBDD***
El test de la conexión a la BBDD al asignarle una uri inválida.
```python
from src.BBDD_access.BBDD_connect import *
import pytest

uri = 'mongodb+srv://admin:admin@cluster0.thpbm.mongodb.net/PyDevops?retryWrites=true&w=majority'
uri_incorrect = 'mongodb+srv://admin:incorrectpassword@cluster0.thpbm.mongodb.net/PyDevops?retryWrites=true&w=majority'

@pytest.mark.BBDD_connect
def test_correct_uri():
    assert connection(uri) == True

# Esta función es solo para checkear que, si la uri es incorrecta, no se conecta a la BBDD.
# Es solo para el caso test, no se enviará a producción, ya que si no se conecta queremos que pare el programa (exit)
# Y con el return solo para esa función
def invalid_uri(uri): 
    try:
        client = pymongo.MongoClient(uri)
        client.server_info()
    except:
        return False

@pytest.mark.BBDD_connect
def test_incorrect_uri():
    assert invalid_uri(uri_incorrect) == False
```

![Tox](/images/tox2.png) 

Estos son los requisitos que necesitamos tener instalados para que la aplicación funcione:
![Requirements](/images/requirements.png)

### **FrontEnd**
![Web](/images/web_portada.png)

El FrontEnd de la web es generado automáticamente por Hugo. Para poder utilizar Hugo debemos hacer lo siguiente:

1. Utilizar la consola **Bash** si somos usuarios de Windows. Powershell o cmd puede causar problemas.
2. Instalar Hugo Extended en nuestra máquina https://github.com/gohugoio/hugo/releases. ¿Por qué la versión extended y no la estándard? Porque con la extended podremos utilizar cualquier tipo de plantilla.
3. Uno vez hayamos instalado Hugo, la instalación varía según el sistema operativo en el que trabajemos, vamos a la carpeta Sites y empezamos a introducir los siguientes comandos:
    - ``hugo new site carrenting`` genera toda la estructura de directorios necesaria para nuestra web.
    - ``cd carrenting`` nos posicionamos en la nueva carpeta. Manualmente nos descargamos el template que más nos guste de https://themes.gohugo.io/ y lo extraemos en el directorio *"themes"*
    - en el archivo config.toml escribimos el nombre del tema que nos hemos descargado ``theme = "ananke"``.
    - Le añadimos contenido MarkDown a la web siguiendo la estrectura que nos mande el tema en su documentación oficial. Si el tema no tiene documentación no es un buen tema. En nuestro caso la distribución es la siguiente: carpeta principal que incluye:
        - **_index.md**: página principal
        - **main.md**: copia de main.md de posts. Sirve para que funcione el botón del nav.
        - **precio.md**: copia de precio.md de posts. Sirve para que funcione el botón del nav.
        - **year.md**: copia de year.md de posts. Sirve para que funcione el botón del nav.
            - Carpeta posts:
                - **main.md**: consulta de todos los items.
                - **precio.md**: consulta de los items inferiores o igual a x precio.
                - **year.md**: consulta de los items anteriores a x año.
        - **formularios.md**: página que incluye los formularios que modifican la base de datos.
    - Ejecutamos el comando ``hugo server`` para inicializar la web.    
    ![Hugo directorios](/images/hugo_directorios.png)

Hemos modificado el template original para adaptarlo a nuestras necesidades. Las modificaciones del CSS las hemos hecho desde el fichero **config.toml**.

Con las siguientes "instrucciones" le hemos añadido un nav a la web.

```
[menu]
[[menu.main]]
  identifier = 'barato'
  name = 'Coches Baratos'
  title = 'blog section'
  url = '/precio/'
  weight = 15
  [[menu.main]]
  identifier = 'año'
  name = 'Coches Clásicos'
  font_colot = 'red'
  title = 'blog section'
  url = '/year/'
  weight = 10
  [[menu.main]]
  identifier = 'todos'
  name = 'Nuestros Coches'
  title = 'blog section'
  url = '/main/'
  weight = -10
  [[menu.main]]
  identifier = 'CRUD'
  name = 'Formularios CRUD'
  title = 'blog section'
  url = '/formularios/'
  weight = 20
```
Con esta instrucción modificamos el color al nav para que sea adecuado al estilo de la página web.

```
[params]
  background_color_class = "bg-orange"
  featured_image = "images/header.jpeg"
```
Y también añadimos esto para que se visualizasen bien todo tipo de caracteres.

```
  [markup]
  [markup.goldmark]
    [markup.goldmark.extensions]
      definitionList = true
      footnote = true
      linkify = true
      strikethrough = true
      table = true
      taskList = true
      typographer = true
    [markup.goldmark.parser]
      autoHeadingID = true
      autoHeadingIDType = 'github'
      [markup.goldmark.parser.attribute]
        block = false
        title = true
    [markup.goldmark.renderer]
      hardWraps = false
      unsafe = true
      xhtml = false
      
  [markup.asciidocExt]
    backend = 'html5'
    extensions = []
    failureLevel = 'fatal'
    noHeaderOrFooter = true
    preserveTOC = false
    safeMode = 'unsafe'
    sectionNumbers = false
    trace = false
    verbose = false
    workingFolderCurrent = false
    [markup.asciidocExt.attributes]
```
## Comparación Temporal

![Tiempo](/images/tiempo.png)
En este proyecto las estimaciones de tiempo las hemos realizado mediante tokens. Donde un token es equivalente a quince minutos de trabajo.

Estimación inicial para cada épica y sus subtareas:

1. El usuario quiere disponer de una BBDD con una estructura específica.
- Estimación: 2 token
- Usado: 1 token
- Hemos tardado menos de lo esperado porque hemos usado la función "insertMany", que añade directamente todos los datos que el usuario desea en la estructura acordada anteriormente.

2. El usuario quiere que los elementos de la BBDD sean accesibles.
    - TAREA 2.1
Tendremos que descargar la BBDD
        - Estimación: 12 tokens
Tiempo usado: 17 tokens
Hemos tardado más de lo estimado porqué cuando queríamos acceder a la BBDD desde Python nos daba 'timeoutError'. Al final, después de investigar cual era el error (dirección IP errónea), nos pudimos conectar perfectamente y pudimos importar los documentos de la BBDD.
    - TAREA 2.2
Tendremos que pasar la BBDD a la función que la convierte en MarkDown.
        - Estimación: 1 token
        Tiempo usado: 3 tokens
Hemos tardado más porqué hemos tenido que cambiar un poco la función que habíamos creado anteriormente (dict_md()), ya que lo que le pasábamos como input era una BBDD simulada. Y esta, no tenia exactamente el mismo formato que la BBDD original cuando la importamos.
    - TAREA 2.3
El usuario quiere acceder a documentos concretos de la BBDD.
        - Estimación: 8 tokens
    Tiempo usado: 9 tokens
3. El usuario quiere pasar la BBDD a formato web.
    - TAREA 3.1
    Necesitamos crear el entorno de trabajo para poder programar las necesidades del usuario
        - Estimación inicial: 1 token
        - Estimación real: 3 token
        - Hemos tardado un poco más de lo previsto porque hemos tenido que hacer la búsqueda de los archivos y carpetas necesarias para trabajar.
    - TAREA 3.2
    Necesitamos emularle al programa una BBDD para trabajar sin necesidad de la BBDD definitiva.
        - Estimación inicial: 2 tokens.
        - Estimación real: 1 token
    - TAREA 3.3
    Necesitamos pasar la BBDD a un archivo .md
        - Estimación: 16 tokens
        - Tiempo usado: 19 tokens.
        - Nos hemos demorado ya que hemos tenido que informarnos sobre como iterar diccionarios anidados.
    - TAREA 3.4
    Poder abrir y escribir los ficheros md mediante programación
        - Estimación: 8 tokens
        - Tiempo usado: 6 tokens
    - TAREA 3.5
    Crear una única función que realice todas las otras funciones y nos enseñe la página web.
        - Estimación: 4 tokens
        - Tiempo usado: 12 tokens
        - Se ha complicado más de lo esperado, porqué  cuando creábamos la función solo funcionaba para un único archivo MarkDown. Al final hemos modificado un poco las anteriores y simplemente llamando a las otras funciones desde un mismo archivo, donde, además, tenemos un función que lanza Hugo, ha funcionado.
4. El usuario quiere crear la web con un generador estático de contenidos.
    - TAREA 4.1
    Tenemos que instalar Hugo.
        - Estimación: 3 tokens
        - Tiempo usado: 3 tokens
        - Hemos seguido el tutorial y la única complicación que hemos tenido es que desde la consola de Windows nos daba error.
    - TAREA 4.2
    Tenemos que aprender a utilizar Hugo
        - Estimación: 6 tokens
        - Tiempo usado: 21 tokens
        - Nos alejamos bastante de lo estimado porqué para aprender a utilizar Hugo de manera correcta, no solo nos hemos documentado, sino que también hemos estado practicando.
    - TAREA 4.3
    Generar una página web mediante Hugo, a partir de un archivo MarkDown
        - Estimación: 4 tokens
        - Tiempo usado: 4 tokens
5. El usuario quiere una página web que contenga los elementos de la BBDD.
    - Tarea 5.1
    Modificar el template para darle un estilo único
        - Estimación: 12 token
        - Real: 14 token
        - Nos hemos demorado ya que no entendíamos muy bien cómo modificar el CSS

## Problemas y Mejoras
### Problemas
Hugo no nos ha terminado pareciendo del todo intuitivo a la hora de modificar el HTML y CSS. Nos gustaría probar a hacer el proyecto con una web hecha por nosotros en HTML.
### Mejoras
+ Añadir una GUI
+ Automatizar CRUD desde la web o desde la GUI. Cuando le des al submit del formulario, que haga CRUD sin que tengas que ejecutar manualmente el script de python.
+ Refactorizar los nombres de las variables.
+ Automatizar la actualización de la web por cada modificación en la BBDD.
