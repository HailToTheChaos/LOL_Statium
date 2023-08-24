LOL Statium
===
Tu fuente de estadísticas de League Of Legends
## Información
- Titulo:  `LOL STATIUM`
- Autor:  `Jaime de la Fuente`

## Dependencias
- python
- pandas
- panel
- tqdm
- matplotlib
- numpy

## Uso
- Para obtener datos y guardarlos en la base de datos
  ```
  python .\Model\main.py
  ```
- Para iniciar la página
  ```
  python -m http.server
  ```

## Directorio
```
|—— Controller
|    |—— Index.js
|—— Docs
|—— Model
|    |—— db.py
|    |—— Download
|    |—— main.py
|    |—— MatchHistory.py
|    |—— Metadata.py
|    |—— PicksBans.py
|    |—— Positions.py
|    |—— Web_scrap.py
|—— Tests
|    |—— Tests.py
|—— View
|    |—— 404.html
|    |—— heatmap.html
|    |—— Img
|        |—— comp.gif
|        |—— heatmap.png
|        |—— index_image.png
|        |—— metrics.png
|        |—— picksBans.png
|        |—— summoners-rift.jpg
|    |—— index.html
|    |—— login.html
|    |—— matchHistory.html
|    |—— metrics.html
|    |—— Picksbans.html
|    |—— Styles
|        |—— login.css
|        |—— style.css
|        |—— style_index.css
```

# 1	RESUMEN
Este proyecto consiste en crear una página web que muestra información y gráficos sobre un videojuego llamado League of Legends, que se juega de forma competitiva en diferentes ligas.
El proyecto se centra en la liga LEC, que es una de las más importantes a nivel europeo. 
Para obtener la información, se usa una técnica que se llama Web Scraping, que sirve para extraer datos de otras páginas web. En este caso, se extraen los datos de una página llamada lol.fandom.com, que los presenta en un formato fácil de usar. 
Los datos se transforman en un marco de datos para poder manejarlos y guardarlos en una base de datos. Tras su guardado, los datos se usan para crear una página web con Python, un lenguaje de programación muy popular. 
 
En la página web se muestran diferentes tipos de gráficos que ayudan a entender mejor el videojuego: mapas que indican dónde ocurren las acciones más importantes, barras que muestran los personajes más usados, tablas que comparan el rendimiento de los jugadores, etc. Estos gráficos se hacen con unas herramientas que se llaman Matplotlib y Panel.

This project consists of creating a web page that shows information and graphics about a video game called League of Legends, which is played competitively in different leagues. 
The project focuses on the LEC league, which is one of the most important in Europe.
To obtain the information, a technique called Web Scraping is used, which serves to extract data from other web pages. In this case, the data is extracted from a page called lol.fandom.com, which presents them in an easy-to-use format. 
The data is transformed into a data frame so that it can be handled and stored in a database. After saving, the data is used to create a web page with Python, a very popular programming language. 
On the web page, different types of graphs are shown that help to better understand the video game: maps that indicate where the most important actions occur, bars that show the most used characters, tables that compare the performance of the players, etc. These graphs are made with some tools called Matplotlib and Panel.

 
 
# 2	INTRODUCCIÓN
League of Legends es un videojuego de género MOBA (Multiplayer Online Battle Arena) que se ha convertido en uno de los más populares y exitosos del mundo. Cuenta con millones de jugadores que compiten entre sí en partidas online, tanto de forma amateur como profesional.
El objetivo principal del League of Legends (también reconocido por sus siglas LOL), es destruir la base del equipo contrario mientras se defiende la propia. Para lograrlo, los jugadores se agrupan en equipos de cinco personas y se enfrentan en una partida. Cada jugador controla a un campeón con habilidades únicas y diferentes roles dentro del equipo.
 
A medida que la partida avanza, los campeones ganan experiencia y obtienen oro para adquirir objetos que mejoran sus habilidades y atributos. Además, durante la partida aparecen objetivos especiales, como el dragón y el barón Nashor, que otorgan ventajas estratégicas al equipo que los capture.
 
El mapa del juego está dividido en tres carriles o líneas: superior, central e inferior, y una jungla entre ellos. Los jugadores deben navegar por el mapa, enfrentarse a los campeones enemigos, eliminar monstruos neutrales y destruir torres defensivas para avanzar hacia la base enemiga.
 
