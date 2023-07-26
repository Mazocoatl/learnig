#diccionarios
my_dict = {
    'David':35,
    'Erika':32,
    'Jaime':50,
    'Jair':21
    }

print(my_dict)
print(type(my_dict))

#imprimir un elemento del diccionario
print(my_dict['David'])
print(my_dict.get('David'))

#imprimir un elemento del diccionario que no existe
#print(my_dict['Pedro']) #error
print(my_dict.get('Pedro')) #no error

#agregar un elemento al diccionario
my_dict['Pedro'] = 70
print(my_dict)

#modificar un elemento del diccionario
my_dict['Pedro'] = 80
print(my_dict)

#eliminar un elemento del diccionario
del my_dict['Pedro']
print(my_dict)

#recorrer un diccionario
for llave in my_dict.keys():
    print(llave)

for valor in my_dict.values():
    print(valor)

for llave, valor in my_dict.items():
    print(llave, valor)

#buscar un elemento en el diccionario
print('David' in my_dict)
print('Pedro' in my_dict)

#buscar un elemento en el diccionario y si no existe agregarlo
print(my_dict.setdefault('David', 50))
print(my_dict.setdefault('Pedro', 50))
print(my_dict)

print(my_dict.pop('David'))
print(my_dict)

print ('items', my_dict.items())  #devuelve una lista de tuplas

print(my_dict.popitem()) #devuelve una tupla con el ultimo elemento del diccionario