# -------------------------------
# Autor: Cristian Leiton Valencia
# -------------------------------

# Ejercicio...
""" Escriba un programa que pida al usuario dos números enteros,
y luego entregue la suma de todos los números que están entre ellos. """

# Ejemplo...
""" Por ejemplo, si los números son 1 y 7, debe entregar como resultado 2 + 3 + 4 + 5 + 6 = 20. """

# Desarrollo ...

numero_1 = int(input("Escriba el número 1: \n"))
numero_2 = int(input("Escriba el número 2: \n"))
suma = 0

for numero in range(numero_1 + 1,numero_2):
    suma += numero
print("La suma de los numeros entre {} y {} es {}".format(numero_1,numero_2,suma))