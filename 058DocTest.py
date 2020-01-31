def suma( a, b ):
    '''
        La funcion suma(a,b) recibe dos parametros
        Devuelve la suma de ambos
        (run in terminal: python 058DocTest.py -v to check testing)

        Pueden ser numeros:

        >>> suma(5,10)
        15
        >>> suma(-5,7)
        2
        >>> suma(0,0)
        0

        Cadenas de texto:

        >>> suma('aa', 'bb')
        'aabb'

        O listas:

        >>> a = [1, 2, 3]
        >>> b = [4, 5, 6]
        >>> suma(a, b)
        [1, 2, 3, 4, 5, 6]

        >>> suma(10,'hola')
        Traceback (most recent call last):
          ...
        TypeError: unsupported operand type(s) for +: 'int' and 'str'
    '''
    return a+b

# if ___name__ == '__main__':
import doctest
doctest.testmod()