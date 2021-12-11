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

![scrum](/images/scrum.png)

## ANÁLISIS
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

### Esquema de la Base de Datos
El esquema nos fue provisto por un compañero de 2º de DAW. Tanto el Equipo de Desarrollo como el compañero de segundo decidimos hacer una web sobre alquiler de coches. El esquema es el siguiente:

![Esquema BBDD](/images/esquema_bbdd.png)

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

![Arquitectura Aplicación](/images/arquitectura_aplicacion.png)

![Diagrama Componentes](/images/diagrama_componentes.png)

## BACKLOG
Hemos dividido el proyecto en 5 tareas principales:
1. Creación de la BBDD: El usuario quiere disponer de una BBDD, con una estructura especifica.
2. Consultar la BBDD: El usuario quiere que los elementos de la BBDD sean accesibles.
3. Programar en Python: El usuario quiere pasar la BBDD a un formato web.
4. Utilizar HUGO para convertir un archivo markdown a html: El usuario quiere crear la web con un generador estático de contenidos.
5. Darle estilo a la página web con CSS: El usuario quiere una página web de los elementos de la BBDD bonita.

### Tarea 3
Hemos dividido la tarea 3 en tres subtareas:
+ Primero, hemos creado el entorno de trabajo con las carpetas y archivos necesarios para poder empezar a programar. Y después hemos creado el entorno virtual y hemos instalado las herremientas necesarias para comprobar que nuestro programa funciona.
+ Luego, hemos creado una base de datos simulada, no real, porque hemos preferido darle prioridad a tener un programa que funcione con cualquier BBDD y luego ya crearemos la BBDD real.
+ Finalmente, hemos creado una función que coge la BBDD simulada y la convierte y la añade en un archivo markdown. También hemos creado un caso test para comprobar que la base de datos no este vacia.

### INICIALIZAR WEB CON HUGO
Para inicializar nuestra página web tendremos que utilizar comandos en la consola de **Git Bash** para así evitar tener errores que nos pueden surgir con la consola de Windows. 
Nota: debemos descargar HUGO Extended para poder utilizar todo tipo de CSS en nuestra web. https://github.com/gohugoio/hugo/releases
Lo que debemos hacer es navegar al directorio en el que tengamos HUGO\Sites y hacer el siguiente comando:
``$ hugo new site quickstart``


Comprobar la versión de Hugo desde powershell puede dar error. Mejor ejecutar comandos desde el cmd
