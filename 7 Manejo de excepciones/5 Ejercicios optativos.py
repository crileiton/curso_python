"""# Solución ejercicio No. 1 - Cristian Leiton Valencia
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Error, no se permite la división entre 0")

# Solución ejercicio No. 2 - Cristian Leiton Valencia
lista = [1,2,3,4,5]
try:
    lista [10]
except IndexError:
    print("Indice fuera de rango, debes utilizar un número mayor o igual a 0 y menor que {}".format(len(lista)))


# Solución ejercicio No. 3 - Cristian Leiton Valencia

colores = {'rojo':'red', 'verde':'green', 'negro':'black'}
try:
    colores['blanco']
except KeyError:
    print("Error: La clave del diccionario no se encuentra, debes probar con otra que si exista")

"""
# Solución ejercicio No. 4 - Cristian Leiton Valencia

try:
    resultado = 15 + "20"
except TypeError:
    print("Error: Solo es posible sumar datos del mismo tipo, debes transformar el número a cadena o la cadena a número")
    
