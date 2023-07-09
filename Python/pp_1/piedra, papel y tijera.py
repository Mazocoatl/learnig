user_option = input('piedra, papel o tijera? ')
pc_option = 'tijera'

if user_option == pc_option:
  print('¡Empate!')
elif user_option == 'piedra':
  if pc_option == 'tijera':
    print('¡User win!')
  else:
    print('¡User lose!')