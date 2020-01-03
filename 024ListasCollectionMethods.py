lista = [1,2,3,4,5]
print( 'lista = [1,2,3,4,5]' )
lista.append(6)
print( 'lista.append(6) => {}'.format( lista ) )
lista.clear()
print( 'lista.clear() => {}'.format( lista ) )

print( '\n' )

l1 = [2,4,6]
l2 = [8,10,12]
l1.extend( l2 )
print( 'l1 = [2,4,6]' )
print( 'l2 = [8,10,12]' )
print( 'l1.extend( l2 ) => {}'.format( l1 ) )

print( '\n' )

print( '["Hola", "Mundo", "Mundo"].count( "Mundo" ) => {}'.format( ["Hola", "Mundo", "Mundo"].count( "Mundo" ) ) )
print( '["Hola", "Mundo", "Mundo"].index( "Mundo" ) => {}'.format( ["Hola", "Mundo", "Mundo"].index( "Mundo" ) ) )

print( '\n' )

cincos = [5, 10, 15, 25, 30, 35]
print( 'cincos = [5, 10, 15, 25, 30, 35]' )
cincos.insert( 3, 20 )
print( 'cincos.insert( 3, 20 ) => {}'.format( cincos ) )
cincos.pop()
print( 'cincos.pop() => {}'.format( cincos ) )
cincos.pop( 0 )
print( 'cincos.pop( 0 ) => {}'.format( cincos ) )
cincos.remove( 15 )
print( 'cincos.remove( 15 ) => {}'.format( cincos ) )
cincos.reverse()
print( 'cincos.reverse() => {}'.format( cincos ) )

print( '\n' )

lista = list( 'Hola mundo' )
print( 'lista = list( "Hola mundo" )' )
lista.reverse()
print( 'lista.reverse() => {}'.format( lista ) )
cadena = ''.join( lista )
print( 'cadena = "".join( lista ) => {}'.format( cadena ) )

print( '\n' )

lista = [ 5, -10, -100, 35, 0, -65 ]
print( 'lista = [ 5, -10, -100, 35, 0, -65 ]' )
lista.sort()
print( 'lista.sort() => {}'.format( lista ) )
lista.sort(reverse=True)
print( 'lista.sort(reverse=True) => {}'.format( lista ) )