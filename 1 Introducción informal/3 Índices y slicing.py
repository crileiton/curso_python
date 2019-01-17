# Algo peculiar y evidente es que una cadena de texto de caracteres, esta formada por la unión de
# distintos caracteres inindividualmente.

# Python como la mayoria de lenguajes nos permite acceder independientemente a estos caracteres
# utilizando algo llamado indices. en el siguiente ejemplo se indica mejor lo mencionado.
palabra = "Python"

# Si queremos acceder al primer caracter de la anterior cadena, tenemos que hacerlo por los indices
# el primer indice de una cadena es el numero 0... asi
print(palabra[0])

# Támbien podemos mostrar en el indice 3
print(palabra[3])

# Podemos utilizar indices en negativo, los indices en negativo hacen referencia a partir del final
# de la cadena, siendo el -1 el indice del ultimo caracter de la cadena
print(palabra[-1])
print(palabra[-2])

# Nota: No podemos utilizar el indice -0 porque haria referencia al 0 (Son lo mismo)
print(palabra[-0])

# Tambien podemos acceder al primer caracter poniendole el indice -6 (segun la palabra "Python")
print(palabra[-6])

# Mientras que lo hicieramos de la forma tradicional, para obtener el primer caracter
# tendriamos que empezar a contar desde 0 y poner un 5
print(palabra[5])

# Python soporta diferentes tipos de indices con una tecnica llamada Slicing
# Slicing es util para sustraer porciones de otras cadenas.
# Ejemplo
# Recordar la siguiente variable
palabra = "Python"
# Tenemos que indicar un indice de inicio y un indice de fin
print(palabra[0:2])
# Muestra la palabra "Py", esto es porque al final excluye o sea el indice 2 excluye 

# Tambien podemos hacer desde el 2 hasta el final por ejemplo
print(palabra[2:-1])
# Muestra la palabra "tho"

# Si necesitariamos que imprima hasta el final simplemente se hace lo siguiente
print(palabra[2:])
# Cuando no se le indica el indice, python cogera por defecto la primera o la ultima posición incluyendola
print(palabra[:])
# Con el anterior comando se imprime la totalidad de la palabra, de otra forma seria asi
print(palabra[:2] + palabra[2:])

# Un ejemplo de slicing en negativo seria
print(palabra[-2:])

# Que pasaria si le indicamos un indice que se encuentra fuera del espacio que abarca una cadena, o sea
# la palabra "Python" tiene 6 caracteres, que pasa si.. (Se indica en comentario porque genera el sgt error)
# "El indice de la cadena se encuentra fuera del rango"
#print(palabra[99])

# Pero en estos casos, claro que se puede utilizar el slicing
print(palabra[:99])
print(palabra[99:])
# El anterior comando (ultimo) devolvera un espacio vacio, una cadena con nada, python interpreta que no hay
# ningun caracter en la posición 99 y de ahi hasta el "ultimo"

# Nota: Una cadena de caracteres en python es INMUTABLE, o sea que no se puede sustituir ninguno de sus
# caracteres individualmente...por ejemplo (Se indica en comentario porque genera el sgt error)
# El tipo cadena str (String) no soporta la asignación de objetos o items
#palabra[0] = "H"

# Pero con python no hay problema porque es muy flexible, se lo puede hacer asi...
palabra = "H" + palabra[1:]
print(palabra)

# En python existe una función llamada "len" viene de length
# Si le pasamos al metodo len una cadena de caracteres, esta es capaz de decirnos cuantos caracteres tiene
# Ejemplo
res = len("Cristian")
print(res)

# Igualmente funcionan con variables (la variable palabra se encuentra la palabra "Python")
res = len(palabra)
print(res)








