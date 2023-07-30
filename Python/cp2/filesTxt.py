file = open('./text.txt')
# print(file.read()) # Lee todo el contenido del archivo
print('-------------------')
# print(file.readline()) # Lee la primera linea del archivo
# print(file.readline()) # Lee la segunda linea del archivo
# print(file.readline()) # Lee la tercera linea del archivo
# print(file.readline()) # Lee la cuarta linea del archivo
# for line in file: # Itera sobre las lineas del archivo
#   print(line)
# file.close() # Cierra el archivo
#la mejor for manera de abrir un archivo es con with
with open('./text.txt') as file: # Abre el archivo en modo lectura
 for line in file:
    print(line)
