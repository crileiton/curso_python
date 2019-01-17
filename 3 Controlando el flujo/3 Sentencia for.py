# Siempre que se piense en listas, cadenas de texto o cualquier otro tipo compuesto, el for es el mejor amigo
# Ejemplo: Imaginar que tenemos una lista de numeros y queremos recorrer dinamicamente todos los elementos
# y mostrarlos por pantalla (dinamicamente == automaticamente =D)
# Con lo que sabemos podemos utilizar un bucle while y un contador a modo de indice para hacerlo... asi
numeros = [1,2,3,4,5,6,7,8,9,10]
indice = 0 # Contador
while(indice < len(numeros)):
    print(numeros[indice])
    indice += 1
# Lo anterior es la forma mas larga porque primero debe declarse los numeros

# Con el ciclo for se lo puede hacer asi
for numero in numeros:
    print(numero)   

# Manipular el contenido de la lista
indice = 0
numeros = [1,2,3,4,5,6,7,8,9,10]
for numero in numeros:
    numeros[indice] *= 10
    indice += 1
print(numeros)

# Lectura secuencial (utilizar mucho en un futuro)
numeros = [1,2,3,4,5,6,7,8,9,10]
for indice,numero in enumerate(numeros):
    numeros[indice] *= 10
print(numeros)

# Recorrer todos los caracteres de una cadena de texto.
cadena = "Hola amigos"
for caracter in cadena:
    print(caracter)

# Modificar cadenas de texto
# Genera error porque las cadenas de texto son inmutables
"""cadena = "Hola amigos"
for i, caracter in enumerate(cadena):
    cadena[i] = "*" """

# Para poder realizar la modificación, se debe realizar asi...
cadena = "Hola amigos"
cadena2 = ""
for caracter in cadena:
    cadena2 += caracter * 2
print(cadena2)

# Diferencia del for de Python frente a otros lenguajes
for i in range(10):
    print(i)

# el range es igual a decir
print(list(range(10)))
