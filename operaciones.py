def suma( n1, n2 ):
    try:
        return n1 + n2
    except TypeError:
        return 'No se puede dividir un numero entre una cadena'

def resta( n1, n2 ):
    try:
        return n1 - n2
    except TypeError:
        return 'Error: Tipo de dato no valido'

def multiplicacion( n1, n2 ):
    try:
        return n1 * n2
    except TypeError:
        return 'Error: Tipo de dato no valido'

def division( n1, n2 ):
    try:
        return n1 / n2
    except TypeError:
        return 'Error: Tipo de dato no valido'
    except ZeroDivisionError:
        return 'Error: No es posible dividir entre 0'