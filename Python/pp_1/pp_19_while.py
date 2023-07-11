#ciclo while
#while condición:
#    bloque de código

#ejemplo 1
print('ejemplo 1')
i = 0
while i < 10:
    i += 1
    print(i)
print(' ')
print('xxxxxxxxxxxxxxxxxx')
print(' ')
print('ejemplo 2')
#ejemplo 2
e = 0
while e < 20:
    e += 2
    if e == 16:
        break #rompe el ciclo y sale del while
    print(e)
print(' ')
print('xxxxxxxxxxxxxxxxxx')
print(' ')
print('ejemplo 3')
#ejemplo 3
r = 0
while r < 20:
    r += 2
    if r < 16:
        continue #rompe la iteración y continua con el while
    print(r)