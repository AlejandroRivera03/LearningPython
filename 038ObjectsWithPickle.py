from io import open
import pickle

lista = [1, 2, 3, 4, 5]
fichero = open( 'lista.pckl', 'wb' ) # wb => write binary
pickle.dump( lista, fichero ) # methos to create and write
fichero.close()

fichero = open( 'lista.pckl', 'rb' )
l = pickle.load( fichero )
fichero.close()
print( l )

class Persona:
    def __init__( self, nombre ):
        self.nombre = nombre
    def __str__( self ):
        return self.nombre

nombres = ['Alejandro', 'Eduardo', 'Rigoberto']
personas = []

for n in nombres:
    p = Persona( n )
    personas.append( p )

fichero = open( 'personas.pckl', 'wb' )
pickle.dump( personas, fichero )
fichero.close()

fichero = open( 'personas.pckl', 'rb' )
people = pickle.load( fichero )
fichero.close()

for pe in people:
    print( pe )