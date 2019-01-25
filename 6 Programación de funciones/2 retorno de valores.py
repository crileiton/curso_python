# ¿Como podemos conectar una función con el exterior?
# Res= RETORNANDO VALORES

# Vamos a crear una funcion en la que simplemente vamos a utilizar la sentencia return y el valor o valores que queremos devolver

def prueba():
    return "Una cadena retornada"
#print(prueba())

# Debemos tener en cuenta que al utilizar el return la funcion devolverla el valor y finalizara en ese momento (como un break)

c = prueba()
#print(c)

#d = prueba() + 10
# La anterior linea de codigo genera error dado a que no se puede sumar texto y numeros

# Algo interesante ocurre cuando devolvemos una lista o cualquier colección ya que podemos utilizarla directamente desde la funcion
# y se ve esteticamente muy raro y funciona incluso con el slicing.. ejemplo
def cristian():
    return [1,2,3,4,5]

print(cristian())

# Pero tambien podemos hacer esto...
print(cristian()[1:4])
# Lo anterior no es muy util ya que estaremos ejecutando la funcion cada vez que consultamos un valor, es mejor
#asignar el resultado a una variable...asi...
l = cristian()
print(l[-1])

# Las funciones pueden devolver multiples valores separados por (,) ... muy interesante

def mauricio():
    return "Una cadena",20,[4,5,6]

print(mauricio())
# El resultado es el siguiente: ('Una cadena', 20, [4, 5, 6]) ... es una TUPLA

# Y la tupla nos permite realizar asignación multiple ... o sea...
# Podemos asignar el resultado de la funcion mauricio a una variable cadena, otra variable entera y otra variable lista

cadena,numero,lista = mauricio()
print(cadena)
print(numero)
print(lista)