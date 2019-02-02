# En python podemos acceder a los atributos y metodos de un objeto muy facilmente, esto es porque se consideran 
# de acceso publico aunque en algunas ocaciones nos interesa que estos no se puedan ejecutar desde fuera o sea queremos
# que sean privados

# La encapsulación es una funcionalidad que tienen muchos lenguajes para impedir el acceso externo a los atributos
# y metodos, pero python NO ofrece esta funcionalidad aun asi se puede simular un comportamiento parecido precediendo
# los nombres de estos atributos y metodos con dos barras bajas (__)

class Ejemplo:
    # Atributo privado
    __atributo_privado = "Soy un atributo inalcanzable desde fuera"

    # Metodo privado
    def __metodoPrivado(self):
        print("Soy un metodo inalcanzable desde fuera")

# Desde fuera no podemos llamar ni los metodos ni atributos privados
#e = Ejemplo()
#e.__metodoPrivado()

# Es posible crear unos metodos que hagan de puente entre el exterior y el interior y los podemos llamar
# publicos

# Para poder acceder al atributo publico...retomamos ejemplo...

class Ejemplo2:
    # Atributo privado
    __atributo_privado = "Soy un atributo inalcanzable desde fuera"

    # Metodo privado
    def __metodoPrivado(self):
        print("Soy un metodo inalcanzable desde fuera")
    
    def atributoPublico(self):
        return self.__atributo_privado
    
    def metodoPublico(self):
        return self.metodoPublico()

# Asi podemos acceder 
e = Ejemplo2()
print(e.metodoPublico)