# Nota: Cuando enviamos información a una función, generalmente estos datos se envian por valor, eso significa que
# se crea una copia dentro de la función de los valores que enviamos en sus propias variables, pero hay un caso
#excepcional las colecciones, listas,diccionarios, conjuntos... estos datos se envian por referencia...o sea
# en lugar de una copia dentro de la función estaremos manejando el dato original y si los modificamos, estos cambios
#tambien se veran reflejados en el exterior porque hacen referencia a la variable externa como una especie de acceso directo

# Ejemplo...
def doblar_valor(numero):
    numero *= 2

n = 10
doblar_valor(n)
print(n)
# En el anterior codigo se supone que duplicamos el valor de 10 pero cuando imprimimos n, nos damos cuenta que no se afectado.
#porque la variable numero es una copia del valor externo y no le afecta en nada en lo que hagamos dentro

# En cambio...una lista...

def doblar_valores(numeros):
    for i,m in enumerate(numeros):
        numeros[i] *= 2

ns = [10,50,100]
doblar_valores(ns)
print(ns)
# Ahora los cambios se ven reflejados en el exterior y con el numero normal NO.

#La pregunta es:
# Es posible indicar a Python cuando queremos pasar un argumento por valor o por referencia y la respuesta es NO.
# Pero podemos utilizar un truco.
# Por ejemplo devolver el valor modificado dentro de la función y volverlo asignar a la variable 

def nueva_funcion(numero):
    return numero * 2

numero = 10
n = nueva_funcion(n)
print(n)

# Y en el caso de una colección podemos evitar la modificación directa creando una copia en la llamada...asi

def nueva_2(numeros):
    for i,m in enumerate(numeros):
        numeros[i] *= 2

po = [10,50,100]
doblar_valores(po[:])
print(po)

# Con lo anterior vamos a prevenir que dentro de la función se pueda modificar la lista 