Es un juego que combina estrategia, habilidad individual y trabajo en equipo, y requiere de coordinación, toma de decisiones rápidas y dominio de las mecánicas de juego para tener éxito. Con su amplia variedad de campeones, estrategias y modos de juego.
El juego tiene una escena competitiva muy desarrollada, con diferentes ligas regionales que se disputan a lo largo del año y que culminan en un campeonato mundial. Una de estas ligas es la LEC (League of Legends European Championship), que reúne a los mejores equipos y jugadores de Europa.

 
Según un artículo de la revista AS, la final de Worlds  del 2021 tuvo un pico de 73 millones de espectadores. Esto quiere decir que la escena competitiva de este videojuego es bastante amplia y sólida.
El análisis de datos y la visualización de información son herramientas muy útiles para comprender mejor el funcionamiento y el rendimiento de un videojuego como League of Legends. A través de ellas, se pueden obtener perspectivas sobre las estrategias, las preferencias, las fortalezas y las debilidades de los equipos y los jugadores que participan en la liga LEC. Además, se pueden generar gráficos atractivos e interactivos que faciliten la comunicación y la difusión de los resultados.
El objetivo de este proyecto es crear una página web que genere estadísticas y gráficos sobre el videojuego League of Legends a nivel competitivo, enfocándose en la liga LEC.
 
