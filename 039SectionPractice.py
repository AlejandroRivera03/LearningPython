from io import open

personas = []

with open( 'personas.txt', 'r', encoding='utf8' ) as fichero:
    for linea in fichero:
        split = linea.replace( "\n", "" ).split(';')
        person = {
            'id': split[0],
            'nombre': split[1],
            'apellido': split[2],
            'nacimiento': split[3]
        }
        personas.append( person )

for p in personas:
    print( '(id={}) {} {} => {}'.format( p['id'], p['nombre'], p['apellido'], p['nacimiento'] ) )