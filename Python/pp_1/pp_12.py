#operadores lógicos
print('Operadores lógicos')
print(" ")

#AND devuelve True si ambos son True
print('AND')
print('True and True =>', True and True)
print('True and False =>', True and False)
print('False and True =>', False and True)
print('False and False =>', False and False)

print(' ')

print('5 >= 6 and 5 <= 6', 5 >= 6 and 5 <= 6)
print('5 >= 4 and 5 <= 4', 5 >= 4 and 5 <= 4)
print('5 >= 5 and 5 <= 5', 5 >= 5 and 5 <= 5)

print(' ')

#Ejemplo para llenar mi inventario  no puedo recibir menos de 100 piezas pero no mas de 1000
stock = input("Ingrese número de stock => ")
stock = int(stock)
print(stock >= 100 and stock <= 1000)

print(" ")
print("*" * 20)
print(" ")

#OR devuelve TRUE si alguno de los dos operadores es True
print('OR')
print('True or True =>', True or True)
print('True or False =>', True or False)
print('False or True =>', False or True)
print('False or False =>', False or False)

print(' ')

print('5 >= 6 or 5 <= 6', 5 >= 6 or 5 <= 6)
print('5 >= 4 or 5 <= 4', 5 >= 4 or 5 <= 4)
print('5 >= 5 or 5 <= 5', 5 >= 5 or 5 <= 5)
print('5 >= 6 or 5 <= 4', 5 >= 6 or 5 <= 4)

print(' ')

#Ejemplo pregunta del tipo del roll
roll = input('Digita el rol = ')
print(roll == 'admin' or roll == "seller")

print(" ")
print("*" * 20)
print(" ")

#NOT niega la operacion boolean 
print('NOT')
print("Not True =>", not True)
print("Not False =>", not False)

print(' ')

print('Not (True or True) =>', not(True or True))
print('Not (True or False) =>', not(True or False))
print('Not (False or True) =>', not(False or True))
print('Not (False or False) =>', not(False or False))

print(' ')

print('Not (5 >= 6 or 5 <= 6)', not(5 >= 6 or 5 <= 6))
print('Not (5 >= 4 or 5 <= 4)', not(5 >= 4 or 5 <= 4))
print('Not (5 >= 5 or 5 <= 5)', not(5 >= 5 or 5 <= 5))
print('Not (5 >= 6 or 5 <= 4)', not(5 >= 6 or 5 <= 4))

print(' ')

#Ejemplo para llenar mi inventario  no puedo recibir menos de 100 piezas pero no mas de 1000, este ejercicio se negara
stock = input("Ingrese número de stock => ")
stock = int(stock)
print(not(stock >= 100 and stock <= 1000))