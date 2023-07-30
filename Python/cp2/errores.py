#errores
# 1. Error de sintaxis (SyntaxError) son errores de escritura en el codigo
# 2. Excepciones (Exceptions) son errores que ocurren durante la ejecucion del programa
# 3. Errores semanticos (SemanticError) son errores de logica en el programa

# Manejo de errores
try: # Intenta ejecutar el codigo
     print(2/0)
except ZeroDivisionError: # Si ocurre un error de division por cero
     print("No se puede dividir por cero") # Imprime un mensaje de error
except: # Si ocurre cualquier otro error
     print("Ha ocurrido un error") # Imprime un mensaje de error

# Lanzar excepciones
def mi_funcion(algo=None): 
        try: 
            if algo is None: # Si el valor de algo es nulo
                raise ValueError("Error! No se permite un valor nulo") # Lanza una excepcion
        except ValueError: # Si ocurre un error de valor
            print("Error! No se permite un valor nulo (desde la funcion)")  # Imprime un mensaje de error

mi_funcion() # Llama a la funcion
# Error! No se permite un valor nulo (desde la funcion)

# Excepciones personalizadas
class MiError(Exception): # Crea una clase de excepcion personalizada
    def __init__(self, valor): # Define el metodo constructor
        self.valor = valor # Inicializa el atributo valor

    def __str__(self): # Define el metodo para convertir a cadena
        return f"Error! {self.valor}" # Devuelve el mensaje de error
    
try:
    raise MiError(2*2) # Lanza la excepcion personalizada
except MiError as e: # Si ocurre un error de la excepcion personalizada
    print(e) # Imprime el mensaje de error
# Error! 4

#assert <expresion booleana>, <mensaje de error> # Si la expresion booleana es falsa, lanza una excepcion con el mensaje de error indicado
assert 2 + 2 == 4, "La suma de 2 + 2 no es 4" # Si la suma de 2 + 2 es 4, no ocurre nada
assert 2 + 2 == 5, "La suma de 2 + 2 no es 5" # Si la suma de 2 + 2 no es 5, lanza una excepcion con el mensaje de error indicado
# AssertionError: La suma de 2 + 2 no es 5

#assert <expresion booleana> # Si la expresion booleana es falsa, lanza una excepcion AssertionError
assert 2 + 2 == 4 # Si la suma de 2 + 2 es 4, no ocurre nada
assert 2 + 2 == 5 # Si la suma de 2 + 2 no es 5, lanza una excepcion AssertionError
# AssertionError

#assert <expresion booleana>, <expresion> # Si la expresion booleana es falsa, lanza una excepcion con el valor de la expresion
assert 2 + 2 == 4, 2 + 2 # Si la suma de 2 + 2 es 4, no ocurre nada
assert 2 + 2 == 5, 2 + 2 # Si la suma de 2 + 2 no es 5, lanza una excepcion con el valor de la expresion
# AssertionError: 4

#varios errores en un try
try:
    print(2/0)
    print("No se ejecuta")
except ZeroDivisionError:
    print("División por cero")
except ArithmeticError:
    print("Error aritmético")
age = 16
if age < 18:
    raise Exception("Menor de edad")