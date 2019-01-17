# La lectura por teclado se utiliza para programas de consola, la instrucción input permite 
# guardar un valor en una variable que nosotros introduzcamos por teclado
# Ejemplo
#valor = input()
#print(valor)
# Se puede guardar numeros o tambien cadenas de caracteres (si ingresa un numero en consola, sera texto)

# Tambien podemos mostrar un texto con el input, por ejemplo
#dato = input("Digite un valor")
# Si intentamos operar el dato con un número, dara error.
#r = dato + 100
#print(r)
# Dice que no se puede sumar un entero a una cadena

# Para poder trabajar con forma de datos que queramos se hace lo siguiente
# si sabemos que vamos a introducir una cadena que es un número.
dato = input("Introduce un número entero\n")
# Lo que se hace es convertir el valor anterior a entero...asi
dato = int(dato)
# con el anterior comando ya tenemos el valor ingresado como entero.
# y ya se puede operar...asi
r= dato + 100
print(r)

#_____________________-----------------------__________________________

# Ingresamos en consola un valor flotante en vez de entero, generara un error porque interpreta que el
# valor no es entero (se comenta porque genera error)
"""print("-------------------------------------")
dato2 = input("Introduce un número entero\n")
dato2 = int(dato2)
r2= dato2 + 100
print(r2)"""

#Para arreglarlo se debe hacer lo siguiente
print("-------------------------------------")
dato2 = input("Introduce un número decimal\n")
dato2 = float(dato2)
r2= dato2 + 100
print(r2)

#-----------------------------------------------
# No hace falta hacer todo el tiempo el anterior trabajo, basta con lo siguiente
print("-------------------------------------")
dato3 = float(input("Ingrese un valor entero\n"))
r = dato3 + 50
print(r)
