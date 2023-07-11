#las listas son un tipo de dato que permite almacenar varios valores y tipos de datos
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#imprime la lista
print(numbers)
#imprime el tipo de dato
print(type(numbers))

tasks = ['tarea 1', 'tarea 2', 'tarea 3']
print(tasks)

types = [1, 'hola', 2.5, True]
print(types)

#imprime el primer elemento de la lista
print(numbers[0])
print(tasks[0])
print(types[0])
#imprime el ultimo elemento de la lista
print(numbers[-1])
print(tasks[-1])
print(types[-1])

#imprime el rango de elementos de la lista
print(numbers[0:3])
print(tasks[0:3])
print(types[0:3])

#modifica el valor de un elemento de la lista
numbers[0] = 10
print(numbers)
tasks[0] = 'tarea 4'
print(tasks)
types[0] = False
print(types)

#agrega un elemento a la lista al final
numbers.append(10)
print(numbers)
tasks.append('tarea 5')
print(tasks)
types.append(False)
print(types)

#agrega un elemento a la lista en una posición especifica
numbers.insert(3, 0)
print(numbers)
tasks.insert(0, 'tarea 0')
print(tasks)
types.insert(0, True)
print(types)

#elimina un elemento de la lista
numbers.pop(0)
print(numbers)
tasks.pop(0)
print(tasks)
types.pop(0)
print(types)

#elimina un elemento de la lista por su valor
numbers.remove(10)
print(numbers)
tasks.remove('tarea 5')
print(tasks)
types.remove(False)
print(types)

#imprime la longitud de la lista
print(len(numbers))
print(len(tasks))
print(len(types))

#imprime la lista en orden inverso
numbers.reverse()
print(numbers)
tasks.reverse()
print(tasks)
types.reverse()
print(types)

#imprime la lista ordenada
numbers.sort()
print(numbers)
tasks.sort()
print(tasks)
#no se puede ordenar una lista con diferentes tipos de datos
#types.sort()
#print(types)

#imprime la lista ordenada en orden inverso
numbers.sort(reverse=True)
print(numbers)
tasks.sort(reverse=True)
print(tasks)

#imprime la lista ordenada temporalmente
print(sorted(numbers))
print(sorted(tasks))

#imprime la lista ordenada temporalmente en orden inverso
print(sorted(numbers, reverse=True))
print(sorted(tasks, reverse=True))

#imprime si un elemento esta en la lista
print(1 in numbers)
print('tarea 1' in tasks)
print(1 in types)

#imprime si un elemento no esta en la lista
print(1 not in numbers)
print('tarea 1' not in tasks)
print(1 not in types)

#imprime la lista en forma de cadena
print(str(numbers))
print(str(tasks))
print(str(types))

#uniendo listas
numbers2 = [10, 11, 12, 13, 14, 15]
print(numbers + numbers2)
tasks2 = ['tarea 6', 'tarea 7', 'tarea 8']
print(tasks + tasks2)
types2 = [False, True, False]
print(types + types2)

new_list = numbers + numbers2
print(new_list)

#encontrar el indice de un elemento
print(new_list.index(10))
print(new_list.index(11))
print(new_list.index(12))

#contar cuantas veces se repite un elemento
print(new_list.count(10))
print(new_list.count(11))
print(new_list.count(12))