# 3	OBJETIVOS Y JUSTIFICACIÓN DEL PROYECTO
El videojuego League of Legends es un fenómeno global que genera un gran interés tanto entre los aficionados como entre los profesionales. Su complejidad y dinamismo hacen que sea un campo muy rico para el análisis de datos y la visualización de información. Sin embargo, no son tantas las páginas web que ofrecen esto.
El propósito de este proyecto es crear una página web que llene este vacío y que permita a los usuarios acceder a información relevante y atractiva sobre el videojuego League of Legends y la liga LEC. Los objetivos específicos del proyecto son los siguientes:
•	Obtener datos de partidas, equipos y jugadores de la liga LEC a través de un método llamado Web Scraping, que consiste en extraer datos de otras páginas web, en este caso lol.fandom.com, que los presenta en un formato fácil de usar.
•	Los datos obtenidos se transforman en un marco de datos (Data Frame), para poder moldear los datos para su fácil guardado en una base de datos.
•	Almacenar los datos en una base de datos SQL, que permita gestionarlos de forma eficiente y segura.
•	Generar un HTML que utilice PyScript, un framework que interconecta Python en un Script HTML, siendo Python un lenguaje de programación muy popular y versátil.
•	Generar estadísticas y gráficos sobre el videojuego League of Legends y la liga LEC, utilizando las librerías de Python MatPlotLib y Panel. Estas estadísticas y gráficos incluirán: mapas de calor con las muertes, asesinatos y colocación de Wards, gráfica de barras horizontales para mostrar los campeones más elegidos, tablas mostrando estadísticas de jugadores, etc.
•	Mostrar las estadísticas y gráficos en la página web de forma interactiva y atractiva, permitiendo al usuario filtrar por diferentes criterios y explorar los datos.
La justificación del proyecto se basa en las siguientes razones:
•	El videojuego League of Legends es un tema de gran interés y actualidad, que cuenta con una gran comunidad de seguidores y aficionados.
•	La liga LEC es una de las más importantes y prestigiosas del mundo, que reúne a los mejores equipos y jugadores de Europa.
•	El análisis de datos y la visualización de información son herramientas muy útiles para comprender mejor el funcionamiento y el rendimiento de un videojuego como League of Legends. A través de ellas, se pueden obtener perspectivas sobre las estrategias, las preferencias, las fortalezas y las debilidades de los equipos y los jugadores que participan en la liga LEC.
•	El proyecto supone un reto formativo y tecnológico, ya que me permite desarrollar competencias en áreas como la programación, la gestión de bases de datos, el web Scraping, el análisis de datos y la visualización de información.
•	También supone un reto incorporar PyScript, una tecnología en fase de desarrollo temprana. Esto supone hacer un esfuerzo para comprender y analizar la documentación oficial de esta herramienta. A su vez, sirve para simplificar este proyecto en un solo lenguaje de programación.
Las posibles soluciones para crear una página web que genere estadísticas y gráficos sobre el videojuego League of Legends son las siguientes:
•	Usar una API (Application Programming Interface) oficial o de terceros que proporcione los datos del juego y de la liga. Una API es un conjunto de reglas y protocolos que permite comunicarse con una aplicación o servicio web. Algunas ventajas de usar una API son: la facilidad de acceso a los datos, la fiabilidad y seguridad de los mismos, la actualización constante y la compatibilidad con diferentes plataformas. Algunas desventajas son: la dependencia de la disponibilidad y el funcionamiento de la API, las posibles limitaciones o restricciones en el uso de los datos, la falta de personalización o flexibilidad en el formato o contenido de los datos.
•	Usar un método llamado Web Scraping, que consiste en obtener datos de páginas web mediante programas o scripts que analizan el código HTML o XML de las mismas. Algunas ventajas de usar Web Scraping son: la posibilidad de acceder a datos que no están disponibles mediante una API, la libertad y flexibilidad para elegir el formato o contenido de los datos, la personalización y adaptación a las necesidades del proyecto. Algunas desventajas son: la dificultad técnica para extraer los datos, la vulnerabilidad a los cambios o modificaciones en las páginas web, los posibles problemas legales o éticos al usar datos sin permiso o consentimiento.
La solución elegida para este proyecto es usar Web Scraping, por las siguientes razones:
•	La página web lol.fandom.com ofrece una gran cantidad y variedad de datos sobre el videojuego League of Legends, que actualmente no están disponibles mediante una API oficial.
•	La página web lol.fandom.com presenta los datos en formato JSON (JavaScript Object Notation), que es un formato ligero y fácil de usar para intercambiar datos. Esto facilita el proceso de obtener y guardar los datos para su posterior procesamiento.
•	El uso de Web Scraping permite personalizar y adaptar los datos a las necesidades del proyecto

 
# 4	ANÁLISIS DE REQUERIMIENTOS
A continuación, se presentan los requerimientos funcionales y no funcionales para el proyecto de crear una página web sobre estadísticas del videojuego League of Legends a nivel competitivo:
4.1	Requerimientos funcionales
1.	Obtener datos de partidas, equipos y jugadores de la liga LEC a través de Web Scraping desde la página lol.fandom.com. Con la librería Requests se obtienen los datos, con BeautifulSoup se obtiene la consulta en formato HTML, se recoge el JSON y posteriormente se obtienen los datos y se guardan en un DataFrame de la librería Pandas.
2.	Almacenar los datos extraídos en una base de datos SQL para su posterior procesamiento. Una vez se obtiene el DataFrame con los datos obtenidos, se pasa a SQL con la librería de Pandas.
3.	Generar un HTML utilizando PyScript, un framework que interconecta Python en un Script HTML. Gracias a PyScript se pueden utilizar las librerías de estadística de Python.
4.	 Crear estadísticas y gráficos utilizando las librerías MatPlotLib y Panel, que incluyan:
•	Mapas de calor que muestren las muertes, asesinatos y colocación de Wards.
•	Gráficas de barras horizontales que muestren los campeones más elegidos.
•	Tablas que muestren estadísticas de jugadores.
La librería Matplotlib se encarga de coger datos de los DataFrames y los transforma en gráficas que requiera el usuario. Posteriormente, mostramos la gráfica en un objeto Pane de la librería Panel, que lo que hace es mostrar la gráfica en una etiqueta que se elija.
5.	Mostrar las estadísticas y gráficos de forma interactiva y atractiva en la página web.
6.	Permitir al usuario filtrar y explorar los datos en la página web según diferentes criterios.
## 4.2	Requerimientos no funcionales:
•	Eficiencia: El proceso de extracción de datos y generación de estadísticas y gráficos debe ser eficiente para manejar grandes volúmenes de datos de manera rápida y efectiva.
•	Seguridad: Los datos extraídos y almacenados en la base de datos deben ser gestionados de forma segura, protegiendo la información sensible y evitando accesos no autorizados.
•	Usabilidad: La página web debe ser fácil de usar y comprender, con una interfaz intuitiva que permita a los usuarios interactuar con las estadísticas y gráficos de manera sencilla.
•	Interactividad: Los gráficos y estadísticas presentados en la página web deben ser interactivos, permitiendo al usuario explorar los datos y personalizar su visualización.
•	Flexibilidad: El sistema debe ser flexible y adaptable a posibles cambios en la estructura de la página lol.fandom.com, asegurando que la extracción de datos siga funcionando correctamente.
•	Mantenibilidad: El código y la infraestructura del proyecto deben ser mantenibles, permitiendo futuras actualizaciones, correcciones de errores y mejoras en el sistema.
•	Compatibilidad: La página web debe ser compatible con diferentes navegadores web y dispositivos, asegurando una experiencia consistente para los usuarios.
Estos requerimientos funcionales y no funcionales proporcionan una base para el desarrollo del proyecto y aseguran que se cumplan las expectativas y necesidades de los usuarios. 
# 5	DISEÑO
DISEÑO DEL PROYECTO: PÁGINA WEB DE ESTADÍSTICAS DE LEAGUE OF LEGENDS
## 5.1	Arquitectura y Componentes:
El proyecto se basa en una arquitectura cliente-servidor, donde el cliente es el navegador web utilizado por los usuarios y el servidor es la aplicación web que proporciona los datos y genera las estadísticas y gráficos. A continuación, se describen los componentes principales:
•	Cliente:
- Navegador web: Interfaz de usuario que permite a los usuarios acceder y visualizar la página web. 
El cliente tiene una página principal donde tiene un menú de navegación para ir directamente a los contenidos, luego distintas secciones dónde se especifican que información hay en cada apartado y una descripción general del proyecto.
 
