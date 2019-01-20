# Primero se debe entender el funcionamiento una pila es una coleccion de elementos ordenados 
# Su peculiaridad es que solo permite 2 opciones
# 1. Añadir un elemento a la pila
# 2. Sacar un elemento de la pila
# Lo interesante de la pila es que el ultimo en entrar es el primero en salir
# Una pila en Python se hace asi...

pila= [3,4,5]
# Acontinuación añadiremos elementos a la pila con el append
pila.append(6)
pila.append(7)
# Ahora viene lo peculiar a la hora de extraer elementos de la pila (para sacar se utiliza el metodo pop())
# pop() devuelve el ultimo elemento de la lista de nuestra "pila" y lo borra...asi
pila.pop()
# Como se logra observar ya no existe el numero 7 dentro de la lista

# Nota: Si queremos guardar el elemento que sacamos de la pila debemos de hacer esto...
n = pila.pop()
print(n)

# COLAS
# Una cola es una colección donde el primer elemento en entrar, es el primero en salir(fila de un banco)
# Se declara asi...
# Debido a que no es muy utilizada se debe importar esta colección manualmente de la libreria de colecciones de python
from collections import deque
cola = deque()
cola = deque(['Cristian','Juan','Miguel'])
cola.append('Maria')
cola.append('Hernando')
# El metodo para extraer es popleft
cola.popleft()
print(cola)
# Podemos ver que en la cola ya no existe Cristian