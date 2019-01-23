# Ejercicio No. 3
import sys
if len(sys.argv) == 3:
    filas = int(sys.argv[1])
    columnas = int(sys.argv[2])

    if ( (filas > 0 and filas < 10) and (columnas > 0 and columnas < 10) ):
        for fila in range(filas):
            print("")
            for columna in range(columnas):
                print("*", end='')
    else:
        print("Filas o columnas incorrectas.")
        print("Ejemplo: tabla.py [1-9] [1-9 ]")
else:
    print("Error argumentos incorrectos.")
    print("Ejemplo: tabla.py [1-9] [1-9 ]")