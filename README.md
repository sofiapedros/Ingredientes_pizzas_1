# Ingredientes_pizzas_1
El repositorio contiene los siguientes ficheros:
- etl.py
- analisis_de_los_datos.py
- analisis_de_los_datos_txt.py
- Analisis_datos.txt
- requirements.txt
- data_dictionary.csv
- order_details.csv
- orders.csv
- pizza_types.csv
- pizzas.csv
- final.csv

### etl.py
"etl.py": Programa que, dado un conjunto de datos de una pizzería como ficheros csv, calcula los ingredientes que debe comprar esa pizzería en una semana, suponiendo que el número de ventas de la pizzería en una semana sea regular (utiliza la media de todos los pedidos). Además, supone que la cantidad de ingredientes de una pizza es 1 ración para la pizza pequeña, 2 para la mediana, 3 para la grande y 4 para tamaños superiores. Guarda la lista de los ingredientes a comprar con el número de raciones necesarias en un csv llamado "final.csv". Realiza esta funcionalidad como una etl: primero extrae los datos, después los tranforma, y por último obtiene un resultado en forma de un nuevo csv.

### analisis_de_los_datos.py
"analisis_de_los_datos.py": programa que imprime un análisis de los datos proporcionados por la pizzería. Imprime número de NaN y nulls totales y por columna así como el
tipo de datos de cada columna.

### analisis_de_los_datos_txt.py
"analisis_de_los_datos.py": programa que guarda en un fichero .txt (Analisis_datos.txt) un análisis de los datos proporcionados por la pizzería. Imprime número de NaN y nulls totales y por columna así como el
tipo de datos de cada columna.

### Analisis_datos.txt
Fichero de texto de salida al ejecutar analisis_de_los_datos_txt.py

### requirements.txt
Librerías utilizadas

### final.csv
Csv obtenido como salida al realizar la etl

### Resto de ficheros csv
Ficheros csv sobre los que se han extraido los datos para hacer el análisis
