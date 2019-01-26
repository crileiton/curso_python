# Normalmente en nuestros programas pueden a ver u ocurrir varios tipos de fallos y siempre que ocurre uno,
# python nos mostrara que a ocurrido algo extraordinario y que se ha detenido la ejecución del programa

# Errores sintacticos: ligados a la sintaxis, la cual es la escritura de las instrucciones, cerrar un parentesis, dos puntos, etc

#print('Hola'

# Errores de nombre 
#pint('Hola')

# Los errores sintacticos se pueden identificar facilmente antes de ejecutar el programa, la mayoria de entornos
#de desarrollo nos avisan de que algo no anda bien para que lo arreglemos o lanza el error con el aviso 

# Sin embargo existen otros errores que no se distinguen tan facilmente, porque a primera vista no hay nada mal

# ERRORES SEMANTICOS

# Estos fallos van mas ligados al sentido del uso, algo que para nosotros deberia ser correcto la mayoria de situaciones
# pero que en algun momento bajo una determinada sircunstancia pueden no funcionar como se espera

# Ejemplo: tenemos una lista con varios elementos y lo sacamos con el metodo pop

lista = [1,2,3]
lista.pop()
lista.pop()
lista.pop()

#print(lista)
# Ahora mismo la lista estará vacia, que sucede si intentamos hacer otro pop en una lista vacia
#lista.pop()
# Pues salta un error: IndexError: pop from empty list
# Este tipo de errores pueda que a primera vista pasen desapercibidos por tanto esta en nuestra mano prevenir que ocurran estas cosas

# En este caso seria tan sencillo como comprobar si la longitud de una lista es mayor que 0 antes de intentar sacar un elemento

lista_2 = [1,2,3,4,5]

if len(lista_2) > 0:
    lista_2.pop()
    lista_2.pop()
    lista_2.pop()
    lista_2.pop()
    lista_2.pop()
 #   lista_2.pop()
else:
    print("No hay más elementos en la lista")

#print(lista_2)


# Otro ejemplo que ya conocemos ocurre cuando leemos un valor por teclado e intentamos realizar una operación matematica
#directamente sin convertirlo a un numero ...ejemplo
"""
n = input("Introduce un número:\n")
m = 4

print("{}/{}={}".format(n, m, n / m))
"""
# Del anterior codigo tenemos un error: TypeError: unsupported operand type(s) for /: 'str' and 'int'

# Tenemos que convertir a flotante.. asi

n = float(input("Introduce un número:\n"))
m = 4

print("{} / {}={}".format(n, m, n / m))

# Si ingresamos un numero entero o flotante estaria bien, pero si el usuario ingresa un texto? ejemplo: aaa
# NO se puede convertir a flotante una cadena de texto con 3 aaa, No hay una forma magica para asegurarnos de que el
#usuario ingrese numeros, por eso salta el error
# ¿Existe alguna otra solución?
# SI creando estados de excepción que sigan ejecutandose aunque ocurra un error 