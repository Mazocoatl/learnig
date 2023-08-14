import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

penguins = sns.load_dataset("penguins")
#extraer los datos de penguins en un csv
penguins.to_csv('C:/Users/jairj/OneDrive/Documentos/learning/Python/visualizacióndeDatos/penguins.csv')

sns.set_theme(style="darkgrid", context='talk')
sns.relplot(
    data=penguins,
    x="flipper_length_mm", # Establecer el eje x
    y="bill_length_mm", # Establecer el eje y
)
sns.relplot(
    data=penguins,
    x="flipper_length_mm", # Establecer el eje x
    y="bill_length_mm", # Establecer el eje y
    hue="body_mass_g", # Establecer el color de la gráfica
    s=300 # Tamaño de los puntos de la gráfica
)
sns.relplot(
    data=penguins,
    x="flipper_length_mm", # Establecer el eje x
    y="bill_length_mm", # Establecer el eje y
    hue="body_mass_g", # Establecer el color de la gráfica
    size="sex", # Establecer el tamaño de los puntos de la gráfica
)
sns.relplot(
    data=penguins,
    x="flipper_length_mm",  # Establecer el eje x
    y="bill_length_mm", # Establecer el eje y
    hue="species", # Establecer el color de la gráfica
    size="body_mass_g", # Establecer el tamaño de los puntos de la gráfica
    palette="ch:r=-.5,l=.75", # Color de la gráfica (ch: color hue, r: red, l: light
    sizes=(10, 200), # Tamaño de los puntos de la gráfica (min, max)
    style="sex", # Establecer el estilo de la gráfica
)
sns.relplot(
    data=penguins,
    x="flipper_length_mm", # Establecer el eje x
    y="bill_length_mm", # Establecer el eje y
    hue="species", # Establecer el color de la gráfica
    row='sex', # Establecer el número de filas de la gráfica
    size="body_mass_g", # Establecer el tamaño de los puntos de la gráfica
    sizes=(10,200),
    style='sex'
)
sns.relplot(
    data=penguins,
    x="flipper_length_mm", # Establecer el eje x
    y="bill_length_mm", # Establecer el eje y
    hue="species", # Establecer el color de la gráfica
    row='sex', # Establecer el número de filas de la gráfica
    col='island', # Establecer el número de columnas de la gráfica
    size="body_mass_g", # Establecer el tamaño de los puntos de la gráfica
    sizes=(10,200),
    style='sex'
)
sns.relplot(
    data=penguins,
    x="flipper_length_mm",  # Establecer el eje x
    y="bill_length_mm", # Establecer el eje y
    hue="species", # Establecer el color de la gráfica
    col='island', # Establecer el número de columnas de la gráfica
    size="body_mass_g", # Establecer el tamaño de los puntos de la gráfica
    palette="ch:r=-.5,l=.75", # Color de la gráfica (ch: color hue, r: red, l: light
    sizes=(10, 200), # Tamaño de los puntos de la gráfica (min, max)
    style="sex", # Establecer el estilo de la gráfica
)
#gráfico de lineas
sns.relplot(
    data=penguins,
    x='species', # Establecer el eje x
    y='body_mass_g', # Establecer el eje y
    kind='line', # Establecer el tipo de gráfica
    hue='sex', # Establecer el color de la gráfica
    style='sex', # Establecer el estilo de la gráfica
    markers=True, # Establecer si se muestran los marcadores o no
)
#gráfico de lineas
sns.relplot(
    data=penguins,
    x='flipper_length_mm', # Establecer el eje x
    y='bill_length_mm', # Establecer el eje y
    kind='line', # Establecer el tipo de gráfica
    hue='species', # Establecer el color de la gráfica
    style='species', # Establecer el estilo de la gráfica
    markers=True, # Establecer si se muestran los marcadores o no
)
#grafico de pie (piechart) relacionando la distribución de los pingüinos por especie
penguins['species'].value_counts().plot(kind='pie', autopct='%1.1f%%', shadow=True, startangle=90)
plt.title('Distribución de los pingüinos por especie')
#Combina dos gráficas
figura, ejes = plt.subplots(1, 2, figsize=(15, 5)) # Establecer el número de filas y columnas de la gráfica y el tamaño de la misma
sns.lineplot(
    data=penguins,
    x='species', # Establecer el eje x
    y='body_mass_g', # Establecer el eje y
    hue='sex', # Establecer el color de la gráfica
    style='sex', # Establecer el estilo de la gráfica
    ci=95, # Establecer el intervalo de confianza
    ax=ejes[0] # Establecer el eje en el que se muestra la gráfica
)
sns.scatterplot(
    data=penguins,
    x='bill_length_mm', # Establecer el eje x
    y='flipper_length_mm', # Establecer el eje y
    hue='species', # Establecer el color de la gráfica
    s=100, # Establecer el tamaño de los puntos de la gráfica
    style='species', # Establecer el estilo de la gráfica
    ax=ejes[1] # Establecer el eje en el que se muestra la gráfica
)

plt.show()