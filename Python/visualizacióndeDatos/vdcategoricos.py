import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

sns.set_theme(style="ticks", context='talk', palette='pastel')

consumos = sns.load_dataset("tips")
consumos.columns = ['Total', 'Propina', 'Genero', 'Fumador', 'Día', 'Tipo', 'Comensales']
consumos.to_csv('C:/Users/jairj/OneDrive/Documentos/learning/Python/visualizacióndeDatos/consumos.csv')

sns.catplot( # Establecer el tipo de gráfica
    data = consumos, # Establecer los datos
    x = 'Día', # Establecer el eje x
    y = 'Total', # Establecer el eje y
    hue = 'Comensales', # Establecer el color de la gráfica
    kind = 'strip', # Establecer el tipo de gráfica
    jitter = True, # Establecer el jitter de la gráfica
    col = 'Fumador', # Establecer el número de columnas de la gráfica
)
sns.catplot( # Establecer el tipo de gráfica
    data = consumos, # Establecer los datos
    x = 'Día', # Establecer el eje x
    y = 'Total', # Establecer el eje y
    hue = 'Comensales', # Establecer el color de la gráfica
    kind = 'swarm', # Establecer el tipo de gráfica
    col = 'Fumador', # Establecer el número de columnas de la gráfica
)

#Gráficas categóricas de distribución
#Gráficas de distribución de boxplot (cajas y bigotes)
sns.catplot( # Establecer el tipo de gráfica
    data = consumos, # Establecer los datos
    x = 'Día', # Establecer el eje x
    y = 'Total', # Establecer el eje y
    hue = 'Comensales', # Establecer el color de la gráfica
    kind = 'box', # Establecer el tipo de gráfica
    col = 'Fumador', # Establecer el número de columnas de la gráfica
)
#Gráficas de distribución de boxen (boxplot más detallado)
sns.catplot( # Establecer el tipo de gráfica
    data = consumos, # Establecer los datos
    x = 'Día', # Establecer el eje x
    y = 'Total', # Establecer el eje y
    hue = 'Comensales', # Establecer el color de la gráfica
    kind = 'boxen', # Establecer el tipo de gráfica
    col = 'Fumador', # Establecer el número de columnas de la gráfica
)
#Gráficas de distribución de violín (boxplot más detallado)
sns.catplot( # Establecer el tipo de gráfica
    data = consumos, # Establecer los datos
    x = 'Día', # Establecer el eje x
    y = 'Total', # Establecer el eje y
    kind = 'violin', # Establecer el tipo de gráfica
)
sns.catplot( # Establecer el tipo de gráfica
    data = consumos, # Establecer los datos
    x = 'Día', # Establecer el eje x
    y = 'Total', # Establecer el eje y
    kind = 'violin', # Establecer el tipo de gráfica
    hue = 'Fumador', # Establecer el color de la gráfica
)
sns.catplot( # Establecer el tipo de gráfica
    data = consumos, # Establecer los datos
    x = 'Día', # Establecer el eje x
    y = 'Total', # Establecer el eje y
    kind = 'violin', # Establecer el tipo de gráfica
    hue = 'Fumador', # Establecer el color de la gráfica
    split = True, # Establecer si se divide o no la gráfica
)

#gráficas categóricas de estimación
#gráficas de estimación pointplot (gráfica de puntos)
sns.catplot( # Establecer el tipo de gráfica
    data = consumos, # Establecer los datos
    x = 'Día', # Establecer el eje x
    y = 'Total', # Establecer el eje y
    kind = 'point', # Establecer el tipo de gráfica (pointplot)
    col = 'Fumador', # Establecer el número de columnas de la gráfica
)
#gráfica de pastel del total de consumo con respecto a fumadores o no fumadores
plt.pie(consumos.groupby('Fumador')['Total'].sum(), labels = ['No fumadores', 'Fumadores'], autopct = '%1.1f%%', shadow = True, startangle = 90)
plt.title('Total de consumo con respecto a fumadores o no fumadores')
#gráficas de estimación barplot (gráfica de barras)
sns.catplot( # Establecer el tipo de gráfica
    data = consumos, # Establecer los datos
    x = 'Día', # Establecer el eje x
    y = 'Total', # Establecer el eje y
    kind = 'bar', # Establecer el tipo de gráfica
    hue = 'Comensales', # Establecer el color de la gráfica
)
#gráficas de estimación countplot (gráfica de conteo)
sns.catplot( # Establecer el tipo de gráfica
    data = consumos, # Establecer los datos
    x = 'Día', # Establecer el eje x
    kind = 'count', # Establecer el tipo de gráfica
    hue = 'Comensales', # Establecer el color de la gráfica
)
#gráfica de pastel del total de consumo con respecto a fumadores o no fumadores
plt.pie(consumos.groupby('Fumador')['Total'].sum(), labels = ['No fumadores', 'Fumadores'], autopct = '%1.1f%%', shadow = True, startangle = 90)
plt.title('Total de consumo con respecto a fumadores o no fumadores')

plt.show()