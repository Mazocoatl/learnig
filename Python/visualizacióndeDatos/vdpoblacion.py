import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
import csv
 #visualizar los datos de un csv
datos = pd.read_csv('C:/Users/jairj/OneDrive/Documentos/learning/Python/cp2/app/data.csv')

#grafica de barras de la poblacion de los continentes por año
sns.set_theme(style="whitegrid") #estilo de la grafica
datos = pd.read_csv('C:/Users/jairj/OneDrive/Documentos/learning/Python/cp2/app/data.csv') #lee el csv
sns.barplot(x="Continente", y="2022 Population", data=datos, ci=False) #grafica de barras
plt.show() #muestra la grafica

#grafica de dispersión de la poblacion de los continentes por año
sns.set_theme(style="whitegrid") #estilo de la grafica
datos = pd.read_csv('C:/Users/jairj/OneDrive/Documentos/learning/Python/cp2/app/data.csv') #lee el csv
sns.scatterplot(x="Continente", y="2022 Population", data=datos, hue="Continente") #grafica de dispersión
plt.show() #muestra la grafica

#grafica de lineas de la poblacion de los continentes por año
sns.set_theme(style="whitegrid") #estilo de la grafica
datos = pd.read_csv('C:/Users/jairj/OneDrive/Documentos/learning/Python/cp2/app/data.csv') #lee el csv
sns.lineplot(x="Continente", y="2022 Population", data=datos, hue="Continente") #grafica de lineas
plt.show() #muestra la grafica

#grafica de pointplot de la poblacion de los continentes por año
sns.set_theme(style="whitegrid") #estilo de la grafica
datos = pd.read_csv('C:/Users/jairj/OneDrive/Documentos/learning/Python/cp2/app/data.csv') #lee el csv
sns.pointplot(x="Continente", y="2022 Population", data=datos, hue="Continente") #grafica de pointplot
plt.show() #muestra la grafica

#grafica de boxplot de la poblacion de los continentes por año
sns.set_theme(style="whitegrid") #estilo de la grafica
datos = pd.read_csv('C:/Users/jairj/OneDrive/Documentos/learning/Python/cp2/app/data.csv') #lee el csv
sns.boxplot(x="Continente", y="2022 Population", data=datos, hue="Continente") #grafica de boxplot
plt.show() #muestra la grafica

#grafica del crecimiento de población de los continentes desde 1970 hasta 2022
sns.set_theme(style="whitegrid") #estilo de la grafica
datos = pd.read_csv('C:/Users/jairj/OneDrive/Documentos/learning/Python/cp2/app/data.csv') #lee el csv
sns.barplot(x="Continente", y="2022 Population", data=datos, hue="Continente") #grafica de lineas
sns.barplot(x="Continente", y="2020 Population", data=datos, hue="Continente") #grafica de lineas
sns.barplot(x="Continente", y="2015 Population", data=datos, hue="Continente") #grafica de lineas
sns.barplot(x="Continente", y="2010 Population", data=datos, hue="Continente") #grafica de lineas
sns.barplot(x="Continente", y="2000 Population", data=datos, hue="Continente") #grafica de lineas
sns.barplot(x="Continente", y="1990 Population", data=datos, hue="Continente") #grafica de lineas
sns.barplot(x="Continente", y="1980 Population", data=datos, hue="Continente") #grafica de lineas
sns.barplot(x="Continente", y="1970 Population", data=datos, hue="Continente") #grafica de lineas
plt.show() #muestra la grafica




