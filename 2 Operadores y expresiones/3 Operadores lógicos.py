# Not: Negación o tambien conocida como (No), solo afecta True o False
# Ejemplo: Negar algo verdadero
print(not True)
print(not True == False)
# Sirve para negar una expresión logica dandole el valor contrario

# Dificiles: Los logicos nos permite crear grandes expresiones
# Se presentan en dos formas
# Conjunción y disyunción

# Conjunción: Viene de conjunto, sinonimo de unido, contiguo o cercano
# Disyunción: Disyunto, sinonimo de separado, apartado o distante

# Operador que une es: AND
print(True and True) # True
print(True and False) # False
print(False and True) # False
print(False and False) # False

a = 7
print(a > 10 and a < 20)

# Ejemplo 2
c = "Hola mundo"
longitud = len(c)
print(longitud >= 5 and c[0] == "H")

#------------------------------------

# Operador que separa es: OR
print("Or",True or True) # True
print("Or",True or False) # True
print("Or",False or True) # True
print("Or",False or False) # False

# Ejemplo

s = "SALIR"
print(s == "EXIT" or s == "FIN" or s == "SALIR")

# Ejemplo 2

cadena = "Cristian"
print(cadena[0] == "c" or cadena[0] == "C")










