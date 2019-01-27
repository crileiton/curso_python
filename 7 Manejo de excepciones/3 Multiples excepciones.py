# Es posible definir distintas excepciones eso podemos hacerlo gracias a que cuando ocurre un error
# dentro del try cada excepcion tiene su propio identificador, si lo capturamos y lo guardamos en una variable
# podriamos hacer un truco para mostrar el nombre de la excepción...asi
"""
try:
    n = input("Introduce un número:\n")
    5 / n
except:
    print("Error")

# salta error porque no estamos convirtiendo a entero o a decimal
# Pero no sabemos que tipo de fallo es el que ha ocurrido, para poder sacar el identificador del error podemos hacer
# este truco

try:
    n = input("Introduce un número:\n")
    5 / n
except Exception as e:  # De esta manera vamos a guardar una excepción generica en la variable e.
    print( type(e).__name__ ) # Para conseguir el nombre del error
"""
# Vamos a encadenar diferentes excepciones asi ...

try:
    n = float(input("Introduce un número:\n"))
    5 / n
except TypeError: # Aqui tendriamos la excepción que se ejecutara cuando ocurra un error como el anterior (no convertir a entero)
    print("No es posible dividir el número por una cadena.")
except ValueError:
    print("Debes introducir un número.")
except ZeroDivisionError:
    print("La división entre 0 es indeterminado")
except Exception as e:  # De esta manera vamos a guardar una excepción generica en la variable e.
    print( type(e).__name__ ) # Para conseguir el nombre del error (IMPORTANTE PARA SABER EL ERROR Y PERSONALIZAR EL ERROR ARRIBA)
