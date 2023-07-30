#funciones
print('hola')

def my_print(texto):
    print(texto*2)

my_print('Hola ')

print('suma normal')
a = 5
b = 6
c = a + b
print(c)

def suma(a,b):
    c = a + b
    return c
print(suma(5,6))

def suma(a,b):
    return a + b
print(suma(5,6))

def suma(a,b):
    my_print(a + b)
suma(5,6)
