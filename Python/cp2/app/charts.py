import matplotlib.pyplot as plt

def generate_bar_chart(labels, values): # genera un gráfico de barras
    fig, ax = plt.subplots() # crea una figura y un conjunto de ejes
    ax.bar(labels, values) # crea un gráfico de barras
    plt.show() # muestra el gráfico

def generate_pie_chart(labels, values): # genera un gráfico de torta
    fig, ax = plt.subplots() # crea una figura y un conjunto de ejes
    ax.pie(values, labels=labels) # crea un gráfico de torta
    ax.axis('equal') # hace que el gráfico de torta sea circular
    plt.show() # muestra el gráfico

if __name__ == '__main__':
    labels = ['A', 'B', 'C']
    values = [1, 4, 2]
    generate_bar_chart(labels, values)
    generate_pie_chart(labels, values)