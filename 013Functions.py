# defining a function
def tabla_de_multiplicar(num):
    print( 'Tabla del {0}'.format( num ) )
    for i in range(1,11):
        print( '{0} x {1} = {2}'.format( num, i, (num*i) ) )

tabla_de_multiplicar( 2 )


# returning value
def five_times( num ):
    return num*5

print( five_times( 34 ) )


# parameters and arguments
def resta(a=None, b=None): # Here are parameters
    if a == None or b == None:
        print( 'Debes enviar dos numeros como argumentos' )
        return
    return a - b

print( resta(5, 2) ) # Here are arguments
print( resta(b=2, a=5) )
print( resta() )

# value and reference
# colecciones, listas, diccionarios, conjuntos are normally passed by reference
# more simple data is passed by value

def doblar( num ):
    return num*2

num = 5
doblar( num ) # passed by value (create a copy)
print( num )

num = doblar( num ) # simulating by reference
print( num )


def doblarr( data ):
    for i,n in enumerate(data):
        data[i] *= 2

data = [1,2,3,4,5]
doblarr( data ) # passed by reference
print( data )

doblar( data[:] ) # sending a copy tu simulate passed by value
print( data )

def indeterminados_posicion(*args):
    print( args ) # a tupla
    for arg in args:
        print( arg )
indeterminados_posicion( 5, 'Hola', [1,2,3,4,5] )

def indeterminados_nombre(**kwargs):
    print(kwargs)
    for kwarg in kwargs:
        print( kwarg, ' ', kwargs[kwarg] )
indeterminados_nombre( n=5, c='Hola', l=[1,2,3,4,5] )

def super_funcion(*args, **kwargs):
    t = 0
    for arg in args:
        t += arg
    print( 'Sumatoria es', t )
    for kwarg in kwargs:
        print( kwarg, ' ', kwargs[kwarg] )

super_funcion( 5,10,15,20,15,nombre='alejandro',edad=20 )

# Recursividad

def cuenta_atras(num):
    print( num )
    num -= 1
    if num > 0:
        cuenta_atras(num)
    else:
        print( 'Booooom!' )
    print( 'fin de la funcion', num )

cuenta_atras( 5 )

def factorial( num ):
    print( 'valor inicial ->', num )
    if num > 1:
        num = num * factorial( num-1 )
    print( 'valor final ->', num )
    return num

factorial(5)

# Integrated functions

print( int( '50' ) )
print( float( '3.1416' ) )
print( 'concatenando numeros ' + str(3.1415) + ' ' + str(55) )
print( 'decimal: {0}, binario: {1}, hex: {2}'.format( 10, bin(10), hex(10) ) )
print( 'binario (1010) a decimal {0}, hex (a) a decimal {1}'.format( int('0b1010', 2), int('0xa', 16) ) )
print( 'abs(-10): {}, abs(10): {}'.format( abs(-10), abs(10) ) )
print( 'round(5.5): {}, round(5.4): {}'.format( round(5.5), round(5.4) ) )
print( 'eval("5+7"): {}'.format( eval("5+7") ) )
print( 'len("una cadena"): {}'.format( len("una cadena") ) )
help()