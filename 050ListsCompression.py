# traditional
print( 'Traditional methods' )
lista = []
for letra in 'casa':
    lista.append( letra )
print( lista )

numbers = []
for number in range( 0, 11 ):
    numbers.append( number**2 )
print( numbers )

conditional = []
for numero in range( 0, 11):
    if numero % 2 == 0:
        conditional.append( numero )
print( conditional )

otherList = []
for numero in range(0,11):
    otherList.append( numero**2 )
pares = []
for numero in otherList:
    if numero % 2 == 0:
        pares.append( numero )
print( pares )

# list's compression method
print( 'Compression methods' )
listaC = [ letra for letra in 'casa' ]
print( listaC )

numbersC = [ number**2 for number in range( 0, 11 ) ]
print( numbersC )

conditionalC = [ numero for numero in range(0, 11) if numero % 2 == 0 ]
print( conditionalC )

paresC = [ numero for numero in [ numero**2 for numero in range(0, 11) ] if numero % 2 == 0 ]
print( paresC )