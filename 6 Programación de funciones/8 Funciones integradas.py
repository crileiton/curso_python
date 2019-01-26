# Las funciones integradas sirven para hacer conversiones entre tipos de datos y otras para manipular
#información...ejemplo

# Sabemos que cuando tenemos una cadena de caracteres podemos transformarla a un entero o a un flotante.

n = int('10')
f = float('3.14')

# Como hacemos al contrario, si queremos por ejemplo concatenar un numero con una cadena...asi..la funcion str()

c = 'Un texto y un numero entero ' + str(23) + ', y un numero flotante ' + str(3.1415)
print(c)

# Podemos tambien transformar un numero entero a binario... por ejemplo el numero 10
num = 10
resultado_binario = bin(10)
print(resultado_binario)
# El resultado es: 0b1010
# Los dos primeros caracteres quiere decir es que devuelve una cadena y que es un numero binario

# Tambien podemos devolver un numero en hexadecimal con la función hex
num = 10
resultado_hexadecimal = hex(10)
print(resultado_hexadecimal)
# El resultado es: 0xa
# 0x indica que es un numero hexadecimal

# Queriendo hacer operaciones
#otro = int(hex(87), 16) + int(hex(3), 16)
#print('El resultado es: ',hex(otro))

# Si queremos hacerlo inverso podemos transformar la cadena del binario o del hexadecimal utilizando la funcion int ...asi
print(int('0b1010', 2))

# O pasandole un hexadecimal
print(int('0xa', 16))

# Tambien tenemos la funcion llamada abs(), la cual nos devuelve el valor absoluto de un numero, el valor
#absoluto de un numero es la distancia y equivale a quitar el signo...ejemplo
print(abs(-30))
# sea positivo o negativo el argumento devuelve en positivo porque la distancia que hay desde -30 a 0 son 30 y de 30 a 0 tambien son 30

# Tambien tenemos las funciones de redondeo .. asi
res = round(5.4)
print(res)
# Respuesta: 5

# Evaluar una expresion en una cadena y esto soporta variables si se han declarado previamente (util)
print(eval('2+5'))
# Interpreta la cadena como una operación...resultado: 7
# Tambien soporta variables
n = 10
print(eval('n * 10 - 5'))
# Resultado: 95

# Para saber la longitud de una cadena o lista
print(len('Una cadena'))
print(len([1,2,3]))

# Una función anecdotica es la funcion help(), ayuda de python, esta en ingles
help()
