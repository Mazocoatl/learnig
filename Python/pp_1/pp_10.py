#operadores de comparación
print("Comparadores")
print(" ")
print("Mayor que '>'") #devuelve true si el valor de la izquierda es mayor que el de la derecha
print('5 > 6', 5 > 6)
print('5 > 4', 5 > 4)
print('5 > 5', 5 > 5)

print(" ")
print("*" * 20)
print(" ")

print("Menor que '<'") #devuelve true si el valor de la izquierda es menor que el de la derecha
print('5 < 6', 5 < 6)
print('5 < 4', 5 < 4)
print('5 < 5', 5 < 5)

print(" ")
print("*" * 20)
print(" ")

print("Mayor o igual que '>='") #devuelve true si el valor de la izquierda es mayor o igual que el de la derecha
print('5 >= 6', 5 >= 6)
print('5 >= 4', 5 >= 4)
print('5 >= 5', 5 >= 5)

print(" ")
print("*" * 20)
print(" ")

print("Menor que '<='") #devuelve true si el valor de la izquierda es menor o igual que el de la derecha
print('5 <= 6', 5 <= 6)
print('5 <= 4', 5 <= 4)
print('5 <= 5', 5 <= 5)

print(" ")
print("*" * 20)
print(" ")

print("Igual que '=='") #devuelve true si el valor de la izquierda es igual que el de la derecha
print('5 == 6', 5 == 6)
print('5 == 4', 5 == 4)
print('5 == 5', 5 == 5)

print(" ")
print("*" * 20)
print(" ")

print("Diferente que '!='") #devuelve true si el valor de la izquierda es diferente que el de la derecha
print('5 != 6', 5 != 6)
print('5 != 4', 5 != 4)
print('5 != 5', 5 != 5)

print(" ")
print("*" * 20)
print(" ")

"""En el caso de string se toma encuanta el largo de la palabra, así como las mayusculas o minúsculas. También no se pueden comparar tipos de datos diferentes"""
print("Comparación en strings")
print("Apple == Apple", "Apple" == 'Apple')
print("Apple == Apple", "Apple" == 'apple')
print("Jair >= Jesus", "Jair" >= "Jesus")
print("Jair <= Jesus", "Jair" <= "Jesus")
print("1" == 1)

print(" ")
print("*" * 20)
print(" ")

age = 15
print(age >= 18)
age = 20
print(age >= 18)