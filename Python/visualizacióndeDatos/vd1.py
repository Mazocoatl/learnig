import matplotlib.pyplot as plt
import numpy as np

anos = [ '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']

nivel1= np.random.rand(10) * 100
nivel2 = np.random.rand(10) * 200 + 100
nivel3 = np.random.rand(10) * 200 + 200
nivel4 = np.random.rand(10) * 200 + 300
nivel5 = np.random.rand(10) * 200 + 400

plt.plot(anos, nivel5, label='Nivel 5', color = 'purple', marker = '<', linestyle = '-') #label es para que se muestre la leyenda y color es para que se muestre de color morado y marker es para que se muestre el marcador de la gráfica y linestyle es para que se muestre la línea de la gráfica
plt.plot(anos, nivel4, label='Nivel 5', color = 'green', marker = '>', linestyle = '--')
plt.plot(anos, nivel3, label='Nivel 5', color = 'blue', marker = '+', linestyle = ':')
plt.plot(anos, nivel2, label='Nivel 5', color = 'black', marker = '*', linestyle = '-.')
plt.plot(anos, nivel1, label='Nivel 5', color = 'red', marker = 'o', linestyle = ' ')

plt.legend() #para que se muestre la leyenda
# Título de la gráfica
plt.title('Resultados en los últimos 10 años que se ha realizado el examen')
# Etiquetas de los ejes
plt.xlabel('Años')
plt.ylabel('Puntaje')
plt.grid(True) #para que se muestre la cuadrícula
#Personalizar los ejes
plt.axis([0, 10, 0, 600]) #para que se muestre el eje x de 0 a 10 y el eje y de 0 a 600
#Activar marcas menores
plt.yticks(np.arange(0, 1001, 50)) #para que se muestre el eje y de 0 a 1000 con saltos de 50
plt.minorticks_on()
plt.show() #para que se muestre la gráfica

eje_x = np.arange(0, 10) #para que se muestre el eje x de 0 a 10

#para que se muestre la gráfica de barras
plt.bar(eje_x, nivel5, label='Nivel 5', color = 'red', width = 1/5) #width es para que se muestre la gráfica de barras con un ancho de 1/5
plt.bar(eje_x + 0.2, nivel4, label='Nivel 4', color = 'blue', width = 1/5) #para que se muestre la gráfica de barras desplazada 0.2
plt.bar(eje_x + 0.4, nivel3, label='Nivel 3', color = 'green', width = 1/5)
plt.bar(eje_x + 0.6, nivel2, label='Nivel 2', color = 'yellow', width = 1/5)
plt.bar(eje_x + 0.8, nivel1, label='Nivel 1', color = 'purple', width = 1/5)

plt.legend()
plt.title('Resultados en los últimos 10 años que se ha realizado el examen')
plt.xlabel('Años')
plt.ylabel('Puntaje')
plt.grid(True)
plt.yticks(np.arange(0, 1001, 50)) 
plt.minorticks_on()
plt.show()

#para que se muestre la gráfica de barras horizontales

plt.barh(eje_x, nivel5, label='Nivel 5', color = 'red', height = 1/5) #height es para que se muestre la gráfica de barras horizontales con un ancho de 1/5
plt.barh(eje_x + 0.2, nivel4, label='Nivel 4', color = 'blue', height = 1/5) #para que se muestre la gráfica de barras horizontales desplazada 0.2
plt.barh(eje_x + 0.4, nivel3, label='Nivel 3', color = 'green', height = 1/5)
plt.barh(eje_x + 0.6, nivel2, label='Nivel 2', color = 'yellow', height = 1/5)
plt.barh(eje_x + 0.8, nivel1, label='Nivel 1', color = 'purple', height = 1/5)

plt.legend()
plt.title('Resultados en los últimos 10 años que se ha realizado el examen')
plt.xlabel('Años')
plt.ylabel('Puntaje')
plt.grid(True)
plt.minorticks_on()
plt.show()

#para que se muestre la gráfica de barras apiladas

plt.bar(eje_x, nivel5, label='Nivel 5', color = 'red', width = 1/5) #width es para que se muestre la gráfica de barras con un ancho de 1/5
plt.bar(eje_x, nivel4, label='Nivel 4', color = 'blue', width = 1/5, bottom = nivel5) #para que se muestre la gráfica de barras desplazada 0.2 y bottom es para que se muestre la gráfica de barras apiladas
plt.bar(eje_x, nivel3, label='Nivel 3', color = 'green', width = 1/5, bottom = nivel5 + nivel4)
plt.bar(eje_x, nivel2, label='Nivel 2', color = 'yellow', width = 1/5, bottom = nivel5 + nivel4 + nivel3)
plt.bar(eje_x, nivel1, label='Nivel 1', color = 'purple', width = 1/5, bottom = nivel5 + nivel4 + nivel3 + nivel2)

plt.legend()
plt.title('Resultados en los últimos 10 años que se ha realizado el examen')
plt.xlabel('Años')
plt.ylabel('Puntaje')
plt.grid(True)
plt.minorticks_on()
plt.show()

#para que se muestre la gráfica de dispersión

plt.scatter(anos, nivel5, label='Nivel 5', color = 'red', marker = 'o') #marker es para que se muestre el marcador de la gráfica
plt.scatter(anos, nivel4, label='Nivel 4', color = 'blue', marker = 'v')
plt.scatter(anos, nivel3, label='Nivel 3', color = 'green', marker = 's')
plt.scatter(anos, nivel2, label='Nivel 2', color = 'yellow', marker = 'p')
plt.scatter(anos, nivel1, label='Nivel 1', color = 'purple', marker = 'P')

plt.legend()
plt.title('Resultados en los últimos 10 años que se ha realizado el examen')
plt.xlabel('Años')
plt.ylabel('Puntaje')
plt.grid(True)
plt.minorticks_on()
plt.show()

#para que se muestre la gráfica de pastel

plt.pie(nivel5, labels = anos, startangle = 90, shadow = True, explode = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0.1), autopct = '%1.1f%%') #labels es para que se muestre la leyenda, startangle es para que se muestre el ángulo de inicio, shadow es para que se muestre la sombra, explode es para que se muestre la gráfica de pastel separada, autopct es para que se muestre el porcentaje
plt.legend()
plt.title('Resultados en los últimos 10 años que se ha realizado el examen')
plt.show()

#para que se muestre la gráficas combinadas

plt.subplot(2, 2, 1) #para que se muestre la gráfica en la posición 1
plt.plot(anos, nivel5, label='Nivel 5', color = 'purple', marker = '<', linestyle = '-') #label es para que se muestre la leyenda y color es para que se muestre de color morado y marker es para que se muestre el marcador de la gráfica y linestyle es para que se muestre la línea de la gráfica
plt.legend() #para que se muestre la leyenda
# Título de la gráfica
plt.title('Resultados en los últimos 10 años que se ha realizado el examen')
# Etiquetas de los ejes
plt.xlabel('Años')
plt.ylabel('Puntaje')
plt.grid(True) #para que se muestre la cuadrícula
#Personalizar los ejes
plt.axis([0, 10, 0, 600]) #para que se muestre el eje x de 0 a 10 y el eje y de 0 a 600
#Activar marcas menores
plt.yticks(np.arange(0, 1001, 50)) #para que se muestre el eje y de 0 a 1000 con saltos de 50
plt.minorticks_on()
plt.show() #para que se muestre la gráfica