Cada apartado se divide en las gráficas que se generan, que en este caso son cuatro: métricas, mapas de calor, Top Picks e Historial de partido. Cada apartado ejecuta un Script distinto y hace una consulta a la base de datos personalizada.
Tambíen existe un Logín, el cual tenía como meta principal hacer estadísticas personalizadas, pero al no haber acceso a la API del videojuego de momento sirve para mandarte newsletters.
 
Las métricas son los metadatos de cada temporada, los cuales muestran las estadísticas de cada jugador en ese periodo. Esto sirve para mostrar sus puntos fuertes y débiles, así como una comparación respecto a la temporada anterior.

 
Las métricas también tienen un apartado para ordenar de mayo a menor las columnas.
 
Los mapas de calor muestran las tendencias a que los jugadores mueran en cierto punto, hagan asesinatos o coloquen un objeto de visión (Ward ). Dichos objetivos se muestran encima del mapa oficial del juego para su fácil visualización.
 
 
Los Top Picks son gráficas de barras horizontales que muestran la tendencia a elegir cierto personaje, mostrando el top 5 de campeones más elegidos y su porcentaje.
 
 
Finalmente, el historial de partidas muestra resultados generales de la partida.
 
Todas estas páginas tienen en común el filtrado general, el cual sirve para filtrar por jugador, por equipo y por Split . También contienen un menú de navegación, el cual puedes acceder a cualquier enlace de la página o visitar las estadísticas de años posteriores (desde 2019, hasta la actualidad).

 


 
A la hora de filtrar los datos, se utiliza el framework PyScript, el cual, al generar eventos en la página ejecuta distintas instrucciones. Generalmente, son instrucciones para filtrar el gráfico/tabla o mostrar los menús. 
•	Servidor:
- Aplicación web: Se encarga de procesar las solicitudes del cliente y generar las respuestas correspondientes.
En el caso de este proyecto, una vez se accede a los distintos apartados, se hace una consulta a la base de datos respecto a cierto año y tipo de datos que se quieran mostrar. Esta consulta genera un data Frame específico y a partir de ahí se generan la gráfica que se requiera.
- HTML: Utiliza PyScript, un framework que interconecta Python en un Script HTML. Esto permite generar gráficas dinámicamente y filtrarlas al instante. Sería un sustituto de JavaScript, aunque todavía se encuentra en una fase temprana.
- Biblioteca Matplotlib: Utilizada para crear gráficos y visualizaciones a partir de los datos obtenidos.
- Biblioteca Panel: Utilizada para mostrar las estadísticas y gráficos de forma interactiva en la página web.
 
•	Obtención de los datos
- Web Scrap: Utiliza la técnica de Web Scraping para extraer datos de la página lol.fandom.com en formato JSON.
 
A continuación, se muestra un ejemplo de Web Scraping:
 
 
Primero se muestra como se obtiene el JSON de la página web lol.fandom.com y después como se obtiene información de una tabla.
- Librería Pandas: Utilizada para guardar los datos en un DataFrame y poder manejarlos para su posterior guardado en una Base de datos SQL.
Ejemplo de DataFrame:
 
- Base de datos SQLite: Almacena los datos extraídos para su posterior procesamiento y consulta.
 
•	Flujo de usuario
A continuación, se muestra cual es el flujo de navegación de la página web.
 
 
 
•	Programa para obtener los datos:
 
  
•	Base de datos: 
Este es el esquema entidad-relación de mi base de datos.
  
## 5.2	Tecnologías y Lenguajes:
 
- Python: Lenguaje de programación utilizado para desarrollar la aplicación web, realizar el Web Scraping, procesar los datos, generar los gráficos y agregar interactividad a la página web.
- HTML: Lenguaje de marcado utilizado para definir la estructura y el contenido de la página web.
- CSS: Lenguaje de estilos utilizado para aplicar estilos y mejorar la apariencia visual de la página web.
- SQLite: Sistema de gestión de bases de datos relacional que se caracteriza por ser ligero, rápido y de fácil implementación.
- Framework PyScript: Utilizado para interconectar Python en un Script HTML y generar el código HTML dinámicamente.
 
