"""
# Solución ejercicio 1 - Cristian Leiton
print("Bienvenido al menú")
print("******************")
n1 = float(input("Ingresa el primer número:\n"))
n2 = float(input("Ingresa el segundo número:\n"))
while True:
    print("""""""Seleccione una operación:
    1. Sumar
    2. Restar
    3. Multiplicar
    4. Salir
    Seleccione ... """""")
    operacion = input()
    if operacion == '1':
        print("La suma de los números es: ",n1 + n2)
    elif operacion == '2':
        print("La resta de los números es: ",n1 - n2)
    elif operacion == '3':
        print("La multiplicación de los números es: ",n1 * n2)
    elif operacion == '4':
        print("Hasta pronto")
        break
    else:
        print("La opción escogida no es correcta")

# Solución ejercicio 2 - Cristian Leiton
v = 2
while((v % 2) == 0):
    n = int(input("Ingrese un número impar:\n"))
    v = n
print("Perfecto el número",n,"es impar.")
"""
# Solución ejercicio 3 - Cristian Leiton
#print(sum(range(0,101,2)))

# Solución ejercicio 3 - profe - Tradicional
num = 0
suma = 0
while num <= 100:
    if num % 2 == 0:
        suma += num
    num += 1
print(suma)

