#conjuntos en python
#conjuntos: son colecciones desordenadas de elementos únicos
#se usan para hacer pruebas de pertenencia a grupos y eliminacion de elementos duplicados
#se pueden crear usando la funcion set() o usando llaves {}
#los conjuntos no soportan indexacion, ni slicing
#los conjuntos no soportan elementos mutables
#los conjuntos soportan operaciones matematicas como union, interseccion, diferencia y diferencia simetrica
#los conjuntos soportan operaciones de pertenencia como in y not in
#los conjuntos soportan operaciones de comparacion como ==, !=, <, >, <=, >=
#los conjuntos soportan operaciones de agregacion como len(), min(), max(), sum()
#los conjuntos soportan operaciones de agregacion como all(), any(), enumerate(), sorted(), zip()
#los conjuntos soportan operaciones de agregacion como del(), copy(), clear(), remove(), discard(), pop(), update(), add()
#los conjuntos soportan operaciones de agregacion como isdisjoint(), issubset(), issuperset(), union(), intersection(), difference(), symmetric_difference()
#los conjuntos soportan operaciones de agregacion como union_update(), intersection_update(), difference_update(), symmetric_difference_update()
#los conjuntos soportan operaciones de agregacion como copy(), isdisjoint(), issubset(), issuperset(), union(), intersection(), difference(), symmetric_difference()

#crear un conjunto
set_countries = {'col', 'mex', 'per', 'arg', 'bra', 'chi', 'uru', 'par', 'ecu', 'bol', 'ven', 'col'}
print(set_countries)
print(type(set_countries))
#crear un conjunto vacio
set_countries = set()
print(set_countries)
print(type(set_countries))

set_numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(set_numbers)
print(type(set_numbers))

set_types = {1, 2.0, 'three', (4, 5, 6), True}
print(set_types)
print(type(set_types))

#crear un conjunto a partir de una cadena
str_countries = 'colombia'
set_countries = set(str_countries)
print(str_countries)
print(type(str_countries))
print(set_countries)
print(type(set_countries))

#crear un conjunto a partir de una lista
list_countries = ['col', 'mex', 'per', 'arg', 'bra', 'chi', 'uru', 'par', 'ecu', 'bol', 'ven', 'col']
set_countries = set(list_countries)
print(list_countries)
print(type(list_countries))
print(set_countries)
print(type(set_countries))

#crear un conjunto a partir de una tupla
tuple_countries = ('col', 'mex', 'per', 'arg', 'bra', 'chi', 'uru', 'par', 'ecu', 'bol', 'ven', 'col')
set_countries = set(tuple_countries)
print(tuple_countries)
print(type(tuple_countries))
print(set_countries)
print(type(set_countries))

#crear un conjunto a partir de un diccionario
dict_countries = {'col': 'colombia', 'mex': 'mexico', 'per': 'peru', 'arg': 'argentina', 'bra': 'brasil', 'chi': 'chile', 'uru': 'uruguay', 'par': 'paraguay', 'ecu': 'ecuador', 'bol': 'bolivia', 'ven': 'venezuela'}
set_countries = set(dict_countries)
print(dict_countries)
print(type(dict_countries))
print(set_countries)
print(type(set_countries))

#crear un conjunto a partir de un rango
range_numbers = range(1, 10)
set_numbers = set(range_numbers)
print(range_numbers)
print(type(range_numbers))
print(set_numbers)
print(type(set_numbers))

#modificar un conjunto
set_countries = {'col', 'mex', 'per', 'arg', 'bra', 'chi', 'uru', 'par', 'ecu', 'bol', 'ven', 'col'}
print(set_countries)
set_countries.add('pan') #agregar un elemento
print(set_countries)
set_countries.update(['nic', 'hon', 'gua', 'els', 'cos']) #agregar varios elementos
print(set_countries)
set_countries.remove('cos') #eliminar un elemento
print(set_countries)
set_countries.discard('els') #eliminar un elemento
print(set_countries)
set_countries.pop() #eliminar un elemento
print(set_countries)
set_countries.clear() #eliminar todos los elementos
print(set_countries)

#eliminar un conjunto
set_countries = {'col', 'mex', 'per', 'arg', 'bra', 'chi', 'uru', 'par', 'ecu', 'bol', 'ven', 'col'}
print(set_countries)
del set_countries
#print(set_countries)

#tamaño de un conjunto
set_countries = {'col', 'mex', 'per', 'arg', 'bra', 'chi', 'uru', 'par', 'ecu', 'bol', 'ven', 'col'}
print(set_countries)
print(len(set_countries))

#iterar un conjunto
set_countries = {'col', 'mex', 'per', 'arg', 'bra', 'chi', 'uru', 'par', 'ecu', 'bol', 'ven', 'col'}
for country in set_countries:
    print(country)

#verificar si un elemento pertenece a un conjunto
set_countries = {'col', 'mex', 'per', 'arg', 'bra', 'chi', 'uru', 'par', 'ecu', 'bol', 'ven'}
print(set_countries)
print('col' in set_countries)
print('col' not in set_countries)

#operaciones con conjuntos
set_countries_a = {'col', 'mex', 'per', 'arg', 'bra', 'chi'}
set_countries_b = {'uru', 'par', 'ecu', 'bol', 'ven'}
print(set_countries_a)
print(set_countries_b)
print(set_countries_a.union(set_countries_b)) #union
print(set_countries_a.intersection(set_countries_b)) #intersección
print(set_countries_a.difference(set_countries_b)) #diferencia
print(set_countries_a.symmetric_difference(set_countries_b)) #diferencia simétrica

#operaciones con conjuntos
set_countries_a = {'col', 'mex', 'per', 'arg', 'bra', 'chi'}
set_countries_b = {'uru', 'par', 'ecu', 'bol', 'ven'}
print(set_countries_a)
print(set_countries_b)
print(set_countries_a.isdisjoint(set_countries_b)) #disjuntos
print(set_countries_a.issubset(set_countries_b)) #subconjunto
print(set_countries_a.issuperset(set_countries_b)) #superconjunto

#operaciones con conjuntos
set_countries_a = {'col', 'mex', 'per', 'arg', 'bra', 'chi'}
set_countries_b = {'uru', 'par', 'ecu', 'bol', 'ven'}
print(set_countries_a)
print(set_countries_b)
set_countries_a.update(set_countries_b) #union
print(set_countries_a)
set_countries_a.intersection_update(set_countries_b) #intersección
print(set_countries_a)
set_countries_a.difference_update(set_countries_b) #diferencia
print(set_countries_a)
set_countries_a.symmetric_difference_update(set_countries_b) #diferencia simétrica
print(set_countries_a)

#operaciones con conjuntos
set_countries_a = {'col', 'mex', 'per', 'arg', 'bra', 'chi'}
set_countries_b = {'uru', 'par', 'ecu', 'bol', 'ven'}
print(set_countries_a)
print(set_countries_b)
set_countries_a_copy = set_countries_a.copy() #copia
print(set_countries_a_copy)
set_countries_a_copy.clear() #limpiar
print(set_countries_a_copy)

#operaciones matematicas con conjuntos
set_countries_a = {'col', 'mex', 'per', 'arg', 'bra', 'chi'}
set_countries_b = {'uru', 'par', 'ecu', 'bol', 'ven'}
print(set_countries_a)
print(set_countries_b)
print(set_countries_a | set_countries_b) #union
print(set_countries_a & set_countries_b) #intersección
print(set_countries_a - set_countries_b) #diferencia
print(set_countries_a ^ set_countries_b) #diferencia simétrica