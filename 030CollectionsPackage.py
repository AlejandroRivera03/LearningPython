from collections import Counter
from collections import defaultdict
from collections import OrderedDict
from collections import namedtuple

l = [1,2,3,4,1,2,3,1,2,1]
print( Counter( l ) )

p = 'palabra'
print( Counter( p ) )

animales = 'gato perro canario perro canario perro'
c = Counter( animales.split() )
print( c )
print( c.most_common() )
print( c.most_common(1) )
print( c.most_common(2) )

l = [10,20,30,40,10,20,30,10,20,10]
c = Counter( l )
print( c.items() )
print( c.keys() )
print( c.values() )
print( list( c ) ) # Lista
print( dict( c ) ) # Diccionario
print( set( c ) ) # Conjunto

print( '\n' )

d = defaultdict( float )
print( d['key'] )
print( d )
d = defaultdict( str )
print( d['key'] )
print( d )
d = defaultdict( int )
print( d['key'] )
print( d )
d = defaultdict( object )
print( d['key'] )
print( d )

print( '\n' )

n = {}
n['uno'] = 'one'
n['dos'] = 'two'
n['tres'] = 'three'
print( n )

n = OrderedDict()
n['uno'] = 'one'
n['dos'] = 'two'
n['tres'] = 'three'
print( n )

n1 = {}
n1['uno'] = 'one'
n1['dos'] = 'two'
n2 = {}
n2['dos'] = 'two'
n2['uno'] = 'one'
print( 'n1 == n2 => {}'.format( n1 == n2 ) )

n1 = OrderedDict()
n1['uno'] = 'one'
n1['dos'] = 'two'
n2 = OrderedDict()
n2['dos'] = 'two'
n2['uno'] = 'one'
print( 'n1 == n2 => {}'.format( n1 == n2 ) )

print( '\n' )

Persona = namedtuple( 'Persona', 'nombre apellido edad' )
p = Persona( nombre='Alejandro', apellido='Rivera', edad='25' )
print( 'p.nombre => {}, or p[0] => {}'.format( p.nombre, p[0] ) )
print( 'p.apellido => {}, or p[1] => {}'.format( p.apellido, p[1] ) )
print( 'p.edad => {}, or p[2] => {}'.format( p.edad, p[2] ) )
print( p )