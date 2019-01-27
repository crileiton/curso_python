"""# Sin duda las excepciones nos pueden ayudar a optimizar nuestros programas y a prevenir errores
# En esta clase aprenderemos a llamar excepciones

def mi_Funcion(algo = None):
    if algo == None: # Tambien se puede poner: if algo is None:
        print("Error, no se permite un valor nulo")

print(mi_Funcion()) # Si ejecutamos la función vacia, genera el siguiente error: Error, no se permite un valor nulo

# El anterior error, esta relacionado con una excepción que podriamos decir que es una excepción de valor
# Podemos invocar la excepción de value error...asi
def mi_Funcion(algo = None):
    if algo == None: # Tambien se puede poner: if algo is None:
        raise ValueError("Error, No se permite un valor nulo")

print(mi_Funcion())
"""
# Podemos mejorar toda la función colocando todo en try..asi
def mi_Funcion(algo = None):
    try:
        if algo == None: # Tambien se puede poner: if algo is None:
            raise ValueError("Error, No se permite un valor nulo")
    except ValueError:
        print("Error, No se permite un valor NULO")

print(mi_Funcion())