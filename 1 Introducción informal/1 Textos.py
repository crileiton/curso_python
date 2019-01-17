# Los textos se conocen como cadenas de caracteres y pueden expresar de varias formas,
# Escencialmente se puede escribir un texto con comillas simples o comillas dobles

# Ejemplo
print('Hola mundo')
print("Hola mundo")

# Los motivos básicos de porque hay dos formas de escribirlo es porque podriamos utilizar dentro de una
# cadena que esta escrita con comillas simples...comillas dobles
# Ejemplo
print('Este texto incluye unas ""')

# Podemos hacer algo distinto, si se quiere utilizar comillas simples dentro del texto, podemos escribirlo
# entre comillas dobles.
# Ejemplo
print("Esta 'palabra' se encuentra entre comillas simples")

# Támbien es posible utilizar comillas dentro de las comillas del mismo tipo, siempre y cuando se utilice
# un caracter, llamado caracter de escape o de evación "escape"
# Tenemos que poner una barra invertida \ delante de cada comilla doble, para que detecte que todo es texto
# Ejemplo
print("Esta \"palabra\" se encuentra escrita entre comillas dobles")


# De la misma manera se puede hacer lo mismo con comillas simples ''
print('Esta \'palabra\' se encuentra escrita entre comillas dobles.')

# La función print tiene muchas ventajas, ademas nos permite imprimir caracteres especiales
# tales como tabulaciones, saltos de líneas.
# Los caracteres "\t" del ejemplo sirve para crear una tabulación
# Ejemplo
print("Un texto\tuna tabulación")

# Si quisieramos lo mismo pero con un salto de línea podriamos escribir lo siguiente
print("Un texto\nuna nueva linea")

# Imaginate el caso que queramos mostrar por pantalla una carpeta o directorio de nuestro ordenador
# lo normal seria lo siguiente
print("c:\nombre\directorio")
# Como se puede observar surge un error debido a que hace un salto de linea.
# Entonces como se puede evitar que nos interprete los caracteres especiales?... así...
# Necesitamos indicarle que la cadena es de tipo raw (crudo) o sea que no la queremos procesar
print(r"c:\nombre\directorio")

# Mostrar una cadena en diferentes lineas muy facilmente
print("""Una linea
otra linea
otra linea mas""")

# Nota: Las cadenas de texto igual que los números son datos y tambien pueden asignarse a una variable
c = "Esto es una cadena\n con dos lineas"
print(c)

# Otro dato importante es que podemos operar texto
d=c + c
print(d)

# EL siguiente ejemplo es valido
s = "Una cadena " "compuesta por dos cadenas"
print(s)
# Pero con variables es erroneo (se la comenta con 3 comillas porque daba error)
"""c1 = "Una cadena"
c2 = "Otra cadena"
print(c1 c2)"""

# Tambien es erroneo lo siguiente (se la comenta con 3 comillas porque daba error)
"""c1 = "Una cadena"
c2 = "otra cadena"
print(c1 "otra cadena")"""

# Lo siguiente es lo correcto
c1 = "Cristian"
c2 = " Leiton"
print(c1 + c2)

# Igualmente esto tambien es correcto
c1 = "Cristian"
c2 = " Leiton"
print(c1 + " Valencia")

# Igualemente se puede multiplicar cadenas
diez_espacios = " " * 10
print(diez_espacios + "Adelante hay 10 espacios")

