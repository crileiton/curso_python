# Ejercicio No. 3
import sys
# Es 2 en la sgte linea porque el nombre del archivo cuenta tambien
if len(sys.argv) == 2:
    numero = int(sys.argv[1])
    if (numero > 0):
        lista_numeros = [numero]
        print(lista_numeros)
    else:
        print("El número no es positivo")
        print("Ejemplo: descomposicion.py [número_entero_positivo]")
else:
    print("Error argumentos incorrectos.")
    print("Ejemplo: descomposicion.py [número_entero_positivo]")
