c = set()
print( 'c = set()' )
c.add( 1 )
print( 'c.add( 1 ) => {}'.format( c ) )
c.add( 2 )
print( 'c.add( 2 ) => {}'.format( c ) )
c.add( 3 )
print( 'c.add( 3 ) => {}'.format( c ) )
c.discard( 1 )
print( 'c.discard() => {}'.format( c ) )
c.add( 1 )
print( 'c.add( 1 ) => {}'.format( c ) )
c2 = c.copy()
print( 'c2 = c.copy() | c2 => {}'.format( c2 ) )
c2.add( 4 )
print( 'c2.add( 4 ) => {} | c => {}'.format( c2, c ) )
c2.clear()
print( 'c2.clear() => {}'.format( c2 ) )

print( '\n' )

c1 = {1, 2, 3}
c2 = {3, 4, 5}
c3 = {-1, 99}
c4 = {1, 2, 3, 4, 5}
print( 'c1 = {1, 2, 3}' )
print( 'c2 = {3, 4, 5}' )
print( 'c3 = {-1, 99}' )
print( 'c4 = {1, 2, 3, 4, 5}' )
print( 'c1.isdisjoint( c2 ) => {}'.format( c1.isdisjoint( c2 ) ) ) # isdisjoint() nada en comun
print( 'c1.isdisjoint( c3 ) => {}'.format( c1.isdisjoint( c3 ) ) )
print( 'c1.issubset( c4 ) => {}'.format( c1.issubset( c4 ) ) ) # issubset() es subconjunto de ?
print( 'c2.issubset( c4 ) => {}'.format( c2.issubset( c4 ) ) )
print( 'c3.issubset( c4 ) => {}'.format( c3.issubset( c4 ) ) )
print( 'c4.issuperset( c1 ) => {}'.format( c4.issuperset( c1 ) ) )
print( 'c4.issuperset( c2 ) => {}'.format( c4.issuperset( c2 ) ) )
print( 'c4.issuperset( c3 ) => {}'.format( c4.issuperset( c3 ) ) )
print( 'c1.union( c2 ) => {}'.format( c1.union( c2 ) ) )
print( 'c1.difference( c2 ) => {}'.format( c1.difference( c2 ) ) )
print( 'c1.intersection( c2 ) => {}'.format( c1.intersection( c2 ) ) )
print( 'c1.symmetric_difference( c2 ) => {}'.format( c1.symmetric_difference( c2 ) ) )

print( 'conjunto.update( conjunto2 ) => hace union de los conjuntos y guarda el resultado en conjunto' )
print( 'conjunto.difference_update( conjunto2 ) => Hace la diferencia entre ambos conjuntos y guarda el resultado en conjunto' )
print( 'conjunto.intersection_update( conjunto2 ) => hace la interseccion entre ambos conjuntos y guarda el resultado en conjunto' )
print( 'conjunto.intersection_update( conjunto2 ) => hace la interseccion entre ambos conjuntos y guarda el resultado en conjunto' )