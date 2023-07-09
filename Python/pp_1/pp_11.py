#Comparar flotantes
print("Comparador de flotantes")
print(" ")

x = 3.3
print("x =",x,type(x))
y = 1.1 + 2.2
print("y =",y,type(y))
print('x = y', x == y)

print(" ")
print("*" * 20)
print(" ")

#Convertir a string 'x' y 'y' para comparar
#utilizamos la función format para cambiar el formato y elegir cuantops decimales queremos
y_str = format(y, ".2g")
print('str =>', y_str, type(y_str))
print('x = y', str(x) == y_str)

print(" ")
print("*" * 20)
print(" ")

#Elegir la tolerancia de exactitud de la operacion de floats
#Sacamos valores absolutos para la comparación de manera matemática
print("x =",x)
print("y =",y)
tolerance = 0.0001
print('x = y', abs(x - y) <= tolerance)

print(" ")
print("*" * 20)
print(" ")

#Otra forma de comparar floats es con la funcion 'round()' que me retorna un flotante y la cantidad de decimales qu eyo decida
print("x =",x)
print("y =",y)
print("Usando la función round => y =",round(y,1))
print('x = y', x == round(y,1))