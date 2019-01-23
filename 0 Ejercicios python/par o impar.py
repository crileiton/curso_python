# Autor: Cristian Leiton Valencia
# Ejercicio: Saber si un número ingresado por consola es par,impar, negativo o positivo.
numero = int(input("Ingrese un número: \n"))
if((numero % 2) == 0) and (numero > 0):
    print("El número",numero,"es par y positivo.")
if(numero % 2) == 0 and (numero < 0):
    print("El número",numero," es par y negativo")
if (numero % 2) != 0 and (numero < 0):
    print("El número",numero," es inpar y negativo")
if (numero % 2) != 0 and (numero > 0):
    print("El número",numero," es inpar y positivo")
