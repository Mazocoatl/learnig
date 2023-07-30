#función de números primos
def is_prime(number):
    if number < 2:
        return False
    elif number == 2:
        return True
    elif number > 2 and number % 2 == 0:
        return False
    else:
        for i in range(3, number):
            if number % i == 0:
                return False
    return True

#función de números no primos
def is_not_prime(number):
    if number < 2:
        return True
    elif number == 2:
        return False
    elif number > 2 and number % 2 == 0:
        return True
    else:
        for i in range(3, number):
            if number % i == 0:
                return True
    return False

#función de número pares
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

#función de número impares
def is_odd(number):
    if number % 2 != 0:
        return True
    else:
        return False

#función de número pares en un rango
def even_in_range(min, max):         
    even = []
    for i in range(min, max + 1):
        if is_even(i):
            even.append(i)
    return even

#función de número impares en un rango
def odd_in_range(min, max):
    odd = []
    for i in range(min, max + 1):
        if is_odd(i):
            odd.append(i)
    return odd

#función de números primos en un rango
def primes_in_range(min, max):
    primes = []
    for i in range(min, max + 1):
        if is_prime(i):
            primes.append(i)
    return primes

#función de números no primos en un rango
def not_primes_in_range(min, max):
    not_primes = []
    for i in range(min, max + 1):
        if is_not_prime(i):
            not_primes.append(i)
    return not_primes
