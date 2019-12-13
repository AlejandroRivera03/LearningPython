# Numeros
print('Operaciones en Python')

print( 'Suma: 7 + 2 = {0}'.format(7+2) )
print( 'Resta: 7 - 2 = {0}'.format(7-2) )
print( 'Multiplicacion: 7 * 2 = {0}'.format(7*2) )
print( 'Division: 7 / 2 = {0}'.format(7/2) )
print( 'Modulo: 7 % 2 = {0}'.format(7%2) )
print( 'Potencia: 7 ^ 2 = {0}'.format(7**2) )

# Multi-asignacion de variables

a = b = 25
print( a )
print( b )

# Cadenas de texto

print( 'Texto comillas simples' )
print( "Texto con comillas dobles" )
print( 'Texto comillas simples con "comillas dobles" al interior' )
print( "Texto comillas dobles con 'comillas simples' al interior" )
print( 'Texto con puras \'comillas\' simples usando \\')
print( "Texto con puras \"comillas\" dobles usando \\")
print( "Texto con\ttabulacion" )
print( "Texto con\nsalto de linea" )
print( r"C:\nombre\directorio texto crudo 'r'" )

c1 = 'cadena 1 '
c2 = 'cadena 2 '
print(c1 + c2 + 'cadena 3')
print( c1 + (" " * 10) + c2 ) # Multiplicacion de cadenas de texto

# Cadenas de texto como rebanadas (slicing)

palabra = 'Python'
print( 'palabra: {0}'.format( palabra ) )
print( 'palabra[0]: {0}'.format( palabra[0] ) )
print( 'palabra[3]: {0}'.format( palabra[3] ) )
print( 'palabra[-6]: {0}'.format( palabra[-6] ) )
print( 'palabra[-1]: {0}'.format( palabra[-1] ) )
print( 'palabra[0:2]: {0}'.format( palabra[0:2] ) )
print( 'palabra[2:]: {0}'.format( palabra[2:] ) )
print( 'palabra[:2]: {0}'.format( palabra[:2] ) )
print( 'palabra[:]: {0}'.format( palabra[:] ) )
print( 'palabra[:99]: {0}'.format( palabra[:99] ) )
print( 'palabra[99:]: {0}'.format( palabra[99:] ) )
print( '"N" + palabra[1:]: {}'.format( "N"+palabra[1:] ) )
print( 'Longitud de una cadena (len() method): {}'.format( len(palabra) ) )