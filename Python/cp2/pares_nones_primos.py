import pkg
print(pkg.URL)
opciones = int(input("¿Qué deseas hacer?\n1. Aritmética\n2. Saber si un número es primo, par o no\n3. Obtener una lista de números pares, impares, primos y no primos en un rango\n4. Salir\n"))
while opciones != 4:
    if opciones == 1:
        print("¿Qué operación deseas realizar?\n1. Suma\n2. Resta\n3. Multiplicación\n4. División\n5. Salir\n")
        operacion = int(input())
        while operacion != 5:
            if operacion == 1:
                print(pkg.aritmetica.sum(float(input("Ingresa el primer número: ")), float(input("Ingresa el segundo número: "))))
            elif operacion == 2:
                print(pkg.aritmetica.res(float(input("Ingresa el primer número: ")), float(input("Ingresa el segundo número: "))))
            elif operacion == 3:
                print(pkg.aritmetica.mul(float(input("Ingresa el primer número: ")), float(input("Ingresa el segundo número: "))))
            elif operacion == 4:
                print(pkg.aritmetica.div(float(input("Ingresa el primer número: ")), float(input("Ingresa el segundo número: "))))
            else:
                print("Opción no válida")
            operacion = int(input("¿Qué operación deseas realizar?\n1. Suma\n2. Resta\n3. Multiplicación\n4. División\n5. Salir\n"))
    elif opciones == 2:
        print("¿Qué deseas saber?\n1. Si un número es primo\n2. Si un número es par\n3. Si un número es impar\n4. Salir\n")
        operacion = int(input())
        while operacion != 4:
            if operacion == 1:
                print(pkg.par_non_prim.is_prime(int(input("Ingresa el número: "))))
            elif operacion == 2:
                print(pkg.par_non_prim.is_even(int(input("Ingresa el número: "))))
            elif operacion == 3:
                print(pkg.par_non_prim.is_odd(int(input("Ingresa el número: "))))
            else:
                print("Opción no válida")
            operacion = int(input("¿Qué deseas saber?\n1. Si un número es primo\n2. Si un número es par\n3. Si un número es impar\n4. Salir\n"))
    elif opciones == 3:
        print("¿Qué deseas obtener?\n1. Una lista de números primos en un rango\n2. Una lista de números no primos en un rango\n3. Una lista de números pares en un rango\n4. Una lista de números impares en un rango\n5. Salir\n")
        operacion = int(input())
        while operacion != 5:
            if operacion == 1:
                print(pkg.par_non_prim.primes_in_range(int(input("Ingresa el número mínimo: ")), int(input("Ingresa el número máximo: "))))
            elif operacion == 2:
                print(pkg.par_non_prim.not_primes_in_range(int(input("Ingresa el número mínimo: ")), int(input("Ingresa el número máximo: "))))
            elif operacion == 3:
                print(pkg.par_non_prim_in_range.even_in_range(int(input("Ingresa el número mínimo: ")), int(input("Ingresa el número máximo: "))))
            elif operacion == 4:
                print(pkg.par_non_prim_in_range.odd_in_range(int(input("Ingresa el número mínimo: ")), int(input("Ingresa el número máximo: "))))
            else:
                print("Opción no válida")
            operacion = int(input("¿Qué deseas obtener?\n1. Una lista de números primos en un rango\n2. Una lista de números no primos en un rango\n3. Una lista de números pares en un rango\n4. Una lista de números impares en un rango\n5. Salir\n"))
    else:
        print("Opción no válida")
    opciones = int(input("¿Qué deseas hacer?\n1. Aritmética\n2. Saber si un número es primo, par o no\n3. Obtener una lista de números pares, impares, primos y no primos en un rango\n4. Salir\n"))
print("Gracias por usar el programa")
