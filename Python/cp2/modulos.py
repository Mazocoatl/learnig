#modulo: conjunto de funciones que se pueden reutilizar en otros programas

import sys #importa el módulo sys (system) que contiene funciones y variables que se usan para manipular diferentes partes del entorno de ejecución de Python (como el path) y para interactuar con el intérprete de Python (como la versión de Python que se está usando).
print(sys.path)

import re #importa el módulo re (regular expression) que contiene funciones y variables que se usan para trabajar con expresiones regulares.
text = 'mi número es 1234-1234-1234, el código del país es 54, mi número de la suerte es 13'
print(re.findall('[0-9]+', text))

import time #importa el módulo time que contiene funciones y variables que se usan para trabajar con fechas y horas. 
timestamp = time.time()
print(timestamp)
print(time.ctime(timestamp))
localtime = time.localtime(timestamp)
print(localtime)
result = time.asctime(localtime)
print(result)
print('año: ', localtime.tm_year)
print('mes: ', localtime.tm_mon)
print('día: ', localtime.tm_mday)
print('hora: ', localtime.tm_hour)
print('minutos: ',localtime.tm_min)
print('segundos: ', localtime.tm_sec)
print(time.strftime('%Y-%m-%d %H:%M:%S', localtime))

import datetime #importa el módulo datetime que contiene funciones y variables que se usan para trabajar con fechas y horas. Es más completo que el módulo time.
print(datetime.datetime.now())
print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

import collections #importa el módulo collections que contiene funciones y variables que se usan para trabajar con colecciones de datos. 
numbers = [1,2,3,4,5,6,7,8,9,0,1,2,3,4,5]
counter = collections.Counter(numbers) #Counter es una subclase de dict que se usa para contar objetos hashables. Es una colección no ordenada donde los elementos son almacenados como claves de diccionario y sus recuentos como valores de diccionario.
print(counter)
print(counter.most_common(3)) #muestra los 3 elementos más comunes de la colección

import random #importa el módulo random que contiene funciones y variables que se usan para trabajar con números aleatorios.
print(random.choice(['a','b','c','d','e','f','g','h','i','j','k','l','m','n']))
print(random.sample(range(100), 10)) #muestra 10 números aleatorios del 0 al 99
print(random.random()) #muestra un número aleatorio entre 0 y 1
print(random.randrange(6)) #muestra un número aleatorio entre 0 y 5
print(random.randint(1,6)) #muestra un número aleatorio entre 1 y 6

import statistics #importa el módulo statistics que contiene funciones y variables que se usan para trabajar con estadísticas.
print(statistics.mean([1,2,3,4,5,6,7,8,9,0,1,2,3,4,5])) #muestra el promedio de los números de la lista
print(statistics.median([1,2,3,4,5,6,7,8,9,0,1,2,3,4,5])) #muestra la mediana de los números de la lista
print(statistics.mode([1,2,3,4,5,6,7,8,9,0,1,2,3,4,5])) #muestra la moda de los números de la lista
print(statistics.stdev([1,2,3,4,5,6,7,8,9,0,1,2,3,4,5])) #muestra la desviación estándar de los números de la lista

import os #importa el módulo os (operating system) que contiene funciones y variables que se usan para trabajar con el sistema operativo.
print(os.getcwd()) #muestra el directorio de trabajo actual
print(os.listdir()) #muestra los archivos y directorios del directorio de trabajo actual

import glob #importa el módulo glob que contiene funciones y variables que se usan para trabajar con patrones de nombres de archivos.
print(glob.glob('*.py')) #muestra los archivos con extensión .py del directorio de trabajo actual
print(glob.glob('*.txt')) #muestra los archivos con extensión .txt del directorio de trabajo actual