# Dado que Python es un lenguaje muy flexible, implementa multitud de tipos distintos por defecto
# y eso incluye tambien tipos compuestos de datos que se utilizan para agrupar diferentes elementos o items
# por ejemplo variables o valores, el mas versatil de estos tipos compuestos es la lista que se puede 
# escribir como una lista de items separados por "comas" y contenidos entre dos corchetes "[]"
# Ejemplo
numeros = [1,2,3,4]
# Normalmente las listas suelen contener items del mismo tipo pero en python no tenemos esta restricción
# por tanto se puede tener una lista de datos y muchos tipos de datos diferentes...por ejemplo
datos = [4,"una cadena",-15,3.14,"otra cadena"]
# Las listas son muy parecidas a las cadenas de caracteres ya que funcionan exactamente igual con los
# indices y tambien permiten utilizar el slicing.
# Por ejemplo si se quiere acceder al primer elemento de esta lista de datos, simplemente nos podemos 
# referir con el indice 0, y ya se lo puede mostrar... asi
print(datos[0])
# Si queremos mostrar el ultimo, podemos hacerlo asi
print(datos[-1])
# O utilizando slicing podemos referirnos por ejemplo...
print(datos[-2:])

# Otra cosa que permiten las listas al igual que las cadenas de caracteres es concatenar con otras listas
# Ejemplo
print(numeros + [5,6,7,8])

# Sin embargo hay una peculiaridad y es que las cadenas de caracteres eran inmutables pero las listas NO.
# Ejemplo
pares = [0,2,4,5,8,10]
# Antes de modificar
print(pares)
pares[3] = 6
# Modificado
print(pares)

# Otra cosa que tienen las listas, es que podemos añadir elementos justo al final, esto es porque incluye
# muchos metodos internos
# Una lista tiene un metodo llamado "append" (adjuntar en español) que permite añadir elementos al final
# Ejemplo: Si quisieramos añadir un nuevo par a la lista de pares
pares.append(12)
print(pares)

# Tambien permite operaciones...asi
pares.append(7*2)
print(pares)

# Una cosa que permiten las listas es la asignación con slicing, es decir tenemos la siguiente lista 
letras = ['a','b','c','d','e','f']
# y quisiera cambiar algunas letras, por ejemplo las 3 primeras y ponerlas en mayuscula
# Para acceder a las 3 primeras letras tenemos...
print(letras[:3])
# Entonces si yo quiero reasignar, se puede hacer asi
letras[:3] = ['A','B','C']
print(letras)

# Otra funcionalidad que se puede realizar gracias al slicing, para borrar valores...
letras[:3] = []
print(letras)

# Otra formar para borrar todo el contenido es asi...
letras = []
print(letras)

# Tambien podemos utilizar el metodo "len", para saber la longitud de una lista
# Ejemplo
print(len(letras))

# Tambien podemos saber la longitud de la lista pares
print(len(pares))

# Las listas pueden contener otras listas, esto se conoce como listas anidadas
# Ejemplo
a = [1,2,3]
b = [4,5,6]
c = [7,8,9]
resul = [a,b,c]
print(resul)
# Lo que se obtiene con el anterior comando es una lista formada 3 listas
# Para referirnos a una lista, pues nos referimos como si se tratase de un elemento
# Por ejemplo para acceder a la primera lista podemos utilizar el indice 0
print(resul[0])
# O a la ultima asi...
print(resul[-1])

# Si quiero acceder al primer elemento de la primera lista, se lo hace asi
print(resul[0][0])
# Si quisiera acceder al número 8
print(resul[2][1])
# Si quisiera acceder al ultimo dato de la ultima lista seria...
print(resul[-1][-1])

