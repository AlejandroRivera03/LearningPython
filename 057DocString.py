import module
import package

''' 
    use help() method and add a function, class, module, package, etc by parameter to check more information about it
'''

def saludar( nombre ):
    '''
        Funcion para saludar a un usuario
        nombre (str): Nombre del usuario
    '''
    print( 'Hola {}!'.format( nombre ) )
saludar( 'Eduardo' )
help( saludar )

class Clase:
    '''Este es el dicstring de la clase'''
    def __init__( self ):
        '''Este es el docstring del inicializador de clase (constructor)'''
        pass
    def metodo( self ):
        '''Este es el docstring del metodo de clase'''
        pass

o = Clase()
help( o )

help( module )

help( module.saludar )

print( dir( module ) )

print( module.__doc__ )

help( package )