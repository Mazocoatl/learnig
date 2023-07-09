#Condicionales
if True:
  print('Se debería de escribir')

if False:
  print('No se debería de escribir')

print(" ")
print("*" * 20)
print(" ")

#ejemplo
pet = input('Cual es tu mascota favorita? ')

if pet == 'perro':
  print('Excelente')
elif pet == 'gato':
  print('Me gusta')
elif pet == 'pez':
  print('Es normal')
else:
  print('Ok')

print(" ")
print("*" * 20)
print(" ")

stock = int(input('Digita el stock: '))

if stock <= 100:
  print('El stock es correcto')
else:
  print('El stock es incorrecto')