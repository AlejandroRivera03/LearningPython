try:
    resultado = 10 / 0
except ZeroDivisionError:
    print( 'Error: Estas dividiendo entre 0' )


lista = [1,2,3,4,5]
try:
    print( lista[10] )
except IndexError:
    print( 'Error: El indice esta fuera del rango' )


colores = { 'rojo':'red', 'verde':'green', 'negro':'black' }
try:
    print( colores['blanco'] )
except KeyError:
    print( 'Error: la key a la que tratas de acceder no se encuentra en el diccionario' )


try:
    resultado = 15 + '20'
except TypeError:
    print( 'Error: Solo es posible sumar/concatenar datos del mismo tipo, transforma el int a string o el string a int' )



def agregar_una_vez( lista, num ):
    try:
        if num not in lista:
            lista.append( num )
        else:
            raise ValueError('Elemento ya en lista')
    except ValueError:
        print( 'Error: Imposible añadir elementos duplicados => {}'.format( num ) )

elementos = [1, 5, -2]
agregar_una_vez( elementos, 10 )
agregar_una_vez( elementos, -2 )
agregar_una_vez( elementos, "Hola" )
print( elementos )