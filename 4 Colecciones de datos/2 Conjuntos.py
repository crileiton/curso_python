# Son colecciones desordenadas de elementos unicos, se utiliza normalmente para hacer pruebas de pertenencia a
#grupos y eliminación de elementos duplicados
# Tambien soportan operaciones matematicas avanzadas (posterior)

# Se declara asi...
conjunto = set()
print(conjunto)

# Podemos crear un conjunto con varios elementos tambien si son escritos entre llaves...asi
conjunto = {1,2,3}
print(conjunto)

# Se dice que los conjuntos son desordenados porque a medida que añadimos elementos a un conjunto este orden no se conserva
#como si ocurre con las listas

# Algunos de sus metodos son...

# Metodo add
conjunto.add(4)
print(conjunto)
# Como se puede observar lo añadio al final, pero que pasa si añado un 0, teoricamente se debe añadir al final pero...j
conjunto.add(0)
print(conjunto)
# Como podemos ver se añadio al principio
# Si en lugar de añadir un numero añado una letra o texto
conjunto.add('H')
print(conjunto)
# Se puede observar que primero coloca todos los numeros y luego todas las letras
conjunto.add('A')
print(conjunto)
conjunto.add('Z')
print(conjunto)
# Se logra observar {0, 1, 2, 3, 4, 'A', 'Z', 'H'}

# Una forma de saber si algo existe en un grupo es asi...(como respuesta obtenemos True o False)
grupo ={'cristian','dani','gabo'}
print('dani' in grupo)

# Se puede hacer lo contrario
print('dani' not in grupo)

# Nota: Una caracteristicas de los conjuntos es que no pueden haber elementos repetidos dentro de él.
test ={'cristian','cristian','cristian'}
print(test)
# Se puede observar que unicamente deja un elemento 'cristian'

# Se tiene la siguiente lista
lista = [1,2,3,3,2,1]
print(lista)
# Si transformamos la anterior lista a un conjunto
c = set(lista)
print(c)
# Lo que se puede observar es que se han eliminado los elementos repetidos

# Ahora lo que se puede hacer es convertir nuevamente el conjunto a una lista
lista_5 = list(c)
print(lista_5)

# Y ya tenemos echa la conversion directa, pero se la puede hacer en una linea asi...
miLista = [1,2,3,3,2,1]
miLista = list(set(miLista))
print(miLista)

# Este concepto tambien funciona con cadenas de caracteres asi...
cadena = "Al pan pan y al vino vino"
cadena_conver = set(cadena)
print(cadena_conver)




