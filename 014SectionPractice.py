def area_rectangulo(base, altura):
    return base*altura
print( area_rectangulo( 15,10 ) )


def area_circulo( radio ):
    return (radio**2) * 3.14159
print( area_circulo( 5 ) )


def relacion(first, second):
    if first > second:
        return 1
    elif first < second:
        return -1
    else:
        return 0
print( relacion( 5,10 ) )
print( relacion( 10,5 ) )
print( relacion( 5,5 ) )


def intermedio(a, b):
    return ( ( a + b ) / 2 )
print( intermedio(-12,24) )


def recortar(cut, min, max):
    if cut < min:
        return min
    elif cut > max:
        return max
    else:
        return cut
print( recortar(15, 0, 10) )


def separar(lista):
    lista.sort()
    pares = []
    impares = []
    for i in lista:
        if i % 2 == 0:
            pares.append(i)
        else:
            impares.append(i)
    return pares, impares
pares, impares = separar( [-12, 84, 13, 20, -33, 101, 9] )
print( pares )
print( impares )