•	Herramientas utilizadas:
- Requests: Librería de Python utilizada para realizar solicitudes HTTP y obtener los datos del sitio lol.fandom.com.
- BeautifulSoup: Librería de Python utilizada para analizar el código HTML y extraer los datos deseados del sitio web.
- Pandas: Librería de Python utilizada para el manejo y procesamiento de datos, incluyendo la transformación de los datos extraídos en DataFrames.
- Matplotlib: Librería de Python utilizada para crear gráficos y visualizaciones a partir de los datos.
- Panel: Librería de Python utilizada para mostrar las estadísticas y gráficos de forma interactiva en la página web.
- SQLite3: Librería de Python que ayuda a conectar la aplicación con la base de datos de forma sencilla.
-Sphynx: Librería para documentar el código en Python (similar a JavaDoc).
En resumen, el proyecto utiliza Python como lenguaje principal de programación y se basa en técnicas de Web Scraping para obtener datos del sitio web lol.fandom.com. Los datos extraídos se almacenan en una base de datos SQL y se utilizan las bibliotecas Matplotlib y Panel para generar estadísticas y gráficos interactivos. La página web se genera utilizando PyScript, que permite interconectar Python en un Script HTML para mostrar los datos y gráficos de manera atractiva y personalizable. 
# 6	IMPLEMENTACIÓN
## 6.1	Entorno
En mi proyecto, he seleccionado Python como lenguaje de programación principal para adquirir, procesar, analizar y visualizar los datos. Para lograr esto, estoy utilizando el framework PyScript.
PyScript desempeña un papel fundamental, ya que permite ejecutar código en forma de scripts HTML, reemplazando así a JavaScript. Esta elección estratégica me brinda la ventaja de aprovechar las robustas bibliotecas de Python para el manejo de datos, así como para la generación dinámica de contenido. Además, gracias a PyScript, tengo total libertad para diseñar la interfaz web utilizando CSS.
En cuanto a la gestión de la base de datos, he optado por utilizar SQLite, considerándola la mejor alternativa debido a su fácil integración con Python y su naturaleza liviana. SQLite también destaca por su rapidez y eficiencia, lo que garantiza una visualización ágil de los datos.
Una vez que los datos han sido adquiridos, utilizo dos herramientas clave para su visualización: Matplotlib y Panel. Estas potentes bibliotecas me permiten generar gráficos interactivos que se incrustarán en la página web, enriqueciendo la experiencia de los usuarios.
Como editor utilizo Visual Studio Code, que es un editor de código fuente desarrollado por Microsoft. Se ha vuelto muy popular entre los desarrolladores debido a su simplicidad, su amplia gama de características y su capacidad de personalización. VS Code es un editor de texto liviano pero potente que proporciona un entorno de desarrollo integrado (IDE) para múltiples lenguajes de programación. En mi caso lo utilizo porque me da la opción de juntar en un mismo proyecto distintos lenguajes.
  
## 6.2	Datos
Mi proyecto se basa principalmente en los datos, ya que gracias a ellos genero las estadísticas y las gráficas. Como he mencionado anteriormente, utilizó la técnica de Web Scraping para extraer los datos relevantes de la página lol.fandom.com.
El formato a la hora de obtener los datos es en JSON. Utilizo la biblioteca requests en Python para realizar solicitudes HTTP a la página web y obtener los datos. Una vez tratados los datos, los almaceno en Data Frames. 
Un Data Frame es una estructura de datos tabular bidimensional en la que los datos se organizan en filas y columnas. Es una estructura similar a una tabla de una base de datos o una hoja de cálculo de Excel. En Python, el Data Frame es proporcionado por la biblioteca pandas, que es ampliamente utilizada para el análisis y manipulación de datos.
Posteriormente, una vez los datos tienen formato de DataFrame, con la librería Pandas tenemos la opción de guardar los datos en SQL, en este caso SQLite3.
Para que luego la lectura sea más fácil, he almacenado los datos por tipos: Picks y Bans de cada partida, posiciones de las muertes, asesinatos y primeras sangres de cada partida, Meta datos generales de una temporada y el historial de cada partida.
La consulta de datos la hago cada vez que se inicia una página
6.3	Configuración
A la hora de obtener los datos, utilizo un entorno virtual de Python. Dicho entorno me permite descargar librerías que no forman parte de la librería estándar, las cuales se descargan mediante PIP. 
En Python, a veces las aplicaciones necesitan una versión específica de una librería, debido a que dicha aplicación requiere que un bug particular haya sido solucionado o bien la aplicación ha sido escrita usando una versión obsoleta de la interfaz de la librería. Es por eso que se utiliza un entorno, el cual contiene una instalación de Python de una versión en particular, además de unos cuantos paquetes adicionales.
Las dependencias que utilizo son Pandas, Matplotlib, Panel, Requests, BeautifulSoup4 y NumPy.
•	Modelo-vista-controlador:
Respecto a la organización del código, me baso en el patrón Modelo-Vista-Controlador.
 
