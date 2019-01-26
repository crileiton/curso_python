# Autor: Cristian Leiton - Ejercicio No. 1
def area_rectangulo(base,altura):
    """ Resuelve el área de un rectángulo

    Devuelve el área de un rectángulo en tipo int

    Parámetros:
    base -- Base rectángulo
    altura -- Altura rectángulo
    
    """
    return base * altura

#print(area_rectangulo(4,5))

# Autor: Cristian Leiton - Ejercicio No. 2

def area_circulo(radio):
    """ Resuelve el área de un circulo

    Devuelve el área de un circulo en tipo float

    Parámetros:
    radio -- Radio del círculo
    
    """
    import math
    resultado = (radio ** 2) * math.pi
    return resultado

#print(area_circulo(123))

# Autor: Cristian Leiton - Ejercicio No. 3

def relacion(n1, n2):
    """ Relación de numeros

    Devuelve 1 cuando n1 es mayor a n2
    Devuelve -1 cuando n1 es menor a n2
    Devuelve 0 cuando n1 es igual a n2

    Parámetros:
    n1 -- Primer número
    n2 -- Segundo número
    
    """
    r = 0
    if (n1 > n2):
        r = 1
    elif (n1 < n2):
        r = -1
    return r

#print(relacion(4,2))

# Autor: Cristian Leiton - Ejercicio No. 4

def intermedio(n1, n2):
    """ Intermedio de dos números

    Devuelve el número intermedio de dos números dados por parámetro

    Parámetros:
    n1 -- Primer número
    n2 -- Segundo número
    
    """
    return (n1 + n2) / 2

#print(intermedio(-12,24))

# Autor: Cristian Leiton - Ejercicio No. 5

def recortar(num_recortar, lim_inferior, lim_superior):
    """ Recorte de números

    Devuelve el limite inferior si el número a recortar es menor.
    Devuelve el limite superior si el número a recortar es mayor.
    Devuelve el número sin cambios si no se supera ningún limite.

    Parámetros:
    num_recortar -- Número a recortar
    lim_inferior -- Limite inferior
    lim_superior -- Limite superior
    
    """
    if num_recortar < lim_inferior:
        return lim_inferior
    elif num_recortar > lim_superior:
        return lim_superior
    return num_recortar

#print(recortar(15, 0, 10))

# Autor: Cristian Leiton - Ejercicio No. 6

def separar(lista):
    """ Pares e impares

    Devuelve una lista con los números pares de la lista dada por parámetro.
    Devuelve otra lista con los números impares de la lista dada por parámetro.

    Parámetros:
    lista -- Lista de números dados por el usuario
    
    """
    lista.sort()
    pares = []
    impares = []
    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    return pares, impares

numeros = [-12, 84, 13, 20, -33, 101, 9]

pares, impares = separar(numeros)
print(pares)
print(impares)

# O tambien podemos mostrar el resultado asi...
print(separar(numeros))