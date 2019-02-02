# Solución de ejercicio de coordenadas
import math

class Punto:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    # Metodo para verificar en que cuadrante se encuentra el punto
    def darCuadrante(self):
        if (self.x > 0 and self.y > 0):
            print("{} pertenece al cuadrante No. 1".format(self))
        elif (self.x < 0 and self.y > 0):
            print("{} pertenece al cuadrante No. 2".format(self))
        elif (self.x < 0 and self.y < 0):
            print("{} pertenece al cuadrante No. 3".format(self))
        elif (self.x > 0 and self.y < 0):
            print("{} pertenece al cuadrante No. 4".format(self))
        else:
            print("{} pertenece al origen".format(self))
    
    def darVector(self, p):
        print("El vector entre {} y {} es: ({}, {}) ".format(self, p, p.x - self.x, p.y - self.y))

    def darDistancia(self, p):
        d = math.sqrt( (p.x - self.x) ** 2 + (p.y - self.y) ** 2 )
        print('La distancia entre {} y {} es {}'.format(self, p, d)) 

A = Punto(2, 3)
B = Punto( 5, 5)
C = Punto(-3, -1)
D = Punto(0, 0)

# Consultar a que cuadrante pertecenece
#A.darCuadrante()
#B.darCuadrante()
#C.darCuadrante()
#D.darCuadrante()

# Consultar los vectores AB y BA
#A.darVector(B)
#B.darVector(A)

#Consultar la distancia entre 'A y B' y 'B y A'
#A.darDistancia(B)
#B.darDistancia(A)

# Cual de los tres puntos A, B o C se encuentra mas lejos del origen (El punto B se encuentra mas lejos)
#A.darDistancia(Punto(0,0))
#B.darDistancia(Punto(0,0))
#C.darDistancia(Punto(0,0))
#D.darDistancia(Punto(0,0))

class Rectangulo:
    def __init__(self, pInicial = Punto(), pFinal = Punto()):
        self.pInicial = pInicial
        self.pFinal = pFinal
    
    def darBase(self):
        self.base = abs(self.pFinal.x - self.pInicial.x)
        print("La base del rectangulo es {}".format(self.base))
    
    def darAltura(self):
        self.altura = abs ( self.pFinal.y - self.pInicial.y )
        print("La altura del rectangulo es {}".format(self.altura))

    def darArea(self):
        self.base = abs(self.pFinal.x - self.pInicial.x)
        self.altura = abs ( self.pFinal.y - self.pInicial.y )
        self.area = self.base * self.altura
        print("El area del rectangulo es {}".format(self.area))

R = Rectangulo(A, B)
R.darBase()
R.darAltura()
R.darArea()