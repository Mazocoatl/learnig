#ciclos anidados
matriz = [[1,2,3],
          [4,5,6],
          [7,8,9]
          ]
print(matriz)
print(matriz[0]) #imprime la primera fila
print(matriz[0][0]) #imprime el primer elemento de la primera fila
print(matriz[0][1]) #imprime el segundo elemento de la primera fila
print('-----------------------')
for fila in matriz:
    print(fila)
    for elemento in fila:
        print(elemento)
print('-----------------------')