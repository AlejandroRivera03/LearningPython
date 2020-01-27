# Function inside function

def hola():

    def bienvenido():
        return 'Holaaa!!'
    
    return bienvenido

print( 'Function inside function' )
print( hola )
print( hola() )
print( hola()() )
print( '\n' )

# Passing a funcion by parameter to another function

def hello():
    return 'Hello!'

def test( funcion ):
    print( funcion() )

print( 'Passing a funcion by parameter to another function' )
test( hello )
print( '\n' )

# Passing a funcion by parameter to another function (other way)

def hi():
    print( 'Hi!' )
def bye():
    print( 'Bye!' )

def monitorizar( funcion ):
    def decorar():
        print( 'Se esta apunto de ejecutar la funcion:', funcion.__name__ )
        funcion()
        print( 'Se ha finalizado la ejecucion de la funcion:', funcion.__name__ )
    return decorar

print( 'Passing a funcion by parameter to another function (other way)' )
print( monitorizar(hi)() )
print( monitorizar(bye)() )
print( '\n' )

# Decorators

@monitorizar
def que_onda():
    print( 'Que onda!' )

@monitorizar
def nos_vemos():
    print( 'Nos vemos!' )

print( 'Decorators' )
print( que_onda() )
print( nos_vemos() )
print( '\n' )

# Decorators and arguments

def monitorizar_args( funcion ):
    def decorar(*args, **kwargs):
        print( 'Se esta apunto de ejecutar la funcion:', funcion.__name__ )
        funcion(*args, **kwargs)
        print( 'Se ha finalizado la ejecucion de la funcion:', funcion.__name__ )
    return decorar

@monitorizar_args
def hi_with_name( name ):
    print( 'Hola {}!'.format( name ) )
@monitorizar_args
def bye_with_name( name ):
    print( 'Adios {}!'.format( name ) )

print( 'Decorators and arguments' )
print( hi_with_name( 'Alejandro' ) )
print( bye_with_name( 'Alejandro' ) )