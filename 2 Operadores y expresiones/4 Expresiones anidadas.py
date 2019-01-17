a = 10
b = 5
res= a * b - 2**b >= 20 and not (a % b) != 0
print(res)

# En el anterior ejemplo da como resultado "False".
# Existen normas de precedencia y tiene el siguiente orden.
# 1. Primero los paréntesis porque tienen prioridad.
# Solución: a * b - 2**b >= 20 and not 0 != 0
# 2. Expresiones aritméticas por sus propias reglas... o sea
  # a. Exponente y raiz. (** - sqrt)
  # Solución: a * b - 32 >= 20 and not 0 != 0
  # b. Multiplicaciones y divisiones. (* - /)
  # Solución: 50 - 32 >= 20 and not 0 != 0
  # c. Sumas y restas (siempre de izquierda a derecha)(+-)
  # Solución: 18 >= 20 and not 0 != 0
# 3. Relacionales de izquierda a derecha (and not or)(Importante notar que el not tiene prioridad
# porque afecta directamente al operando)
# Solución: 18 >= 20 and not false
# 4. Lógicos (False - True)
# Solución: false and not false
# Solución: false and true
# Solución: false