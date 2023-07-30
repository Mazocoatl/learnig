def sum_range(a, b):
    sum = 0
    for x in range(a, b):
        sum += x
    return sum
result = sum_range(1, 10)
print(result)
result_2 = sum_range(result, 100)
print(result_2)
print(sum_range(result_2, result_2 + 1000))

def volum(a = 5, b = 6, c = 7):
    return a * b * c, b , 'hola' 
result3, b, text = volum(b = 10)
print(result3)
print(b)
print(text)

#funciones lambda (anónimas) son funciones que no tienen nombre y se pueden usar en una sola linea de código y no se pueden reutilizar
def suma(a,b):
    return a + b
print(suma(5,6))

suma = lambda a,b: a + b
print(suma(5,6))

#funciones recursivas
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))

#funciones recursivas
def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(5))

#funciones con número variable de argumentos
def suma(*args):
    sum = 0
    for x in args:
        sum += x
    return sum
print(sum_range(1, 10))

def suma(*args):
    return sum(args)
print(sum_range(1, 10))

#high order functions (funciones de alto nivel) son funciones que reciben como parámetro otra función
def suma(a,b):
    return a + b
def resta(a,b):
    return a - b
def operacion(func,a,b):
    return func(a,b)
print(operacion(suma,5,6)) 
print(operacion(resta,5,6))

def incrementar(x):
    return x + 1
lista = [1,2,3,4,5]
lista2 = map(incrementar,lista)
print(list(lista2))


def increment(x): 
    return x + 1
increment_v2 = lambda x: x + 2 

def high_order(x, func):
    return x + func(x)
high_order_v2 = lambda x, func: (x + func(x))*2

result = high_order(2, increment)
print(result)
result = high_order_v2(2, increment_v2)
print(result)
result = high_order(2, lambda x: x + 3)
print(result)
result = high_order_v2(2, lambda x: x + 3)
print(result)
result = high_order(2, lambda x: x * 5)
print(result)
result = high_order_v2(2, lambda x: x * 5)
print(result)

#funciones map
def cuadrado(x):
    return x * x
lista = [1,2,3,4,5]
lista2 = map(cuadrado,lista) #map aplica la función a cada elemento de la lista
print(list(lista))
print(list(lista2))
lista3 = map(lambda x: x * x,lista) #map aplica la función a cada elemento de la lista
print(list(lista3))
list4 = [x * x for x in lista] #list comprehension
print(list4)
list5 = list(map(lambda x, y : x + y, lista, list4))
print(list5)

#map con diccionarios
diccionario = {'a':1,'b':2,'c':3,'d':4,'e':5}
diccionario2 = {k:v*v for (k,v) in diccionario.items()}
print(diccionario2)

#map diccionarios
items = [
    {'title': 'Item 1', 'price': 10},
    {'title': 'Item 2', 'price': 20},
    {'title': 'Item 3', 'price': 30},
    {'title': 'Item 4', 'price': 40},
]
prices = list(map(lambda item: item['price'], items))
print(prices)
def add_taxes(items):
    new_item = items.copy() #copy() crea una copia del diccionario
    new_item['taxes'] = new_item['price'] * 0.19
    return new_item
new_items = list(map(add_taxes, items))
print('New items:')
print(new_items)
print('Old items:')
print(items)

#funciones filter
def es_par(x):
    return x % 2 == 0
lista = [1,2,3,4,5]
lista2 = filter(es_par,lista) #filter filtra los elementos de la lista que cumplen la condición
print(list(lista2))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
new_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(new_numbers)

#filter con diccionarios
matches = [
    {
    'home_team': 'Bolivia',
    'away_team': 'Uruguay',
    'home_team_score': 3,
    'away_team_score': 1,
    'home_team_result': 'Win'
  },
  {
    'home_team': 'Brazil',
    'away_team': 'Mexico',
    'home_team_score': 1,
    'away_team_score': 1,
    'home_team_result': 'Draw'
  },
  {
    'home_team': 'Ecuador',
    'away_team': 'Venezuela',
    'home_team_score': 5,
    'away_team_score': 0,
    'home_team_result': 'Win'
  },
]
new_matches = list(filter(lambda x: x['home_team_result'] == 'Win', matches))
print(matches)
print(len(matches))
print(new_matches)
print(len(new_matches))

#funciones reduce
from functools import reduce
def suma(x,y):
    return x + y
lista = [1,2,3,4,5]
resultado = reduce(suma,lista) #reduce aplica la función a los elementos de la lista y devuelve un único valor
print(resultado)

numbers = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x + y, numbers)
print(result)

numbers = [1, 2, 3, 4, 5]
def accum(counter, x):
    print('counter +> ', counter)
    print('x +> ', x)
    return counter + x
result = reduce(accum, numbers, 0)  
print(result)

#reduce con diccionarios
matches = [
    {
    'home_team': 'Bolivia',
    'away_team': 'Uruguay',
    'home_team_score': 3,
    'away_team_score': 1,
    'home_team_result': 'Win'
    },
    {
    'home_team': 'Brazil',
    'away_team': 'Mexico',
    'home_team_score': 1,
    'away_team_score': 1,
    'home_team_result': 'Draw'
    },
    {
    'home_team': 'Ecuador',
    'away_team': 'Venezuela',
    'home_team_score': 5,
    'away_team_score': 0,
    'home_team_result': 'Win'
    },
]
total_home_team_score = reduce(lambda x, y: x + y['home_team_score'], matches, 0)
print(total_home_team_score)