#crea una lista con los números del 1 al 100.
lista = []
i = 0
while i < 100:
    i = i + 1
    lista.append(i)
print(lista)
print(' ')
print('xxxxxxxxxxxxxxxxxx')
print(' ')
#Agrega solo los números pares del 1 al 100 a una lista.
lista_par = []
i = 0
while i < 100:
    i = i + 1
    if i % 2 == 0:
        lista_par.append(i)
print(lista_par)
print(' ')
print('xxxxxxxxxxxxxxxxxx')
print(' ')
#Agrega solo los números impares del 1 al 100 a una lista.
lista_imp = []
i = 0
while i < 100:
    i = i + 1
    if i % 2 != 0:
        lista_imp.append(i)
print(lista_imp)
print(' ')
print('xxxxxxxxxxxxxxxxxx')
print(' ')
#Agrega solo los números primos del 1 al 100 a una lista. usando while
lista_pri = []
i = 0
while i < 100:
    i = i + 1
    if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0:
        lista_pri.append(i)
lista_pri.insert(1, 2)
lista_pri.insert(2, 3)
lista_pri.insert(3, 5)
lista_pri.insert(4, 7)
print(lista_pri)
print(' ')
print('xxxxxxxxxxxxxxxxxx')
print(' ')
#utilizando for loop, itera a través de la lista de 1 al 100 e imprime solo los números pares y agrégalos a una lista.
lista_par2 = []
for i in lista:
    if i % 2 == 0:
        lista_par2.append(i)
print(lista_par2)
print(' ')
print('xxxxxxxxxxxxxxxxxx')
print(' ')
#utilizando for loop, itera a través de la lista de 1 al 100 e imprime solo los números impares y agrégalos a una lista.
lista_imp2 = []
for i in lista:
    if i % 2 != 0:
        lista_imp2.append(i)
print(lista_imp2)
print(' ')
print('xxxxxxxxxxxxxxxxxx')
print(' ')
#utilizando for loop, itera a través de la lista de 1 al 100 e imprime solo los números primos y agrégalos a una lista.
lista_pri2 = []
for i in lista:
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        lista_pri2.append(i)
print(lista_pri2)
print(' ')
print('xxxxxxxxxxxxxxxxxx')
print(' ')
#utilizando for loop, itera a través de la lista de 1 al 100 e imprime solo los números divisibles entre 5 y agrégalos a una lista.
lista_div5 = []
for i in lista:
    if i % 5 == 0:
        lista_div5.append(i)
print(lista_div5)
print(' ')
print('xxxxxxxxxxxxxxxxxx')
print(' ')
#crea una lista con los números del -100 al 100.
lista_neg = []
i = -100
while i < 100:
    i = i + 1
    lista_neg.append(i)
print(lista_neg)
print(' ')
print('xxxxxxxxxxxxxxxxxx')
print(' ')
#crea una lista con los números del -100 al 100 que sean pares positivos.
lista_par_pos = []
i = -100
while i < 100:
    i = i + 1
    if i % 2 == 0 and i > 0:
        lista_par_pos.append(i)
print(lista_par_pos)
print(' ')
print('xxxxxxxxxxxxxxxxxx')
print(' ')
#crea una lista con los números del -100 al 100 que sean pares negativos.
lista_par_neg = []
i = -100
while i < 100:
    i = i + 1
    if i % 2 == 0 and i < 0:
        lista_par_neg.append(i)
print(lista_par_neg)
print(' ')
print('xxxxxxxxxxxxxxxxxx')
print(' ')
#utilizando for loop, itera a través de la lista de -100 al 100 e imprime solo los números pares y agrégalos a una lista.
lista_par_pos2 = []
for i in lista_neg:
    if i % 2 == 0 and i > 0:
        lista_par_pos2.append(i)
print(lista_par_pos2)