# Solución ejercicio No. 1 - Cristian Leiton Valencia
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


# Solución ejercicio No. 4 - Cristian Leiton Valencia

try:
    resultado = 15 + "20"
except TypeError:
    print("Error: Solo es posible sumar datos del mismo tipo, debes transformar el número a cadena o la cadena a número")

# Solución ejercicio No. 5 - Cristian Leiton Valencia

def agregar_una_vez(pLista, pElemento):
    try:
        if pElemento in pLista:
            raise ValueError("Error: Imposible añadir elementos duplicados => ",pElemento)
        else:
            pLista.append(pElemento)
            print("Agregado")
    except ValueError:
        print('Error: Imposible añadir elementos duplicadosss => ',pElemento)

elementos = [1, 5, -2]
agregar_una_vez(elementos,'hola')


def agregar_una_vez_2(pLista, pElemento):
    try:
        bandera = False
        for elemento in pLista:
            if(elemento == pElemento):
                bandera = True
                raise ValueError
        if(bandera == False):
            pLista.append(pElemento)
            print("Agregado")
    except ValueError:
        print('Error: Imposible anadir elementos duplicadosss => ',pElemento)

elementos = [1, 5, -2]
agregar_una_vez_2(elementos,10)
agregar_una_vez_2(elementos,-2)
agregar_una_vez_2(elementos,'Hola')
print(elementos)