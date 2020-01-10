from io import open

texto = 'Una linea con texto\nOtra linea con texto'

fichero = open( 'fichero.txt', 'w' )
fichero.write( texto )
fichero.close()

fichero = open( 'fichero.txt', 'r' )
text = fichero.read()
fichero.close()

fichero = open( 'fichero.txt', 'r' )
lines = fichero.readlines()
fichero.close()

print( text )
print( lines )

fichero = open( 'fichero.txt', 'a' )
fichero.write( '\nTercer linea del fichero' )
fichero.close()

fichero = open( 'fichero.txt', 'r' )
print( fichero.readline() )
print( fichero.readline() )
print( fichero.readline() )
print( fichero.readline() )
fichero.close()

print( 'Ciclo para leer lineas => ' )
with open( 'fichero.txt', 'r' ) as fichero:
    for linea in fichero:
        print( linea )

print( '\nPunteros =>' )

fichero = open( 'fichero.txt', 'r' )
fichero.seek(15) # puntero en la posicion 15
print( 'fichero.seek(15) => \n{}'.format( fichero.read() ) )
print( 'fichero.read() => \n{}'.format( fichero.read() ) )
fichero.seek(10) # puntero en la posicion 10
print( 'fichero.seek(10) => \n{}'.format( fichero.read() ) )
fichero.seek(0) # puntero en la posicion 0
print( 'fichero.read(5) => {}'.format( fichero.read(5) ) )
print( 'fichero.read() => {}'.format( fichero.read() ) )

print( '\n' )
print( '\n' )
fichero.seek(0)
texto = fichero.read()
fichero.seek( len( texto ) / 2 )
print( fichero.read() )

fichero.seek( 0 )
fichero.seek( len( fichero.readline() ) )
print( fichero.read() )

fichero = open( 'fichero.txt', 'r+' )
lineas = fichero.readlines()
lineas[1] = 'Segunda linea del ficherooooo\n'
fichero.seek(0)
fichero.writelines(lineas)
fichero.close()