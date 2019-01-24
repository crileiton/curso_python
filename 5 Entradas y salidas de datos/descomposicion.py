# Ejercicio No. 3
import sys
# Es 2 en la sgte linea porque el nombre del archivo cuenta tambien
if len(sys.argv) == 2:
    numero = int(sys.argv[1])
    if (numero > 0 and numero < 9999):
        cadena = str(numero)
        longitud = len(cadena)
        for i in range(longitud):
            print("{:04d}".format( int(cadena[longitud-1-i]) * 10 ** i) )
    else:
        print("El número no es correcto")
        print("Ejemplo: descomposicion.py [0 - 9999]")
else:
    print("Error argumentos incorrectos.")
    print("Ejemplo: descomposicion.py [0 - 9999]")
