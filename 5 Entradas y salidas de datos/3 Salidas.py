"""v = 'Otro texto'
n = 10
#print('Un texto',v,'y un numero',n)
c = "Un texto {} y un numero {}".format(v,n)
print(c)

# Otra forma de mostrar datos es referenciando el orden
d = "Un texto {1} y un numero {0}".format(v,n)
print(d)

#Otra forma de simplificar es asi...
e = "Un texto {texto} y un numero {numero}".format(texto = v, numero = n)
print(e)

# Supongamos que queremos mostrar una palabra en una cadena de 20 caracteres y la queremos alinear a la derecha
print("{:>30}".format("palabra")) # Alineamiento a la derecha y 30 espacios
# Resultado:                        palabra.
print("{:<30}".format("palabra")) # Alineamiento a la izquierda y 30 espacios
# Resultado: palabra                       .
print("{:^30}".format("palabra")) # Alineamiento al centro y 30 espacios de lado y lado
# Resultado:            palabra            .

# Truncamiento
# Imaginar que tenemos una palabra y queremos mostrar solo unos caracteres del principio por ejemplo...
print("{:.3}".format("palabra")) # Truncamiento a 3 caracteres
# Resultado: pal

# Truncamiento y alineamiento
print("{:>30.3}".format("palabra")) # Truncamiento a 3 caracteres y alineamiento a la derecha 30 caracteres
# Resultado:                            pal.
"""
# La mejor utilidad del format a parte del anterior es el formateo de numeros, podemos rellenar espacios de numeros
#enteros alineados a la derecha o izquierda con ceros 

# Podemos redondear o recortar numeros decimales y rellenarlos con 0 o espacios 

#Ejemplo: Formateo de número entero, rellenando con espacios.
# Quiero mostrar el numero 1000 el 100 y el 10 y que todos ocupen 4 caracteres y que se rellenen los espacios
#en blanco con espacios y todos alineados a la derecha porque son numeros
print("{:4d}".format(10))
print("{:4d}".format(100))
print("{:4d}".format(1000))
# Resultado:
#  10
# 100
#1000

#rellenado con 0 y todos alineados a la derecha porque son numeros
print("{:04d}".format(10))
print("{:04d}".format(100))
print("{:04d}".format(1000)) 
# Resultado:
#0010
#0100
#1000

# Tambien podemos formatear numeros flotantes
# Ejemplo formateo de numeros flotantes y rellenados con espacios
print("{}".format(3.1415926))
# Suponiendo que queremos recortar por ejemplo a 2 decimales
print("{:.2f}".format(3.1415926))
# Suponiendo que queremos recortar por ejemplo a 3 decimales
print("{:.3f}".format(3.1415926))

# Ahora llenando espacios
print("{:.3f}".format(153.21))
# Si le decimos 3 decimales a un numero que no tenga 3 decimales lo rellena con 0 asi...
# Resultado: 153.210


# Suponiendo que tengo los numeros...
#3.142
#153.210
# y quiero que esten alineados con el punto, lo primero que hay que hacer es 
print("{:7.3f}".format(3.1415926))
print("{:7.3f}".format(153.21))
# Resultado:
#  3.142
#153.210
# El truco esta en contar los caracteres del numero mas largo y aplicar a todos, en este caso es 7

# Si quisieramos rellenar igualmente pero con 0, se hace lo siguiente...
print("{:07.3f}".format(3.1415926))
print("{:07.3f}".format(153.21))
# Resultado:
#003.142
#153.210