'''Modulo con funciones y clases a exportar en 028Modules.py y 057DocString.py'''

def saludar():
    '''Funcion que imprime una cadena de texto saludando'''
    print('Saludando desde la funcion saludar de modulo.py')

class Saludo():
    '''Docstring de la clase saludo'''
    def __init__( self ):
        '''DocString del metodo constructor de la clase Saludo'''
        print( 'Saludando desde el init de la clase Saludo de modulo.py' )