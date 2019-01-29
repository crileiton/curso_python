# En python todo absolutamente es un objeto 
# Primero se realizara un caso de estudio realizado en programación estructurada y despues con programación orientada a objetos

# Caso de estudio:
# Nos piden crear un registro para manejar los clientes de una empresa con su nombre, apellidos y su dni 
# y el programa debe permitirnos mostrar los datos de los clientes o borrarlos a partir de su dni o bien el echo
# de que todavia no hemos trabajado los ficheros ni las bases de datos, se obtara por crear una lista con diccionarios
# asi como los ejemplo que vimos anteriormente

# 1. Crear una lista

clientes = [
    {'Nombre':'Cristian', 'Apellidos':'Leiton Valencia', 'dni':'11111111A'},
    {'Nombre':'Daniela', 'Apellidos':'Rodriguez Ceron', 'dni':'22222222A'}
]

# Con el anterior codigo ahora ya podemos consultar los clientes
# print(clientes)

# 2. Ahora que tenemos un par de clientes la primera funcionalidad sera mostrar la información de un cliente
# apartir de su dni...como podemos hacerlo...pues normalmente podemos hacerlo con una función a la que pasariamos a 
# la lista de clientes y un dni para que ella se encargue de buscarlo...asi...

def mostrar_Cliente(clientes,dni):
    for cliente in clientes:
        if (dni == cliente['dni']):
            print('{} {}'.format(cliente['Nombre'],cliente['Apellidos']))
            return
    print('Cliente no encontrado')

#mostrar_Cliente(clientes,'11111111A')

# y de esta manera nos devolvera Cristian Leiton Valencia si ejecutamos: mostrar_Cliente(clientes,'11111111A')

# Tambien podemos hacer lo mismo para borrar un cliente...asi

def borrar_Cliente(clientes,dni):
    # Para poder afectar a la lista se utiliza el enumerador conservando el indice (i = indice) 
    for i, cliente in enumerate(clientes):
        if (dni == cliente['dni']):
            # Si encuentra un cliente con el dni que estamos buscando, borramos el cliente de la lista pasandole 
            # el elemento del indice actual 
            del(clientes[i])
            print(str(cliente),"> BORRADO")
            return
    print('Cliente no encontrado')
# Si ejecutamos la siguiete función podemos observar que el cliente cristian queda eliminado
borrar_Cliente(clientes,'11111111A')
# Verificamos nuevamente la lista y aparece unicamente el cliente Daniela
print(clientes)

# A la larga el anterior codigo se vuelve un tanto confuso porque se genera mucho codigo, mucha documentación 
# haciendo referencia a todas las posibles funciones que van a servir para manejar los clientes y como utilizarlas
# Lo anterior es una idea de como funciona la programación estructurada