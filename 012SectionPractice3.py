import sys

if len(sys.argv) == 2:
    numero = int( sys.argv[1] )
    if numero < 0 or numero > 9999:
        print( 'Error - Numero incorrecto' )
        print( 'python 012SectionPractice3.py [0 - 9999]' )
    else:
        cadena = str( numero )
        longitud = len( cadena )

        for i in range( longitud ):
            print( '{0:04d}'.format( ( int( cadena[longitud-1-i] ) * 10**i ) ) )
else:
    print( 'Error - Argumentos incorrectos' )
    print( 'python 012SectionPractice3.py [0 - 9999]' )