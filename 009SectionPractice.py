from collections import deque

usuarios = {'Martha', 'David', 'Elvira', 'Juan', 'Marcos'}
administradores = {'Juan', 'Martha'}

administradores.discard('Juan')

administradores.add('Marcos')

for usuario in usuarios:
    if usuario in administradores:
        print( usuario, 'administrador' )
    else:
        print( usuario, 'normal')


caballero   = { 'vida':2, 'ataque':2, 'defensa':2, 'alcance':2 }
guerrero    = { 'vida':2, 'ataque':2, 'defensa':2, 'alcance':2 }
arquero     = { 'vida':2, 'ataque':2, 'defensa':2, 'alcance':2 }

caballero['vida'] = ( guerrero['vida']*2 )
caballero['defensa'] = ( guerrero['defensa']*2 )

guerrero['ataque'] = ( caballero['ataque']*2 )
guerrero['alcance'] = ( caballero['alcance']*2 )

arquero['vida'] = ( guerrero['vida'] )
arquero['ataque'] = ( guerrero['ataque'] )
arquero['defensa'] = ( guerrero['defensa']/2 )
arquero['alcance'] = ( guerrero['alcance']*2 )

print( 'caballero:\t', caballero )
print( 'guerrero:\t', guerrero )
print( 'arquero:\t', arquero )



tareas = [
    [6, 'Distribucion'],
    [2, 'Diseño'],
    [1, 'Concepcion'],
    [7, 'Mantenimiento'],
    [4, 'Produccion'],
    [3, 'Planificacion'],
    [5, 'Pruebas']
]

print( '==Tareas desordenadas==' )
for tarea in tareas:
    print( tarea[0], tarea[1] )

tareas.sort()

cola = deque()

for tarea in tareas:
    cola.append( tarea[1] )

print( '\n==Tareas ordenadas==' )
for tarea in cola:
    print( tarea )