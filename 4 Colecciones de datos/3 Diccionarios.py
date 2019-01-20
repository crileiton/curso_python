"""# Los diccionarios son junto a las listas las colecciones mas utilizadas en python
# se basan en una estructura mapeada del ingles maping donde cada elemento de la colección se encuentra 
# identificado con una clave unica, por lo tanto no pueden aver dos claves iguales en el mismo diccionario
# en otros lenguajes se podria considerar arreglos asociativos.
# Para crear un diccionario podemos indicar siempre una clave, generalmente una cadena de caracteres y un valor
#para cada elemento, asi...

# Diccionario vacio
vacio = {}
print(vacio)
print(type(vacio))
# En la anterior linea de codigo miramos que el tipo de la variable vacio es de tipo diccionario

# Ejemplo: Diccionario de traducciones de colores
colores = {'amarillo':'yellow','azul':'blue','verde':'green'}
print(colores)

# Nota: Los diccionarios tambien son colecciones desordenadas

# Suponiendo que quiero saber la traducción del color amarillo, entonces...
print(colores['amarillo'])
# podemos ver que por consola da como respuesta yellow

# Tambien se puede con números
numeros = {10:'diez',20:'veinte'}
print(numeros[10])

# Tambien podemos modificar los registros en el diccionario
colores['amarillo'] = 'write'
print(colores)
# En consola podemos observar lo siguiente: {'amarillo': 'write', 'azul': 'blue', 'verde': 'green'}

# Tambien podemos borrar la clave y el valor
del(colores['amarillo'])
print(colores)
# En consola podemos observar lo siguiente: {'azul': 'blue', 'verde': 'green'}

# Ejemplo 2
edades = {'Cristian':22,'Juan':45,'Maria':34}
edades['Cristian'] += 1
print(edades)
# Podemos observar que la edad de cristian aumento en 1

# Tambien podemos hacer operaciones
suma_edades = edades['Juan'] + edades['Maria']
print(suma_edades)

# Tambien podemos recorrer todos los elementos de un diccionario con un bucle for
for edad in edades:
    print(edad)
# Cristian Juan Maria: Como se logra observar en el anterior for no se puede acceder a los valores, sino a los valores clave

# Para poder obtener los valores y no los valores claves se hace...
for clave in edades:
    print(edades[clave])

# Si queremos mostrar la clave y el valor...
for clave in edades:
    print(clave,edades[clave])

# Otra forma que es la debida es utilizando un metodo interno de los diccionarios llamado items...asi...
edades = {'Cristian':22,'Juan':45,'Maria':34}
for clave,valor in edades.items():
    print(clave,valor)
"""
# Lo mas utilizado es utilizarlo en conjunto con las listas para crear colecciones de datos avanzadas

# Ejemplo: Quiero crear una lista de personajes, cada personaje tiene un nombre, clase, raza. Podemos utilizar
#una mezcla entre diccionarios para guardar cada atributo o variable del personaje y luego introducir estos diccionarios
#dentro de una lista de personajes...asi

# 1. Crear la lista de personajes
personajes = []
# 2. Crear un personaje(Diccionario)
p = {'Nombre':'Gandalf','Clase':'Mago','Raza':'Humano'}
# en 'p' ya tengo un personaje que es un diccionario
# Podemos agregar este personaje a la lista de personajes
personajes.append(p)

# Vamos a crear mas personajes
p = {'Nombre':'Legolas','Clase':'Arquero','Raza':'Elfo'}
personajes.append(p)
p = {'Nombre':'Gimli','Clase':'Guerrero','Raza':'Enano'}
personajes.append(p)


# Podemos recorrer comodamente los personajes teniendo su información para manipularla o consultarla, por ejemplo

for p in personajes:
    print(p['Nombre'],p['Clase'],p['Raza'])
