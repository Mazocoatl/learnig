import random

options = ('piedra', 'papel', 'tijera')
print('¡Bienvenido a piedra, papel o tijera!')

user_option = input('¿Qué eliges piedra, papel o tijera? ')
user_option = user_option.lower()
while user_option not in options:
  print('¡Opción no válida!')
  user_option = input('¿Qué eliges piedra, papel o tijera? ')
  user_option = user_option.lower()

pc_option = random.choice(options)
print('El usuario eligió: ' + user_option)
print('La pc eligió: ' + pc_option)

if user_option == pc_option:
  print('¡Empate!')
elif user_option == 'piedra':
  if pc_option == 'tijera':
    print('¡Piedra le gana a tijera!')
    print('¡User win!')
  else:
    print('¡Papel le gana a piedra!')
    print('¡PC win!')
elif user_option == 'papel':
  if pc_option == 'piedra':
    print('¡Papel le gana a piedra!')
    print('¡User win!')
  else:
    print('¡Tijera le gana a papel!')
    print('¡PC win!')
elif user_option == 'tijera':
  if pc_option == 'papel':
    print('¡Tijera le gana a papel!')
    print('¡User win!')
  else:
    print('¡Piedra le gana a tijera!')
    print('¡PC win!')