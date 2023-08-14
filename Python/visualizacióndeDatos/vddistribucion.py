#Distribution de Datos e Histogramas
import matplotlib.pyplot as plt
import numpy as np

datos = [1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # Establecer los datos
plt.hist(datos, bins = 5, color = 'pink', ec = 'black') # Establecer los datos a graficar
#Generar arreglos de datos aleatorios
datos = np.random.randn(10) * 10 # Establecer los datos aleatorios con una distribución normal de media 0 y desviación estándar 1
ejemplo = np.random.normal(loc = 100, scale = 10, size = 1000) # Establecer los datos aleatorios con una distribución normal de media 100 y desviación estándar 10
ejemplo.mean() # Calcular la media de los datos
print(ejemplo.mean()) # Mostrar la media de los datos
ejemplo.std() # Calcular la desviación estándar de los datos
print(ejemplo.std()) # Mostrar la desviación estándar de los datos
ejemplo.var() # Calcular la varianza de los datos
print(ejemplo.var()) # Mostrar la varianza de los datos
plt.hist(ejemplo, bins = 5, color = 'pink', ec = 'black') # Establecer los datos a graficar
plt.show() # Mostrar la gráfica
#Generar arreglos de datos aleatorios
datos1 = np.random.normal(size = 1000000) # Establecer los datos aleatorios con una distribución normal de media 0 y desviación estándar 1
plt.hist(datos1, color = 'pink', ec = 'black') # Establecer los datos a graficar
plt.title('Distribución normal') # Establecer el título de la gráfica
plt.show() # Mostrar la gráfica
datos2 = np.random.uniform(size = 1000000) # Establecer los datos aleatorios con una distribución uniforme de media 0 y desviación estándar 1
plt.hist(datos2, color = 'skyblue', ec = 'black') # Establecer los datos a graficar
plt.title('Distribución uniforme') # Establecer el título de la gráfica
plt.show() # Mostrar la gráfica
datos3 = np.random.exponential(size = 1000000) # Establecer los datos aleatorios con una distribución exponencial de media 0 y desviación estándar 1|
plt.hist(datos3, color = 'green', ec = 'black') # Establecer los datos a graficar
plt.title('Distribución exponencial') # Establecer el título de la gráfica
plt.show() # Mostrar la gráfica