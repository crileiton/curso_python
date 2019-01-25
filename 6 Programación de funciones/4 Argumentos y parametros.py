"""#resta de numeros
def resta(a, b):
    'Resta de numeros'
    return a - b

d = resta(2,6)
print(d)

# Tambien es posible enviar los argumentos por nombre y su gracia es que podemos cambiar el orden a nuestro antojo en el momento de llamar a la funcion
e = resta(b = 3, a = 6)
print(e)

# Otra cosa que podemos hacer es asignar un valor por defecto a los parametros de una función, para evitar que se ejecute
# una función incorrectamente... ejemplo
#resta()
# si ejecutamos la anterior linea de codigo tal cual genera el error: TypeError: resta() missing 2 required positional arguments: 'a' and 'b'

# Para arreglar esto podemos definir asi...
def resta2(a = None, b = None):
    return a - b

print(resta2())
# Ejecutando el anterior codigo genera este error: TypeError: unsupported operand type(s) for -: 'NoneType' and 'NoneType'
"""
# Para evitar debemos hacer lo siguiente

def resta3(a = None, b = None):
    if (a == None or b == None):
        print("Error debes enviar 2 números a la función")
        return
    else:
        return a - b

print(resta3())