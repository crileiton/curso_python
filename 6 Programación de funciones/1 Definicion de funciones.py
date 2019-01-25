# La definición es asi...
# Al igual que con las variables lo recomendable para elegir el nombre de una función es utilizar minusculas
#y palabras separadas con barras bajas en caso de que queramos poner espacios, idealmente utilizar nombres autoexplicativos
#NO utilizar nombres que no sepamos lo que son como por ejem... letras o una palabra que no tenga sentido con lo que hace la funcion

def saludar():
    print("Hola! este print se llama desde la función saludar")

saludar() 

# Dentro de una función podemos crear variables y utilizar cualquier sentencia... ejemplo...
# Crear una función que dibuje la tabla del numero 5

def dibujarTablaDelCinco():
    for i in range(11):
        print("5 * ", i, "=", i * 5)

dibujarTablaDelCinco()

# Otra cosa que debemos aprender sobre las funciones es el ambito de sus variables, por ejemplo

def test():
    n = 10
test()
#print(n)
# Con la anterior linea queriamos imprimir el valor de n, pero las variables de una funcion solo estan disponibles
#dentro de la función por eso genera error

m = 10
def testa():
    print(m)

testa()

# En el anterior codigo podemos ver que si se ejecuta la variable m que esta declarada aparte, todo esto sucede a que
#la variable se encuentra declarada fuera de la función, por tanto abarca tambien la función, el ambito tambien abarca todo
#lo que hay por debajo y por lo tanto se puede utilizar dentro de las otras funciones que nos encontremos

# Otro ejemplo
def testu():
    print(l)

l = 10
testu()