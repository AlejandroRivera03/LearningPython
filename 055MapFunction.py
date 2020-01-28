numeros = [2, 5, 10, 23, 50, 33]
print( list( map( lambda num: num*2, numeros ) ) )

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]
print( list( map( lambda x,y: x*y, a, b ) ) )

c = [11, 12, 13, 14, 15]
print( list( map( lambda x,y,z: x*y*z, a, b, c ) ) )

class Persona:
    def __init__( self, nombre, edad ):
        self.nombre = nombre
        self.edad = edad
    def __str__( self ):
        return '{} de {} años'.format( self.nombre, self.edad )

personas = [
    Persona( 'Alejandro', 35 ),
    Persona( 'Martha', 16 ),
    Persona( 'Manuel', 78 ),
    Persona( 'Eduardo', 12 )
]

personas = map( lambda persona: Persona( persona.nombre, persona.edad+1 ), personas )

for persona in personas:
    print( persona )