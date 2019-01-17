# Correción del ejercicio 3
numero_1 = 9
numero_2 = 3
numero_3 = 6

media = (numero_1 + numero_2 + numero_3) / 3
print("La nota promedio es: ", media)

# Solución del ejercicio 4
numero_1 = 10 * 0.15
numero_2 = 7 * 0.35
numero_3 = 4 * 0.50
media = numero_1 + numero_2 + numero_3
print("La nota promedio es: ", media)

# Solución del ejercicio 5
matriz = [
    [1,1,1,3],
    [2,2,2,7],
    [3,3,3,9],
    [4,4,4,13]
]
matriz [0][3] = (sum(matriz[0][:-1]))
matriz [1][3] = (sum(matriz[1][:-1]))
matriz [2][3] = (sum(matriz[2][:-1]))
matriz [3][3] = (sum(matriz[3][:-1]))
print(matriz)

# Solución del ejercicio 6
cadena = "zeréP nauJ,01"
cadena_bien = cadena[::-1]
nombre_apellido = cadena_bien[3:]
nota = cadena_bien[:2]
print(nombre_apellido," ha sacado un ",nota," de nota.")