# La sentencia if permite dividir el flujo de un programa en diferentes caminos
# Ejemplo
if True:
    print("Se cumple la condición")
# Es importante que todo el bloque que se ejecutara debe de estar identado, de esta manera
# podemos ejecutar dentro, muchas tareas... asi
if True:
    print("Se cumple la condición")
    print("Tambien se muestra este print")

# Si a la condición le pasamos algo que no es True, sencillamente no se ejecutará..Ejemplo
if False:
    print("Ojo Se cumple la condición")
    print("Ojo Tambien se muestra este print")

# Y que pasaria si le pasamos algo asi...
if not False:
    print("Cristian Se cumple la condición")
    print("Cristian Tambien se muestra este print") 

# Intentemos encadenar más if
a = 5
if a == 2:
    print("a vale 2")
if a == 5:
    print("a vale 5")
    
# Tambien podemos definir if dentro de if siempre que respetemos los niveles de tabulación
a = 5
b = 10
if a == 5:
    print("a vale: ",a)
    if b == 10:
        print("y b vale: ",b)

# Tambien se puede hacer en una sola expresion gracias a and ... asi
a = 5
b = 10
if a == 5 and b == 10:
    print("a vale",a,"y b vale",b)

# Tambien existe la sentencia else, cuando no se cumple la condición
n = 11
if n % 2 == 0:
    print(n,"Es un número par.")
else:
    print(n,"Es un número impar")

# Tambien existe la sentencia elif (sino si), se encadena a un if para comprobar otra posible condición
# Siempre que la anterior no se cumpla
# Ejemplo: util para crear menus
comando = "SALUDAR"
if comando == "ENTRAR":
    print("Bienvenido al sistema")
elif comando == "SALUDAR":
    print("Hola, espero que estes bien aprendiendo Python")
elif comando == "SALIR":
    print("Saliendo del sistema")
else:
    print("Este comando no se conoce")

# Es importante: el uso de if elif else a diferencia de varios if como antes, comprueba las condiciones de
# arriba abajo, hasta que se comprueba alguna de ellas

nota = float(input("Introduce una nota\n"))
if nota >= 9:
    print("Sobresaliente")
elif nota >= 7:
    print("Notable")
elif nota >= 6:
    print("Bien")
elif nota >= 5:
    print("Suficiente")
else:
    print("Insuficiente")

# Truco: palabra pass, que se puede utilizar para definir un bloque vacio, por ejemplo...
# Imaginar que queremos una estructura asi
if True:
    pass

# La sentencia switch NO existe en python pero se puede manejar con diccionarios.
