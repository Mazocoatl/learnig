#ciclo For (para)
# for variable en elemento iterable:
#     instrucciones

#ejemplo 1
print('ejemplo 1')
for i in range(10):
    print(i)
print(' ')
print('xxxxxxxxxxxxxxxxxx')
print(' ')
print('ejemplo 2')
#ejemplo 2
for e in range(1, 20):
    print(e)
print(' ')
print('xxxxxxxxxxxxxxxxxx')
print(' ')
print('ejemplo 3')
#ejemplo 3
for r in range(0, 20, 2):
    print(r)
print(' ')
print('xxxxxxxxxxxxxxxxxx')
print(' ')
print('ejemplo 4 con lista')
#ejemplo 4
my_list = [23, 45, 67, 89, 12, 34, 56, 78, 90]
for i in my_list:
    print(i)
print(' ')
print('xxxxxxxxxxxxxxxxxx')
print(' ')
print('ejemplo 5 con tupla')
#ejemplo 5
my_tuple = ('Pedro', 'Juan', 'Diego', 'Luis', 'Carlos')
for i in my_tuple:
    print(i)
print(' ')
print('xxxxxxxxxxxxxxxxxx')
print(' ')
print('ejemplo 6 con diccionario')
#ejemplo 6
my_dict = {
    'name': 'Pedro',
    'age': 23,
    'country': 'MX'
}
for i in my_dict:
    print(i, '=>', my_dict[i])
print(' ')
for i, value in my_dict.items():
    print(i, '=>', value)
print(' ')
print('xxxxxxxxxxxxxxxxxx')
print(' ')
print('ejemplo 7 con cadena')
#ejemplo 7
my_string = 'Hola mundo'
for i in my_string:
    print(i)
print(' ')
print('xxxxxxxxxxxxxxxxxx')
print(' ')
print('ejemplo 8 con break')
#ejemplo 8
for i in range(10):
    if i == 5:
        break
    print(i)
print(' ')
print('xxxxxxxxxxxxxxxxxx')
print(' ')
print('ejemplo 9 con continue')
#ejemplo 9
for i in range(10):
    if i < 5:
        continue
    print(i)
print(' ')
print('xxxxxxxxxxxxxxxxxx')
print(' ')
print('ejemplo 10 con else')
#ejemplo 10
for i in range(10):
    print(i)
else:
    print('Fin del ciclo for')
print(' ')
print('xxxxxxxxxxxxxxxxxx')
print(' ')
print('ejemplo 11 con else y break')
#ejemplo 11
for i in range(10):
    if i == 5:
        break
    print(i)
else:
    print('Fin del ciclo for')
print(' ')
print('xxxxxxxxxxxxxxxxxx')
print(' ')
print('ejemplo 12 con else y continue')
#ejemplo 12
for i in range(10):
    if i < 5:
        continue
    print(i)
else:
    print('Fin del ciclo for')
print(' ')
print('xxxxxxxxxxxxxxxxxx')
print(' ')
print('listas con varios diccionarios')
#listas con varios diccionarios
my_list = [
    {
        'name': 'Pedro',
        'age': 23,
        'country': 'MX'
    },
    {
        'name': 'Juan',
        'age': 34,
        'country': 'MX'
    },
    {
        'name': 'Diego',
        'age': 45,
        'country': 'MX'
    },
    {
        'name': 'Luis',
        'age': 56,
        'country': 'MX'
    },
]
for name in my_list:
    print(name)
print(' ')
for name in my_list:
    print(name['name'], '=>', name['age'])
print(' ')
for name in my_list:
    for key, value in name.items():
        print(key, '=>', value)
print(' ')
print('xxxxxxxxxxxxxxxxxx')
print(' ')
print('listas con varios diccionarios y break')
#listas con varios diccionarios y break
for name in my_list:
    if name['name'] == 'Diego':
        break
    print(name['name'], '=>', name['age'])
print(' ')
print('xxxxxxxxxxxxxxxxxx')
print(' ')
print('listas con varios diccionarios y continue')
#listas con varios diccionarios y continue
for name in my_list:
    if name['name'] == 'Diego':
        continue
    print(name['name'], '=>', name['age'])
print(' ')
print('xxxxxxxxxxxxxxxxxx')
print(' ')
print('listas con varios diccionarios y else')
#listas con varios diccionarios y else
for name in my_list:
    print(name['name'], '=>', name['age'])
else:
    print('Fin del ciclo for')
print(' ')
print('xxxxxxxxxxxxxxxxxx')
print(' ')
print('listas con varios diccionarios y else y break')
#listas con varios diccionarios y else y break
for name in my_list:
    if name['name'] == 'Diego':
        break
    print(name['name'], '=>', name['age'])
else:
    print('Fin del ciclo for')
print(' ')
print('xxxxxxxxxxxxxxxxxx')
print(' ')
print('listas con varios diccionarios y else y continue')
#listas con varios diccionarios y else y continue
for name in my_list:
    if name['name'] == 'Diego':
        continue
    print(name['name'], '=>', name['age'])
else:
    print('Fin del ciclo for')
