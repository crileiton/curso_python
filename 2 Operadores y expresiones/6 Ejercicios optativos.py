# Solución Ejercicio 1
# Solución Cristian Leiton
print("***Solución Cristian Leiton***")
numero_1 = float(input("Ingrese el primer número\n"))
numero_2 = float(input("Ingrese el segundo número\n"))
if (numero_1 == numero_2):
    print("El número",numero_1,"y el número",numero_2,"son iguales.")
else:
    print("El número",numero_1,"y el número",numero_2,"son diferentes.")
if (numero_1 > numero_2):
    print("El número",numero_1,"es mayor que el número",numero_2,".")
if (numero_2 >= numero_1):
    print("El número",numero_2,"es mayor o igual que el número",numero_1,".")

# Solución profesor
print("***Solución profesor***")
n1 = float(input("Introduce el primer número\n"))
n2 = float(input("Introduce el segundo número\n"))
print("Son iguales? ",n1 == n2)
print("Son diferentes? ",n1 != n2)
print("El primero es mayor que el segundo? ",n1 > n2)
print("El segundo es mayor o igual que el primero? ",n2 >= n1)

# Solución Ejercicio 2
# Solución Cristian Leiton
cadena = input("Ingrese una cadena de texto:\n")
print("La longitud es mayor o igual que 3? y es menor que 10?",len(cadena) >= 3 and len(cadena) < 10)

# Solución profesor
cadena_profe = input("Escribe una cadena: \n")
condiciones = len(cadena_profe) >= 3 and len(cadena) < 10
print("¿La longitud de la cadena es mayor o igual que 3 y menor que 10? ",condiciones) 

# Solución Ejercicio 3
# Solución Cristian Leiton y profe fueron iguales
numero_magico = 12345679
numero_usuario = int(input("Ingresa un número entre 1 y 9:\n"))
numero_usuario *= 9
numero_magico *= numero_usuario
print("El número mágico es: ",numero_magico)