En el Modelo tenemos la parte de backend donde se guardan la estructura/lógica de los datos. En dicho paquete se encuentra el código con el cual generamos los datos y los guardamos, la base de datos y las descargas para controlar que los datos se obtienen bien (una vez verificado se guarda todo en la base de datos).
Esta parte se divide en los distintos modelos de datos, la base de datos y los tests.
 
Por otro lado, tenemos la parte de la página web, la cual es la parte de la vista del proyecto. Es decir, es el frontend o interfaz gráfica de usuario.
 
Por último, tenemos el controlador, la cual es el cerebro de la aplicación que controla como se muestran los datos. Aquí se muestra el JavaScript para gestionar el login y los Scripts de PyScript para los HTML.
 
 
•	Web Scraping: 
Implemento el código necesario para realizar el Web Scraping en Python utilizando librerías como requests o BeautifulSoup. Extraigo los datos necesarios de lol.fandom.com y los guardo en la base de datos.
Generación de gráficos: Utilizo la librería Matplotlib y Panel para generar los gráficos deseados basados en los datos extraídos. 
•	Integración el framework web - PyScript:
Como he comentado, utilizo PyScript, lo cual me permite manejar los Scripts de HTML con Python.
Para su perfecto funcionamiento, tengo que importar la hoja de estilos y el Script que permite utilizar pyScript en HTML:
 
Una vez importado, procedo la configuración de pyScript. En la configuración incluyo las librerías y fichero necesarios que voy a utilizar posteriormente:
 
Finalmente, incluyo el Script que quiero utilizar:
 
•	Firebase console:
Para controlar los usuarios que se registran o inician sesión utilizo Firebase.
Firebase es una plataforma para el desarrollo de aplicaciones web y aplicaciones móviles, el cual tiene herramientas como la autenticación de usuarios, manejo de bases de datos NOSQL, almacenamiento de imágenes, etc.
Para configurarlo, lo primero es crear un proyecto:
 
Una vez configurado, le implemento los modulos de Authetication y Cloud Firestore.
 
Authentication funciona como un administrador de usuarios. A través del código, se van creando usuarios o se les da la opción de iniciar sesión. En el caso de que no exista un usuario, sería el propio SDK de Firebase implementado el que nos diga que las credenciales no son correctas.
Así se implementaría Firebase en HTML.
 

Posteriormente, lo que he hecho es hacer un Script que permita registrar usuarios o iniciar sesión. También manejo el control de errores.
Una vez se registran, guardo los datos en Cloud Firestore para tratarlos posteriormente. 
# 7	PRUEBAS
## 7.1	Ejemplos de pruebas unitarias
•	Pruebo que al introducirle datos correctos, devuelva un data frame que no esté vacio.
 
•	Prueba para verificar que, al meterle datos vacíos, devuelve un data frame vacio.
 
•	Prueba para verificar que devuelve un data frame vacio cuando le metes una liga y temporada invalida
 
   
 
# 8	EXPLOTACIÓN
La explotación de un sistema informático abarca una serie de etapas cruciales para su funcionamiento eficiente y exitoso. 
## 8.1	Planificación
 

En primer lugar, la planificación es fundamental para establecer los objetivos del sistema, identificar los requisitos y definir un plan estratégico. En mi caso, la planificación se basó principalmente en la investigación de que herramientas me podrían resultar más prácticas y eficientes a la hora de mostrar mi aplicación.
Esa investigación desembocó posteriormente en la implementación de dichas herramientas hasta construir el proyecto que tenía en mente.
Los pasos que di a la hora de planificar mi trabajo fueron los siguientes:
Primero valoré que datos eran fundamentales para generar las estadísticas del League of Legends. A esta lluvia de ideas le siguió la investigación de la mejor forma de obtener y de guardar estos datos. Inicialmente se guardaban en ficheros CSV hasta que encontrase la mejor forma de guardarlos en una base de datos, así podría posteriormente obtener los datos de una forma rápida y eficiente.
Una vez tenía la estructura, había que pensar en cómo enseñar los datos. Desde el principio pensé que la mejor forma de mostrar los datos era a través de una página web, así podría llegar más fácil a mi público objetivo, sin obligarles a descargar una aplicación.
Una vez elegí mostrar los datos con PyScript, estuve investigando e implementando las herramientas para mostrar los datos. Finalmente, implementé un diseño a la página que lo hiciese más atractivo.

