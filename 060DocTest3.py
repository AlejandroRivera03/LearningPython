def palindromo( palabra ):
    '''
        La funcion palindromo(palabra) recibe una palabra.
        Si la palabra es un palindromo devuelve True, si no False

        Un palindromo es una palabra o frase que se le se le igual
        tanto de izquierda a derecha como de derecha a izquierda

        >>> palindromo('radar')
        True
        >>> palindromo('somos')
        True
        >>> palindromo('holah')
        False
        >>> palindromo('Ana')
        True
        >>> palindromo('Anita lava la tina')
        True
    '''
    if palabra.lower().replace(' ', '') == palabra[::-1].lower().replace(' ', ''):
        return True
    else:
        return False

import doctest
doctest.testmod()