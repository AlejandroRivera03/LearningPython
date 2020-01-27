def pares( n ):
    for numero in range( n+1 ):
        if numero % 2 == 0:
            yield numero

print( pares( 10 ) )

for num in pares( 10 ):
    print( num )

print( [ num for num in pares(20) ] )

lista = [1,2,3,4]
list_iterable = iter( lista ) # iter() method, to make a list, str, etc iterable
print( 'next() method' )
print( next( list_iterable ) )
print( next( list_iterable ) )
print( next( list_iterable ) )
print( next( list_iterable ) )
# print( next( list_iterable ) ) returns and error (StopIteration), the list has finished