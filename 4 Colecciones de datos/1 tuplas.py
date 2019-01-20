# Son colecciones parecidas a las listas con la diferencia de que son inmutables,
# Se utiliza para asegurar que al terminar los datos no se pueden modificar,
# Python utiliza tuplas en algunas funciones para devolver resultados inmutables 
# Se declara asi

tupla = (100,"Hola",[1,2,3,4,5],-50)
print(tupla)

# Las tuplas aceptan indexación y slicing
print(tupla[0])
print(tupla[-1])
print(tupla[1:-1])
print(tupla[2:])

# Acceder a los valores internos de la lista
print(tupla[2][0])

# Ejemplo de que el valor de una tupla no se puede redefinir
# tupla[0] = 50

# Si es posible saber la longitud
print(len(tupla))

# O la longitud de la lista dentro de la tupla
print(len(tupla[2]))

# Podemos utilizar el index para buscar un elemento y saber su posición pero devolvera un error si no lo encuentra
print(tupla.index(100))
# Nos dice que se encuentra en la posición 0

# Tambien podemos buscar con el index pasandole una cadena
print(tupla.index('Hola'))
# Nos dice que se encuentra en la posición 1

# Pero si intentamos buscar el indice de un elemento que no esta en la tupla, nos da un error - ValueError: tuple.index(x): x not in tuple
#print(tupla.index('ola'))

# Otra caracteristicas es el count el cual permite contar el numero de elementos repetidos o no que hay en una tupla
print("aqui",tupla.count(100))
# Nos dira que el numero 100 se encuentra 1 vez

# Ejemplo con algo que no este
print("aqui",tupla.count(200))
# Nos dira que el numero 200 se encuentra 0 veces

# Redeclaramos la tupla y podemos elementos repetidos

tupla = (100,100,100,50,10)
print(tupla.count(100),"redeclarado")
# Nos dira que el numero 100 se encuentra 3 veces

# Si intentamos realizar un tupla.append nos dira error...asi AttributeError: 'tuple' object has no attribute 'append'
#tupla.append(10)