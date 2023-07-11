import random
import os
l = True

opciones = ('piedra', 'papel', 'tijera')
def clear():
    if turnos != 0:
        os.system('pause')
    os.system('cls' if os.name == 'nt' else 'clear')
def tur():
    sg=True
    while sg:
        turnos = input('¿Cuantos turnos quieres jugar? ')
        if turnos.isdigit() and int(turnos) > 0:
            sg=False
        else:
            print('Ingresa un numero valido mayor a 0')
    return int(turnos)
while l:
    u, c, e, t = 0, 0, 0, 0
    print('Bienvenido a piedra, papel o tijera')
    turnos = tur()
    while turnos > 0:
        clear()
        print('1.- Piedra 🪨 | 2.- Papel 🗞️ | 3.- Tijera ✂️')
        print(f'Puntuación: | Usuario: {u} | PC: {c} | Empates: {e} | Turnos: {turnos} |')
        pc_option = random.choice(opciones)
        user = input('Ingresa tu opción: ')
        user = user.lower()
        if len(user)>0 and user in opciones or len(user)>0 and int(user) <= len(opciones)and int(user)>0:
            if user.isdigit():
                user=opciones[int(user)-1]
            print(f'PC: {pc_option}  VS Usuario: {user}')
            if pc_option != user:
                if (pc_option == 'piedra' and user == 'papel') or (pc_option == 'papel' and user == 'tijera') or (pc_option == 'tijera' and user == 'piedra'):
                    print('Ganaste')
                    u += 1
                    turnos -= 1
                else:
                    print('Perdiste')
                    c += 1
                    turnos -= 1
            else:
                print('Empate')
                e += 1
                turnos -= 1
        else:
            print('Ingresa una opción valida')
    clear()
    print(f'Puntuación: | Usuario: {u} | PC: {c} | Empates: {e} |')
    if u > c:
        print('🏆🥇🎉🎊¡Ganaste!🎊🎉🥇🏆')
    elif u < c:
        print('💀🤣😂👎Perdiste👎😂🤣💀')
    else:
        print('Empate')
    l = input('¿Quieres volver a jugar? (s/n) ').lower()
    if l == 's':
        l = True
    else:
        l = False
clear()
print('Gracias por jugar')
