# Una excepción es un bloque de codigo excepcional que nos permitira continuar con la ejecución en caso de que ocurra un error
# volviendo al ejemplo del ejercicio anterior tenemos el problema de que cuando el usuario no introduzca una cedena
# que fuera un número si no un texto, fallaba al hacer la conversión.
try:    
    n = float(input("Introduce un número:\n"))
    m = 4
    print("{} / {} = {}".format(n, m, n / m))
except:
    print("Ha ocurrido un error, introduce bien el número.")


# Para que el codigo se repita hasta que el usuario ingrese bien el número se debe hacer lo siguiente
while(True):
    try:    
        n = float(input("Introduce un número:\n"))
        m = 4
        print("{} / {} = {}".format(n, m, n / m))
        break # Importante romper la iteración si todo ha salido bien
    except:
        print("Ha ocurrido un error, introduce bien el número.")

# Las excepciones tambien permite añadir un bloque de codigo llamado else al except para ejecutar un codigo en caso de 
# que todo vaya correctamente y ese es lugar perfecto para el break asi...
while(True):
    try:    
        n = float(input("Introduce un número:\n"))
        m = 4
        print("{} / {} = {}".format(n, m, n / m))
    except:
        print("Ha ocurrido un error, introduce bien el número.")
    else:
        print("Todo ha funcionado correctamente")
        break # Importante romper la iteración si todo ha salido bien
# Todavia se permite una sentencia extra llamada Finaly o finalmente y se ejecuta siempre al final del try...asi
while(True):
    try:    
        n = float(input("Introduce un número:\n"))
        m = 4
        print("{} / {} = {}".format(n, m, n / m))
    except:
        print("Ha ocurrido un error, introduce bien el número.")
    else:
        print("Todo ha funcionado correctamente")
        break # Importante romper la iteración si todo ha salido bien
    finally:
        print("Fin de la iteración")
# Finally se ejecutara siempre al final de cada iteración del while, ocurra o no ocurra un error 

# Resumiendo: tenemos 4 bloques de excepción.
# try: Para capturar cualquier error dentro de un bloque de instrucciones
# except: Para definir el codigo excepcional.
# else: Para definir el codigo que se ejecutara si no ocurre ningun error 
# finally: Para definir el codigo que se ejecutara al final alla o no un error 