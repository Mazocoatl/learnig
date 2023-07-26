name = "Jair"
lastname = "Varela Vázquez"

#Concatenar
fullname = name + " " + lastname
print(fullname)

"""Dependiendo de la frase o lo que se escribe manejaremos la comilla sencilla o la doble"""
print("I'm Jair")

print('She say "Hello"')

template = "Hola, mi nombre es " + name + " y mis apellidos son " + lastname
print("v1",template)

template = "Hola, yo soy {} y mi apellido es {}".format(name,lastname)
print("v2",template)

template = f"Hola, mi nombre es {name} y mi apellido es {lastname}"
print("v3",template)