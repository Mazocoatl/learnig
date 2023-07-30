with open('./text.txt', 'a') as file: # Abre el archivo en modo escritura
  file.write('\nHola desde Python') # Escribe una linea en el archivo

# with open('./text.txt', 'w') as file: # Abre el archivo en modo escritura (sobreescribe el contenido)
#   file.write('Hola desde Python') # Escribe una linea en el archivo
'''
with open('./text.txt', 'r+') as file: # Abre el archivo en modo lectura y escritura (no sobreescribe el contenido)
    file.write('\nHola desde Python') # Escribe una linea en el archivo
    file.seek(0) # Mueve el cursor al inicio del archivo
    print(file.read()) # Lee todo el contenido del archivo
'''
# with open('./text.txt', 'rb') as file: # Abre el archivo en modo lectura binaria (no sobreescribe el contenido)
#     print(file.read()) # Lee todo el contenido del archivo

# with open('./text.txt', 'wb') as file: # Abre el archivo en modo escritura binaria (sobreescribe el contenido)
#     file.write(b'Hola desde Python') # Escribe una linea en el archivo

# with open('./text.txt', 'r+b') as file: # Abre el archivo en modo lectura y escritura binaria (no sobreescribe el contenido)
#     file.write(b'Hola desde Python') # Escribe una linea en el archivo
#     file.seek(0) # Mueve el cursor al inicio del archivo
#     print(file.read()) # Lee todo el contenido del archivo

# with open('./text.txt', 'a+b') as file: # Abre el archivo en modo lectura y escritura binaria (no sobreescribe el contenido)
#     file.write(b'Hola desde Python') # Escribe una linea en el archivo
#     file.seek(0) # Mueve el cursor al inicio del archivo
#     print(file.read()) # Lee todo el contenido del archivo

# with open('./text.txt', 'ab') as file: # Abre el archivo en modo escritura binaria (no sobreescribe el contenido)
#     file.write(b'Hola desde Python') # Escribe una linea en el archivo

# with open('./text.txt', 'w+') as file: # Abre el archivo en modo lectura y escritura (sobreescribe el contenido)
#     file.write('Hola desde Python') # Escribe una linea en el archivo
#     file.seek(0) # Mueve el cursor al inicio del archivo
#     print(file.read()) # Lee todo el contenido del archivo

# with open('./text.txt', 'a+') as file: # Abre el archivo en modo lectura y escritura (no sobreescribe el contenido)
#     file.write('\nHola desde Python') # Escribe una linea en el archivo
#     file.seek(0) # Mueve el cursor al inicio del archivo
#     print(file.read()) # Lee todo el contenido del archivo

#modificar una linea en un archivo
with open('./text.txt', 'r+') as file: # Abre el archivo en modo lectura y escritura (no sobreescribe el contenido)
    file.seek(0) # Mueve el cursor al inicio del archivo
    file.write('Hola desde Python') # Escribe una linea en el archivo
    file.seek(0) # Mueve el cursor al inicio del archivo
    print(file.read()) # Lee todo el contenido del archivo
