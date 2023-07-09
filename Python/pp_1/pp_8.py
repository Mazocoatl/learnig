#python puede cambiar el tipo de la variable de manera dinamica
name = "Jair"
print(type(name))
name = 12
print(type(name))
name = True
print(type(name))

#Solo se puede concatenar o hacer operaciones con el mismo tipo de datos
print("Me llamo " + "Jair")
print(10 + 12)
print("Jair " + "12")
"""Si la intrusccion anterior la escribiera
sin comillas en el 12, el programa me daria un error"""

#para cambiar el tipo de dato a string se agrega antes del valor 'str'
age = 29
print(type(age))
print("Mi edad es de " + str(age))
print(f"Mi edad es {age}")
print(type(str(age)))

#para cambiar un string a numero se agrega antes 'int'
age = input('Escribe tu edad ')
print(type(age))
age = int(age)
print(type(int(age)))
age += 10
print(f'En 10 anos tu edad sera de {age}')