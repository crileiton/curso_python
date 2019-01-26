# Dado que tenemos dos maneras de enviar y recibir datos por posición y por nombre, python implementa 2 formas
#distintas de gestionar los valores indeterminados para manejar por ejemplo los argumentos por posición lo que se debe hacer
#es indicar un parametro iterable de la siguiente forma

def indeterminados_posicion(*args):
    print(args)

indeterminados_posicion(1,'Hola',[1,2,3,4,5])
# Cuando imprimimos esta lista de argumentos indeterminados iterables, el resultado es una TUPLA
# Resultado: (1, 'Hola', [1, 2, 3, 4, 5])
# Nota: Las tuplas son inalterables, inmutables

# Podemos recorrer facilmente esta especie de colección iterable...ejemplo
def indeterminados_posicion2(*args):
    for arg in args:
        print(arg)

indeterminados_posicion2(1,'Hola',[1,2,3,4,5])

# En cuanto a los argumentos por nombre en lugar de un iterable, python puede gestionar un diccionario, o sea en lugar
#de una tupla un diccionario y ya que estos permiten identificar cada valor con una clave este seria el caso mas obvio
# Ejemplo...
def indeterminados_nombre(**kwargs):
    print(kwargs)

indeterminados_nombre(n = 5, c ='Hola', l = [1,2,3,4,5])
# Podemos observar que el resultado es un diccionario: {'n': 5, 'c': 'Hola', 'l': [1, 2, 3, 4, 5]}

# Ahora si queremos recorrerlos podemos hacer lo siguiente...

def indeterminados_nombre2(**kwargs):
    for kwarg in kwargs:
        print(kwarg)

indeterminados_nombre2(n = 5, c ='Hola', l = [1,2,3,4,5])
# Sabemos que los diccionarios que por defecto unicamente nos muestra las claves
# Respuesta:    n
#               c
#               l

# Podemos tambien mostrar primero la clave luego un espacio y luego clave 

def indeterminados_nombre3(**kwargs):
    for kwarg in kwargs:
        print(kwarg, " ", kwargs[kwarg])

indeterminados_nombre3(n = 5, c ='Hola', l = [1,2,3,4,5])

# Superfunción: con un poco de todo
# Requisitos:
#               Enviar primero los argumentos por posición y luego todos los que son por nombre
# Ej: Imaginar que queremos crear una superfunción a la que le pasemos un monton de valores, numeros y lo que queremos es 
#que los sume, no sabemos cuantos queremos enviar... ejem...

def super_funcion(*args, **kwargs):
    total = 0
    for arg in args:
        total += arg
    print("Sumatorio indeterminado es:",total)
    for kwarg in kwargs:
        print(kwarg," ", kwargs[kwarg])


super_funcion(10, 50, -1, 1.56, nombre = 'Cristian', edad = 27)

# La respuesta a al anterior codigo es:     Sumatorio indeterminado es: 60.56
#                                           nombre   Cristian
#                                           edad   27
# Podemos hacer una superfuncion que sume todos los numeros que son indeterminados y mostrar el nombre y edad de Cristian

