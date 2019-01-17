# La palabra relacional = comparar dos valores

# Igual que
print(3 == 2)

# Diferente que
print(3 != 2)

# Mayor que
print(3 > 2)

# Menor que
print(3 < 2)

# Mayor o igual que
print(3 >= 2)

# Menor o igual que
print(3 <= 2)

# Tambien con variables
a = 10
b = 5
print(a > b)
print(a != b)
print(a == b * 2)

# Tambien es posible comparar cadenas de texto.
# Ejemplo
print("Cadena","Hola" == "hola")
print("Cadena","Hola" != "hola")

# Si guardamos texto en una variable, tambien podemos comparar con indices
c = "Hola"
print("Indices",c[0] == "H")
print("Indices",c[-1] == "H")

# Tambien podemos trabajar con listas
l1 = [0,1,2]
l2 = [2,3,4]
print("Listas",l1 == l2)
print("Listas",len(l1) == len(l2))
print("Listas",l1[-1] == l2[0])

# Igualmente existe con lógicos
print("Logicos",True == True)
print("Logicos",True == False)
print("Logicos",True != False)

# Los siguientes ejemplo dan como resultado True y False
# Porque aritmeticamente hablando True = 1 y False = 0
print("Logicos",True > False)
print("Logicos",False > True)
print("Logicos",True * 3)
print("Logicos",True * False)