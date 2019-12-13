# we can save different type of values
datos = [4, 'una cadena', -15, 3.14, 'otra cadena']
print( datos[0] ) # we can use slicing
print( datos[-1] )
print( datos[-2:] )


numeros = [1, 2, 3, 4]
print( numeros + [5, 6, 7, 8] )


pares = [0, 2, 4, 5, 8, 10]
print( pares )
pares[3] = 6
print( pares )
pares.append(12) # method to add values at the end
pares.append(7*2)
print( pares )

letras = ['a', 'b', 'c', 'd', 'e', 'f']
print( letras )
print( letras[:3] )
letras[:3] = ['A', 'B', 'C']
print( letras )
letras[:3] = []
print( letras )

a = ['a', 'b', 'c']
b = ['d', 'e', 'f']
c = ['g', 'h', 'i']
r = [a, b, c]
print( r )
print( r[1][2] )