# diccionario = {llave:valor for valor in iterable}
dic_v1 = {}
for number in range(1, 11):
    dic_v1[number] = number * 2
print(dic_v1)

dic_v2 = {number: number * 2 for number in range(1, 11)}
print(dic_v2)

import random
countries = ['Colombia', 'México', 'Perú', 'Argentina', 'Brasil', 'Chile']
population = {}
for country in countries:
    population[country] = random.randint(10000, 1000000)
print(population)

population = {country: random.randint(10000, 1000000) for country in countries}

names = ['Juan', 'Karla', 'Pedro', 'Miguel', 'María', 'Laura', 'Andrés', 'Diana']
ages = {12, 34, 22, 18, 17, 32, 21, 24}
print(list(zip(names, ages)))

students = {name: age for name, age in zip(names, ages)}
print(students)

# diccionario con condición = {llave:valor for llave, valor in iterable if condición}
import random
countries = ['Colombia', 'México', 'Perú', 'Argentina', 'Brasil', 'Chile']
population_v2 = {countries: random.randint(10000, 1000000) for countries in countries}
print(population)

result_1 = {country: 'Grande' if population >= 500000 else 'Pequeño' for country, population in population.items()}
print(result_1)

result_2 = {country: population for country, population in population.items() if population >= 500000}
print(result_2)

result_3 = {country: population for country, population in population.items() if population < 500000}
print(result_3)

text = 'Hola, soy Carlos'
unique = {c: c.upper() for c in text if not c.isspace()}
print(unique)

unique2 = {c: c.upper() for c in text if c in 'aeiou'}
print(unique2)
