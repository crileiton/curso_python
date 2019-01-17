# ¿Que es una iteración?
# - Iterar es realizar una determinada acción varias veces
# - Cada vez que se repite la acción se denomina iteración
# While (Mientras en español)
# Se basa en repetir un bloque a partir de evaluar una condición lógica, siempre que ésta sea True.

# Ejemplo:
c = 0
while c <= 5:
    c += 1
    print("c vale",c)

# En python tambien podemos encadenar un else despues de un while, para ejecutar un codigo una vez este se ha
# completado .... Ejemplo

c = 0
while c <= 5:
    c += 1
    print("c vale",c)
else:
    print("Se ha completado toda la iteracion y c vale: ",c)

# Imaginar que queramos romper la ejecución del bucle while en algun momento, por ejemplo 
# salir cuando la c valga 2... podemos utilizar una palabra llamada break (romper español)

c = 0
while c <= 5:
    c += 1
    if (c == 2):
        print("Rompemos el bucle cuando c vale: ",c)
        break
    print("c vale",c)
else:
    print("Se ha completado toda la iteracion y c vale: ",c)

# En el anterior ejemplo tampoco se ejecuta el else, porque la rompimos en medio de funcionamiento

# Tambien es importante la sentencia continue (continuar español), permite saltar la iteración actual, pero
# sin romper el bucle

c = 0
while c <= 5:
    c += 1
    if (c == 4):
        print("Continuamos con la siguiente iteración y c vale: ")
        continue
    print("c vale",c)
else:
    print("Se ha completado toda la iteracion y c vale: ",c)

# la sentencia do - while (Programa para una terminal por ejemplo)
# Ejemplo
print("Bienvenido al menú interactivo")
while(True):
    print("""¿Qué deseas hacer? Escribe una opción:
    1. Saludar
    2. Sumar dos números
    3. Salir""")
    opcion = input()
    if opcion == '1':
        print("Hola, espero estes bien, un saludo")
    elif opcion == '2':
        n1 = float(input("Introduce el primer número:\n"))
        n2 = float(input("Introduce el segundo número:\n"))
        print("El resultado de la suma es:", n1+n2)
    elif opcion == '3':
        print("Buena suerte, !hasta luego¡ ha sido un placer ayudarte")
        break # Este momento es muy importante porque rompemos la ejecución del while infinito
    else:
        print("Comando desconocido, vuelve a intentarlo")