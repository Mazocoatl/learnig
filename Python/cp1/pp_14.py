texto = "Ella sabe programar en Python"
#operador in devuelve True o False si el elemento se encuentra en el texto
print('JavaScrip' in texto)
print('Python' in texto)

if 'Js' in texto:
    print('Esa palabra si se encuentra en el texto')
else:
    print('Esa palabra no se encuentra en el texto')

#operador not in devuelve True o False si el elemento no se encuentra en el texto
print('JavaScrip' not in texto)
print('Python' not in texto)

if 'Js' not in texto:
    print('Esa palabra no se encuentra en el texto')
else:
    print('Esa palabra si se encuentra en el texto')

#operador is devuelve True o False si el elemento es igual al texto
print('JavaScrip' is texto)
print('Python' is texto)

if 'Js' is texto:
    print('Esa palabra si se encuentra en el texto')
else:
    print('Esa palabra no se encuentra en el texto')

#operador is not devuelve True o False si el elemento no es igual al texto
print('JavaScrip' is not texto)
print('Python' is not texto)

if 'Js' is not texto:
    print('Esa palabra no se encuentra en el texto')
else:
    print('Esa palabra si se encuentra en el texto')

#size de un texto len() devuelve el tamaño del texto incluyendo espacios en blanco y caracteres especiales
size = len(texto)
print(size)

#upper() convierte el texto a mayúsculas
print(texto.upper())

#lower() convierte el texto a minúsculas
print(texto.lower())

#capitalize() convierte la primera letra del texto a mayúscula
print(texto.capitalize())

#title() convierte la primera letra de cada palabra del texto a mayúscula
print(texto.title())

#swapcase() convierte las mayúsculas a minúsculas y viceversa
print(texto.swapcase())

#replace() reemplaza una palabra por otra
print(texto.replace('Python', 'Java'))

#count() cuenta cuantas veces se repite una palabra en el texto o una letra
print(texto.count('Python'))
print(texto.count('a'))

#find() devuelve la posición de la primera letra de la palabra en el texto
print(texto.find('Python'))

#startswith() devuelve True o False si el texto empieza con la palabra
print(texto.startswith('Ella'))

#endswith() devuelve True o False si el texto termina con la palabra
print(texto.endswith('Python'))

#split() devuelve una lista con las palabras del texto
print(texto.split())

#join() convierte una lista en un texto
print(' '.join(texto.split()))

#strip() elimina los espacios en blanco al inicio y al final del texto
print(texto.strip())

#lstrip() elimina los espacios en blanco al inicio del texto
print(texto.lstrip())

#rstrip() elimina los espacios en blanco al final del texto
print(texto.rstrip())

#isalnum() devuelve True o False si el texto es alfanumérico
print(texto.isalnum())

#isalpha() devuelve True o False si el texto es alfabético
print(texto.isalpha())

#isdigit() devuelve True o False si el texto es numérico
print(texto.isdigit())

#islower() devuelve True o False si el texto es minúsculas
print(texto.islower())

#isupper() devuelve True o False si el texto es mayúsculas
print(texto.isupper())

#istitle() devuelve True o False si el texto es título
print(texto.istitle())

#isspace() devuelve True o False si el texto es espacios en blanco
print(texto.isspace())


#isprintable() devuelve True o False si el texto es imprimible
print(texto.isprintable())

#isidentifier() devuelve True o False si el texto es un identificador
print(texto.isidentifier())

#isdecimal() devuelve True o False si el texto es decimal
print(texto.isdecimal())

#isnumeric() devuelve True o False si el texto es numérico
print(texto.isnumeric())

#isascii() devuelve True o False si el texto es ascii
print(texto.isascii())

