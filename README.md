# PyDevops

Proyecto de primero de DAW DUAL

## INTRODUCCIÓN

_Alessandro Lapini y Andreu Sorell, de 1º DAW DUAL_

¿En qué consiste nuestro proyecto? El documento "Repte PyDevops" compartido por David lo explica de manera clara:

> La empresa tiene una web que muestra una colección de items que están en stock. Actualmente, usan un wordpress donde han de picar la info a mano. La información que aparece en la web está desactualizada porque ninguno de los programadores/as de la empresa quiere meterse en ese infierno, que no han estado estudiando Basic, Pascal y Fortran en los años 90 para acabar editando plantillas.

Nuestro trabajo es el de implementar un sistema de integración y entrega contínua empleando los siguientes metodos:

- Desarrollar una aplicación **Python** para extraer los datos de **MongoAtlas**. Diseñando así unas especificación del esquema de los documentos **JSON**.
- Los documentos **JSON** tendremos que formatearlos a ficheros **Markdown** con una aplicación desarrollado por nosotros en Python.
- Situar los ficheros MarkDown en la estructura de directorios que establece el generador de sitios estáticos **HUGO**, también mediante una aplicación Python que vamos a desarrollar.
- Customizar los estilos **CSS** que utiliza HUGO para darle a la web la presentación adecuada.

De este modo, cada vez que se añada, actualice o elimine un item de la base de datos, solo tendremos que lanzar esta "aplicación" y la web se actualizará de manera autómatica con los modificaciones realizadas en la base de datos.

## BACKLOG
Hemos dividido el proyecto en 5 tareas principales:
1. Creación de la BBDD
El usuario quiere disponer de una BBDD, con una estructura especifica.
2. Descargar la BBDD
El usuario quiere que los elementos de la BBDD sean accesibles.
3. Programar en Python
El usuario quiere pasar la BBDD a un formato web.
4. Utilizar HUGO para convertir un archivo markdown a html
El usuario quiere crear la web con un generador estático de contenidos.
5. Darle estilo a la página web con CSS
El usuario quiere una página web de los elementos de la BBDD bonita.

### Tarea 3
Hemos dividido la tarea 3 en tres subtareas:
+ Primero, hemos creado el entorno de trabajo con las carpetas y archivos necesarios para para poder empezar a programar.
+ Luego, hemos creado una base de datos simulada, no real, porque hemos preferido darle prioridad a tener un programa que funcione con cualquier BBDD y luego ya crearemos la BBDD real.
+ Finalmente, hemos creado una función que coge la BBDD simulada y la convierte y la añade en un archivo markdown. También hemos creado un caso test para comprobar que la base de datos no este vacia.


Comprobar la versión de Hugo desde powershell puede dar error. Mejor ejecutar comandos desde el cmd
