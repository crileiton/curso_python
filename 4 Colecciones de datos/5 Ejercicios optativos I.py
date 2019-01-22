# Solución ejercicio No. 1
"""usuarios = {'Marta','David','Elvira','Juan','Marcos'}
administradores = {'Juan','Marta'}

administradores.discard('Juan')
administradores.add('Marcos')

for usuario in usuarios:
    if usuario in administradores:
        print(usuario," Es administrador")
    else:
        print(usuario,' No es administrador')


# Solución ejercicio No. 2
caballero = { 'vida':2, 'ataque':2, 'defensa':2, 'alcance':2 }
guerrero = { 'vida':2, 'ataque':2, 'defensa':2, 'alcance':2 }
arquero = { 'vida':2, 'ataque':2, 'defensa':2, 'alcance':2 }

caballero['vida'] = guerrero['vida'] * 2
caballero['defensa'] = guerrero['defensa'] * 2

guerrero['ataque'] = caballero['ataque'] * 2
guerrero['alcance'] = caballero['alcance'] * 2

arquero['vida'] = guerrero['ataque']
arquero['ataque'] = guerrero['alcance']

arquero['defensa'] = guerrero['defensa'] / 2
arquero['alcance'] = guerrero['alcance'] * 2

print('Caballero: \t',caballero)
print('Guerrero: \t',guerrero)
print('Arquero: \t',arquero)

"""
# Solución ejercicio No. 3
tareas = [
    [6, 'Distribución'],
    [2, 'Diseño'],
    [1, 'Concepción'],
    [7, 'Mantenimiento'],
    [4, 'Producción'],
    [3, 'Planificación'],
    [5, 'Pruebas'],
]

print('== Tareas desordenadas ==')
for tarea in tareas:
    print(tarea[0],tarea[1])

from collections import deque
tareas.sort()
print(tareas)

cola = deque()

for tarea in tareas:
    cola.append(tarea[1])


print('== Tareas ordenadas ==')
for tarea in tareas:
    print(tarea[0],tarea[1])