## 8.2	Gestión del cambio y migración
Considero que la gestión del cambio y migración es esencial para asegurar una transición fluida hacia el nuevo sistema en el contexto de este proyecto. Dado que este proyecto se basa en proporcionar datos y estadísticas actualizadas del juego, es importante estar preparado para los posibles cambios que puedan ocurrir tanto en el juego mismo como en las fuentes de datos disponibles.
En primer lugar, es fundamental estar al tanto de las actualizaciones y cambios en el juego League of Legends. Riot Games, como desarrollador del juego, realiza actualizaciones periódicas que pueden afectar la mecánica de juego, los personajes, los objetos y otras variables relevantes para el análisis de estadísticas. Es necesario establecer un proceso de seguimiento y evaluación de estas actualizaciones para asegurar que la página web refleje con precisión los cambios en el juego y proporcione estadísticas actualizadas a los usuarios.
Además, también es importante considerar los posibles cambios en las fuentes de datos disponibles. Es posible que Riot Games libere su API (Interfaz de Programación de Aplicaciones) que brinda acceso a los datos del juego de todos los jugadores. Estas modificaciones pueden afectar la forma en que se recopilan y presentan los datos en la página web. Por lo tanto, es necesario mantenerse informado sobre los cambios en la API y adaptar el sistema de recopilación y procesamiento de datos en consecuencia.

Para abordar estos posibles cambios desde el punto de vista de la gestión del cambio y migración, es esencial tener un equipo técnico bien preparado y actualizado. Este equipo deberá seguir de cerca las actualizaciones del juego y las modificaciones en la API, asegurándose de comprender plenamente los impactos que estos cambios puedan tener en la página web. Además, el equipo deberá estar capacitado para realizar las adaptaciones necesarias en el sistema de recopilación y procesamiento de datos, garantizando que la información presentada a los usuarios sea precisa y actualizada.
La comunicación con los usuarios también desempeña un papel crucial en la gestión del cambio y migración. Es fundamental informar a los usuarios sobre los posibles cambios que puedan ocurrir y cómo se abordarán desde el proyecto. Esto se puede lograr a través de comunicados y actualizaciones en la página web, correos electrónicos informativos o incluso mediante la implementación de un sistema de notificaciones dentro de la plataforma. La comunicación clara y oportuna ayudará a mitigar cualquier resistencia al cambio y mantendrá a los usuarios informados sobre las actualizaciones del juego y las adaptaciones realizadas en la página web.
En resumen, en el contexto de una página web de estadísticas del League of Legends, la gestión del cambio y migración implica estar preparado para los posibles cambios en el juego y en las fuentes de datos. Esto requiere un seguimiento constante de las actualizaciones del juego, una adaptación del sistema de recopilación y procesamiento de datos, un equipo técnico actualizado y capacitado, y una comunicación clara con los usuarios. Al abordar estos aspectos, se garantiza una transición fluida hacia el nuevo sistema y se asegura que los usuarios puedan seguir accediendo a estadísticas precisas y actualizadas del juego.

## 8.3	Implantación final
La implantación final consistiría en dos partes: 
La primera sería automatizar el proceso de descarga de datos. Esto implicaría utilizar un servicio en la nube que permita de forma recurrente obtener los datos de páginas para así tener a nuestros usuarios informados con los últimos datos de partidas recientes.
La segunda tiene que ver con los servicios en la nube, ya que para mostrar nuestra página se necesitaría hacer un hosting de ella.
## 8.4	Seguimiento y las pruebas
El seguimiento y las pruebas en producción son necesarios para monitorear el rendimiento del sistema y realizar ajustes según sea necesario.
Pienso establecer indicadores clave de rendimiento y llevar a cabo pruebas periódicas para identificar posibles problemas o áreas de mejora. Esto asegura que el sistema funcione de manera óptima y cumpla con los objetivos establecidos.

Finalmente, el mantenimiento continuo es fundamental para garantizar que el sistema esté actualizado, seguro y en funcionamiento durante toda su vida útil. Para ello, en este proyecto se intenta hacer pruebas y verificar que no hay ningún error. Si lo hubiese se intentaría arreglar de la forma más rápida y óptima posible.
 
# 9	PRESUPUESTO
Este presupuesto presenta una estimación de costos para el desarrollo y lanzamiento de LOL Statium. El presupuesto está pensado para un equipo compuesto por dos desarrolladores y un analista de datos.
Categoría	Descripción	Coste Estimado
Hardware	Equipos para desarrollar para una plantilla de 3 personas (computadora, monitores, periféricos)	2000 € – 3000 €
Software	Licencias y herramientas de desarrollo (IDE, editores)	0€ (hay IDEs y editores gratuitos)
Servicios en la nube	Servidores Web que pueden automatizar el proceso de Web Scraping y alojamiento de la página	10 € - 100€ (dependiendo del tráfico de la Web y las herramientas que se requiera)
Costos fijos	Dominio, seguridad SSL y otros costos recurrentes	80 € - 160 € por año
Costos variables	Marketing, publicidad y promoción (de momento en redes o Google)	20 € mensuales
 
