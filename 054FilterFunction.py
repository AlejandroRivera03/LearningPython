numeros = [2, 5, 10, 23, 50, 33]

print( list( filter( lambda num: num % 5 == 0, numeros ) ) )

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

menores = filter( lambda persona: persona.edad < 18, personas )
for menor in menores:
    print( menor )