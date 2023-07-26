#indexing y slicing de cadenas
#Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.
#Ejemplo:
#>>> cuenta_vocales()
#Introduce una palabra: murcielago
#La vocal a aparece 1 veces
#La vocal e aparece 1 veces
#La vocal i aparece 1 veces
#La vocal o aparece 1 veces
#La vocal u aparece 1 veces
#def cuenta_vocales():
palabra = input('Introduce una palabra: ')
vocales = ['a', 'e', 'i', 'o', 'u']
for vocal in vocales:
    n = 0
    for letra in palabra:
        if letra == vocal:
            n += 1
    print('La vocal ' + vocal + ' aparece ' + str(n) + ' veces')
#indexing para cadenas de caracteres y listas de caracteres (strings y listas)
texto = 'Ella sabe Python'
print(texto)
print(texto[0])
print(texto[1])
print(texto[2])
print(texto[3])

size = len(texto)
print('size del texto => ',size)
print(texto[size-1])
print(texto[-1])
print(texto[-2])
print(texto[-3])

#slicing
print(texto[0:5])
print(texto[5:9])
print(texto[10:16])
print(texto[10:-1])
print(texto[10:])
print(texto[:9])
print(texto[:])
print(texto[::2])
print(texto[::-1])
print(texto[::-2])
print(texto[10:16:1])
print(texto[10:16:2])