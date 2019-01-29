# Estamos deacuerdo que una galleta es diferente a otras, pero no cabe duda que tienen mucho en comun
# forma, color, proceso pero se diferencian en el sabor o una es mas dulce que otras
"""
# El valor de estos atributos es lo que diferencia cada galleta de las otras y la hace unica y especial.
# La gracia de la programación orientada a objetos es que los objetos tambien pueden tener sus propios atributos,
# una especie de variables internas a las que nos podemos referir a ellas con un puntito y el nombre del atributo
# lo mejor es que si este no existe se creara automaticamente dentro de la instancia del objeto y podremos utilizarlo
# Ejemplo...

class Galleta():
    pass

una_galleta = Galleta()

# Ahora podemos crear un nuevo sabor a esta galleta (galleta de arriba)
una_galleta.sabor = 'Salado'
una_galleta.color = 'Marrón'

# Ahora podemos dirigirnos a estos atributos simplemente con un puntito asi...
print("El sabor de esta galleta es:",una_galleta.sabor)


# Aparte de definirlos fuera, tambien podemos definirlos directamente en la clase y darle un valor por defecto
# compartido por todas las instancias...ejemplo...

class Galleta():
    chocolate = False

galleta = Galleta()
print(galleta.chocolate)
# Ejecutando la anterior linea de codigo, nos dice que la galleta no tiene chocolate asi... False

# Ahora si yo pusiera esto...
galleta.chocolate = True
print(galleta.chocolate)
# Pues entonces la galleta ya tiene chocolate

# Pero claro añadir de uno en uno los atributos es un poco engorroso, por eso lo interesante seria establecerlos
# en el momento de crear el objeto y para hacerlo antes tenemos que introducir conceptos nuevos ...asi...

# Metodo especial llamado: init
# Palabra reservada: self

# Vamos a crear nuevamente la clase y vamos a introducir los conceptos anteriores

class Galleta():
    chocolate = False
    # Aqui viene el metodo init...asi...
    def __init__(self):
        print("Se acaba de crear una galleta.")

g = Galleta()
# Respuesta: Se acaba de crear una galleta.

# El metodo init es una función interna de la clase
# Este metodo se comparte por todos los objetos de la misma clase
# y concretamente el metodo init es un metodo especial que se ejecuta al crear un objeto
# permite ademas enviarle argumentos durante la instanciación y como se puede suponer los metodo especiales
# se escriben con 2 rayas bajar delante y atras

# En cuanto a la palabra self que tienen todos los metodos sean especiales o no, hace referencia al propio objeto
# y sirve para diferenciar entre el ambito de clase y el de un metodo, es un requisito implicito en todos los metodos 
# ya que por defecto al llamar cualquier metodo se pasa automaticamente al propio objeto
# esto ocurre de forma transparente en la llamada pero es obligatoria la definición 

# Ejemplo...
class Galleta():

    chocolate = False

    def __init__(self):
        print("Se acaba de crear una galleta.")

# Quiero crear un metodo propio..ejemplo

    def chocolatear(self):
        chocolate = True

g = Galleta()
g.chocolatear()
print(g.chocolate)

# Ejecutando el anterior codigo da como respuesta lo siguiente:
# Se acaba de crear una galleta.
# False

# Si acabamos de chocolatear la galleta, ¿porque aparece chocolate en False?
# el atributo chocolate que esta dentro del metodo chocolatear en realidad no hace referencia al chocolate 
# que se encuentra en la clase (mas arriba) sino a una variable interna de la función chocolatear

# Para poder acceder al atributo de clase tenemos que referirnos asi...
class Galleta():

    chocolate = False

    def __init__(self):
        print("Se acaba de crear una galleta.")

# Quiero crear un metodo propio..ejemplo

    def chocolatear(self):
        # ---cambio---
        self.chocolate = True

g = Galleta()
g.chocolatear()
print(g.chocolate)

# Si ejecutamos el anterior codigo tenemos como respuesta:
# Se acaba de crear una galleta.
# True

# Ahora ya tenemos que chocolatear cambia el atributo interno de la galleta (el de arriba)
# y por eso devolvio verdadero

# Ahora vamos a crear otro metodo interno...asi...
class Galleta():

    chocolate = False

    def __init__(self):
        print("Se acaba de crear una galleta.")

# Quiero crear un metodo propio..ejemplo

    def chocolatear(self):
        # ---cambio---
        self.chocolate = True

    def tiene_chocolate(self):
        if (self.chocolate):
            print("Soy una galleta chocolateada =D ")
        else:
            print("Soy una galleta sin chocolate =( ")


g = Galleta()
g.tiene_chocolate()
g.chocolatear()
g.tiene_chocolate()

# La respuesta al anterior codigo es:
# Se acaba de crear una galleta.
# Soy una galleta sin chocolate =( 
# Soy una galleta chocolateada =D 

# Gracias al self podemos hacer referencia al propio objeto y asignar unos cuantos atributos en la propia creación
# Ejemplo...
# Dado a que el metodo init se llama por defecto, vamos a hacer lo siguiente...

class Galleta():

    chocolate = False

    # --- cambio ---
    # Aumento de parametros: de esta forma vamos aceptar sabor y color y los vamos asignar dentro del init a unos
    # atributos que podemos crear aqui mismo dentro del init ( para que sean atributos de clase debe tener el self) ...asi

    def __init__(self, sabor, color):
        # el valor despues del igual hace referencia a las de función (función init)
        # y las primeras a las de la clase (son distintas)
        self.sabor = sabor
        self.color = color
        # --- cambio ---
        print("Se acaba de crear una galleta {} y {}".format(sabor,color))

# Quiero crear un metodo propio..ejemplo

    def chocolatear(self):
        # ---cambio---
        self.chocolate = True

    def tiene_chocolate(self):
        if (self.chocolate):
            print("Soy una galleta chocolateada =D ")
        else:
            print("Soy una galleta sin chocolate =( ")


g = Galleta('Salada', 'Marron')
g.tiene_chocolate()
g.chocolatear()
g.tiene_chocolate()

# La salida del anterior codigo es:
# Se acaba de crear una galleta Salada y Marr�n
# Soy una galleta sin chocolate =( 
# Soy una galleta chocolateada =D 
"""
# Aun con el anterior codigo tenemos problemas si quisieramos crear una galleta sin atributos o sea asi...
# otra_galleta = Galleta()

