while(True):
    try:
        n = float( input( 'Introduce un numero: ' ) )
        m = 4
        print( '{}/{}={}'.format( n, m, m/n ) )
    except TypeError:
        print( 'No se puede dividir un numero entre una cadena' )
    except ValueError:
        print( 'No se puede dividir un numero entre una cadena x2' )
    except ZeroDivisionError:
        print( 'No puedes dividir entre 0' )
    except Exception as e:
        print( type( e ).__name__ )
    else:
        print( 'Todo ha funcionado correctamente' )
        break
    finally:
        print( 'Fin de la iteracion' )

def mi_funcion( algo = None ):
    try:
        if algo is None:
            raise ValueError( 'Error! No se permite un valor nulo' ) # invocando error
    except ValueError: # controlando error provocado
        print( 'Error! no se permite un valor nulo (exception)' )
mi_funcion()