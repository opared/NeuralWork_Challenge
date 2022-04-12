# NeuralWork_Challenge

Este repositorio muestra mi solución al Challenge propuesto para el cargo de Data Engineer

Cree una solución en Django REST framework que permite la carga de datos a una base de datos SQLlite.
Esto a través del requerimiento cargar-viajes/ , el cual solo requiere un .CSV con los datos

Además se le pueden solicitar diferentes tipos de filtrado, 

* 'filtro-semana/', devuelve los viajes que ocurren en una semana, esta es determinada de acuerdo a una fecha en cadena de caracteres con la  forma YYYY-MM-dd que le es indicada.
* 'filtro-coordenadas/', devuelve los viajes cuyo origen o destino se encuentran dentro de una cuadricula, este requerimiento necesita 5 valores entregados en orden, que son "coor_up" ,"coor_down",  "coor_right" ,"coor_left" y "columna", las primeras 4 corresponden a las coordenadas superior, inferior, derecha e izquierda del recuadro y la ultima es para elegir si evaluar en las coordenadas de origen ("origin_coord") o de destino ("destination_coord"). 
* 'filtro-hora/', devuelve los viajes filtrados por hora del día, requiere que se le pase una hora en cadena de caracteres con la forma HH:MM.
* 'filtro-fuente/', filtra según la fuente de los datos, se le debe pasar el nombre de la fuente tal como aparece en los datos 
* 'filtro-region/', filtra según la región, se le debe pasar el nombre de la región.

Todos estos filtrados entregan la lista de viajes filtrada y el promedio de viajes por semana.
Solo el filtro  'filtro-semana/' no entrega el promedio de viajes por semana.


El desempeño de esta solución fue evaluado con Locust, se puede ver el resultado en el archivo 'benchmarking.html', empieza a tener problemas cuando alcanza los 600 usuarios, esto se debe a que realice las pruebas en mi PC que no es muy buen servidor