# Podemos definir un valor por defecto en las funciones por ejemplo en el init ...asi


class Galleta():

    chocolate = False

    def __init__(self, sabor = None, color = None):
        # el valor despues del igual hace referencia a las de función (función init)
        # y las primeras a las de la clase (son distintas)
        self.sabor = sabor
        self.color = color
        print("Se acaba de crear una galleta {} y {}".format(sabor,color))

    def chocolatear(self):
        self.chocolate = True

    def tiene_chocolate(self):
        if (self.chocolate):
            print("Soy una galleta chocolateada =D ")
        else:
            print("Soy una galleta sin chocolate =( ")

# Si ejecutamos una galleta vacia
#otra_galleta = Galleta()
# Nos dira: Se acaba de crear una galleta None y None

# Podemos modificar el mensaje haciendo que unicamente se muestre el mensaje si el sabor y color tienen un valor
# diferente a None...asi... 

class Galleta2():

    chocolate = False

    def __init__(self, sabor = None, color = None):
        # el valor despues del igual hace referencia a las de función (función init)
        # y las primeras a las de la clase (son distintas)
        self.sabor = sabor
        self.color = color
        if (sabor is not None and color is not None):
            print("Se acaba de crear una galleta {} y {}".format(sabor,color))
        else:
            print("Se creo una galleta sin sabor ni color")

    def chocolatear(self):
        self.chocolate = True

    def tiene_chocolate(self):
        if (self.chocolate):
            print("Soy una galleta chocolateada =D ")
        else:
            print("Soy una galleta sin chocolate =( ")

# Si ejecutamos una galleta vacia
otra_galleta = Galleta2()