import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

penguins = sns.load_dataset("penguins") # Cargar el dataset de pinguinos de seaborn

sns.set_theme(style="darkgrid", context='talk') # Establecer el estilo de la gráfica y el contexto de la misma (paper, notebook, talk, poster)
# Visualizar los datos
relacional = sns.relplot(data=penguins, height=7, aspect=1.2, markers=['s', '.', 'P', 'd']) # Establecer el tipo de gráfica, los datos, el tamaño y el aspecto de la gráfica
relacional.set(title='Análisis de pingüinos') # Establecer el título de la gráfica
relacional.set(xlabel='Número de pingüinos') # Establecer el título del eje x
relacional.set(ylabel='Variables') # Establecer el título del eje y
plt.grid(True) # Establecer si se muestra la cuadrícula o no

plt.show()