#
class Pelicula:
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print("Se ha creado la pelicula:",self.titulo)

    def __str__(self):
        return '{} ({})'.format(self.titulo, self.lanzamiento)

class Catalogo:
    peliculas = []

    def __init__(self, peliculas=[]):
        self.peliculas = peliculas
    
    def agregar(self, p):
        self.peliculas.append(p)
    
    def mostrar(self):
        for p in self.peliculas:
            print(p)

p = Pelicula('El Padrino', 175, 1972)

c = Catalogo([p])

c.mostrar()
# Importante lo de abajo...
c.agregar(Pelicula("El Padrino 2", 202, 1974))
c.mostrar()