"""# La recursividad es un proceso de repetición en el que algo se repite asi mismo
# Este efecto es lo que sucede cuando ponemos 2 espejos uno frente a otro
# Se utiliza en las funciones y toman el nombre de funcion recursiva

# Ejemplo de funcion recursiva sin retorno.
def cuenta_atras(numero):
    numero -= 1
    if numero > 0:
        print(numero)
        cuenta_atras(numero)
    else:
        print("Booooooom!")
    print("Fin de la función",numero)

cuenta_atras(10)
"""
# Ejemplo de factorial de un numero: entero que corresponde a ese numero multiplicado por todos los numeros enteros que van
#antes de él hasta el 1
def factorials(num):
    print('valor inicial es:',num)
    if num > 1:
        num = num * factorials(num - 1)
    print('valor final es:',num)
    return num

print(factorials(5))