# 10	 CONCLUSIONES
En este proyecto, se ha desarrollado una página web que muestra información y gráficos sobre el videojuego League of Legends, centrándose en la liga LEC, una de las más importantes a nivel europeo. Para obtener los datos necesarios, se ha utilizado la técnica de Web Scraping para extraer información relevante de la página lol.fandom.com en un formato fácil de usar.
Los datos extraídos se han transformado en un marco de datos utilizando la biblioteca Pandas, lo que ha permitido su manejo y almacenamiento eficiente en una base de datos SQL. La utilización de una base de datos ha facilitado la gestión y consulta de los datos, garantizando su integridad y seguridad.
La página web ha sido creada utilizando Python, un lenguaje de programación muy popular y versátil. Se ha utilizado el framework PyScript para interconectar Python en un script HTML, lo que ha permitido generar un HTML dinámico y interactivo.
Se han utilizado las librerías Matplotlib y Panel de Python para generar diversos tipos de gráficos y estadísticas sobre el videojuego League of Legends y la liga LEC. Estos gráficos incluyen mapas de calor que muestran las muertes, asesinatos y colocación de Wards, gráficas de barras horizontales que muestran los campeones más elegidos, tablas comparativas de rendimiento de los jugadores, entre otros.
El proyecto ha logrado satisfacer los objetivos propuestos al proporcionar una página web que ofrece información relevante y atractiva sobre el videojuego League of Legends y la liga LEC. Los usuarios pueden acceder a estadísticas y gráficos interactivos que les permiten explorar los datos y obtener una mejor comprensión del juego.
Además, el proyecto ha permitido desarrollar competencias en áreas como la programación, el manejo de bases de datos, el análisis de datos y la visualización de información. También se ha enfrentado al reto de utilizar PyScript, una tecnología en desarrollo temprano, lo que ha implicado un esfuerzo adicional para comprender y aplicar esta herramienta.

En resumen, este proyecto ha sido exitoso en la creación de una página web que proporciona información detallada y gráficos interactivos sobre el videojuego League of Legends y la liga LEC. Ha cumplido con los objetivos propuestos y ha permitido el desarrollo de habilidades técnicas y formativas en el área de programación, análisis de datos y visualización de información. 
# 11	 LÍNEAS DE TRABAJO FUTURAS
A continuación, me gustaría destacar las posibles líneas de trabajo futuras que este proyecto podría abordar.
Una de ellas es la implementación de algoritmos de aprendizaje automático más avanzados para mejorar la precisión y la eficiencia de las predicciones en el análisis de partidas de League of Legends. Esto nos permitiría obtener resultados aún más precisos y detallados, lo que sería de gran utilidad para los jugadores y los analistas.
Otra línea de trabajo interesante sería la integración de nuevas fuentes de datos en el análisis de partidas. Por ejemplo, podríamos explorar la posibilidad de utilizar datos de otros videojuegos con competitivo para obtener otro tipo de información. Esto nos proporcionaría una visión más completa y enriquecedora del panorama competitivo de los eSports .
Además, considero importante investigar y desarrollar herramientas de visualización más avanzadas para presentar los resultados del análisis de partidas de manera más intuitiva y comprensible. Esto permitiría a los usuarios interpretar y aprovechar mejor la información proporcionada por la plataforma, facilitando la toma de decisiones estratégicas y tácticas durante las partidas.
Por otro lado, es relevante mencionar que Riot Games ha cerrado temporalmente el acceso a su API debido a la ley de protección de datos. Sin embargo, se espera que próximamente se habilite nuevamente el acceso a la API, lo que sería un gran avance para el proyecto. Esto permitiría obtener datos en tiempo real y acceder a información más detallada sobre las partidas de jugadores que no sea del mundo del competitivo, lo que mejoraría significativamente la calidad, la precisión de nuestros análisis y ayudaría a los usuarios a mejorar en el juego.
En resumen, las líneas de trabajo futuras para este proyecto incluyen la implementación de algoritmos de aprendizaje automático más avanzados, la integración de nuevas fuentes de datos, el desarrollo de herramientas de visualización mejoradas y la expectativa de volver a utilizar la API de Riot Games en un futuro cercano, una vez que se resuelvan las cuestiones legales relacionadas con la protección de datos. Estas mejoras nos permitirían ofrecer a los jugadores y a la comunidad de eSports una plataforma más completa, precisa y útil para el análisis de partidas de League of Legends.
