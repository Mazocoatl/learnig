#tuplas son inmutables y no se pueden modificar

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 1)
string = ("hola", "mundo", "soy", "una", "tupla")

print(numbers)
print(type(numbers))
print(string)
print(type(string))

print('0 =>', numbers[0]) # imprime el primer elemento de la tupla
print('-1 =>', numbers[-1]) # imprime el ultimo elemento de la tupla
#numbers[0] = 1 # no se puede modificar una tupla

#en una tupla se puede buscar un elemento
print('1 in numbers =>', 1 in numbers)

#en una tupla se puede buscar la posicion de un elemento
print('numbers.index(1) =>', numbers.index(1))

#en una tupla se puede contar cuantas veces se repite un elemento
print('numbers.count(1) =>', numbers.count(1))

#en una tupla se puede saber cuantos elementos tiene
print('len(numbers) =>', len(numbers))

#en una tupla se puede saber cual es el elemento mas grande
print('max(numbers) =>', max(numbers))

#en una tupla se puede saber cual es el elemento mas pequeño
print('min(numbers) =>', min(numbers))

#una tupla se puede convertir en una lista
lnumbers = list(numbers)
print(lnumbers)
print(type(lnumbers))
lnumbers.append(10)
print(lnumbers)
lnumbers[0] = 0
print(lnumbers)

#una lista se puede convertir en una tupla
tlnumbers = tuple(lnumbers)
print(tlnumbers)
print(type(tlnumbers))