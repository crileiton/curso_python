# Aparte de los metodos que podemos crear dentro de una clase tambien hay varios que son especiales
# como por ejemplo el metodo especial init que se ejecuta al crear una instancia por eso tambien se denomina 
# metodo CONSTRUCTOR

# Vamos a repasar el metodo init
class Pelicula:
    
    # Constructor de clase
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print("Se ha creado la pelicula: ", self.titulo)

#p = Pelicula("El Padrino", 175, 1972)

# De la misma forma que existe el metodo constructor, tambien existe el metodo destructor que se ejecuta al borrar
# una instancia, por defecto el destructor pasa desapercibido pero podemos sobreescribirlo para ejecutar algun tipo de
# instrucción...ejemplo

class Pelicula2:
    
    # Constructor de clase
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print("Se ha creado la pelicula: ", self.titulo)

    # Destructor de la clase ( Solo se ejecuta cuando se borre una instancia)
    def __del__(self):
        print("Se esta borrando la pelicula:",self.titulo)


p = Pelicula2("El Padrino", 175, 1972)
# Si ejecutamos precisamente en este momento observamos lo siguiente:
# Se ha creado la pelicula:  El Padrino
# Se esta borrando la pelicula: El Padrino

# Pero porque se muestra el mensaje del metodo destructor, sin ejecutarlo manualmente?
# Precisamente porque cuando finaliza el programa se eliminan de la memoria todas las instancias de todos
#los objetos que existen
# por eso se ejecuta automaticamente el destructor 
# Para eliminar manualmente la instancia se utiliza el siguiente codigo
# del(p)

# ---------------------------------------------------------------------------------

# Otro metodo especial es el metodo string
# es lo que ocurre cuando le pasamos una cadena str un valor y lo convierte a una cadena de caracteres
# Ejemplo el siguiente numero lo convierte a una cadena
print(str(10))

# Los objetos de la clase tambien podemos redefinir esta string
# Ejemplo si pasamos el objeto p a string obtenemos lo siguiente... <__main__.Pelicula2 object at 0x002EB050>
print(str(p))
print("Empieza la clase 3")
# Esto <__main__.Pelicula2 object at 0x002EB050>  es una referencia a una instancia del tipo pelicula que esta
# almacenado en esta dirección de memoria 0x002EB050

# Podemos redeclarar esta función string para mostrar algo mas interesante al momento de transformar un objeto a cadena
# redefinimos la clase con su metodo string asi...

class Pelicula3:
    
    # Constructor de clase
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print("Se ha creado la pelicula: ", self.titulo)

    # Destructor de la clase ( Solo se ejecuta cuando se borre una instancia)
    def __del__(self):
        print("Se esta borrando la pelicula:",self.titulo)

    # Redefinimos el metodo string
    def __str__(self):
        return "{} lanzada en {} con una duracion de {} minutos".format(self.titulo, self.lanzamiento, self.duracion)

p3 = Pelicula3("El Padrino", 175, 1972)

print(str(p3))

# Del anterior codigo obtenemos: El Padrino lanzada en 1972 con una duracion de 175 minutos

# Otro metodo muy especial es len()
# Este metodo suele decirnos la longitud, pero tambien podemos adaptarlos a nuestros objetos
# Ejemplo: Podemos hacer que len nos diga cuanto dura una pelicula 
# Si ejecutamos lo siguiente
#len(p3)
# Miramos que genera error dado que tenemos que sobreescribirlo...asi

class Pelicula4:
    
    # Constructor de clase
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print("Se ha creado la pelicula: ", self.titulo)

    # Destructor de la clase ( Solo se ejecuta cuando se borre una instancia)
    def __del__(self):
        print("Se esta borrando la pelicula:",self.titulo)

    # Redefinimos el metodo string
    def __str__(self):
        return "{} lanzada en {} con una duracion de {} minutos".format(self.titulo, self.lanzamiento, self.duracion)

    # Redefenir el método Length
    def __len__(self):
        return self.duracion

p4 = Pelicula4("El Padrino", 175, 1972)
print(len(p4))
# Del anterior codigo observamos el siguiente resultado: 175