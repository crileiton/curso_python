"""# Solución ejercicio 4 - Cristian Leiton
total = 0
cantidad = int(input("Cuantos números desea introducir:\n"))
cantidad_total = cantidad
while(cantidad != 0):
    num = float(input("Ingrese un número: "))
    total += num
    cantidad -= 1
print("La cantidad de números es: ",cantidad_total)
print("La suma total es: ",total)
print("La media es: ",total / cantidad_total)

# Solución ejercicio 4 - Profe
repeticiones = int(input("¿Cuantos números quieres introducir?"))
suma = 0

for r in range(repeticiones):
    suma += float(input("Introduce un número: "))
print("Se han introducido",repeticiones,"números que en total han sumado",suma,"y la media es",suma / repeticiones)


# Solución ejercicio 5 - Cristian Leiton
numeros = [1,3,6,9]
while(True):
    num = int(input("Ingresa un número entero del 0 - 9\n"))
    if(num in range(10) and num in numeros):
        print("El numero cumple con los dos criterios")
        break

# Solución ejercicio 5 - Profe
numeros = [1,3,6,9]

while True:
    numero = int(input("Escribe un número del 0 al 9: \n"))
    if numero >= 0 and numero <= 9:
        break
if(numero in numeros):
    print("El número",numero,"SI encuentra en la lista.")
else:
    print("El número",numero,"NO encuentra en la lista.")
"""