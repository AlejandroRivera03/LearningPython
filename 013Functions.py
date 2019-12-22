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