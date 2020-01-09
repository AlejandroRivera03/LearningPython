import random

print( 'random.random() => {}'.format( random.random() ) ) # >= 0 y < 1
print( 'random.uniform(1,10) => {}'.format( random.uniform(1,10) ) ) # >= 1 y < 10 flotantes
print( 'random.randrange(10) => {}'.format( random.randrange(10) ) ) # >= 0 y < 10 enteros
print( 'random.randrange(0,101) => {}'.format( random.randrange(0,101) ) ) # >= 0 y < 101
print( 'random.randrange(0,101,2) => {}'.format( random.randrange(0,101,2) ) ) # >= 0 y < 101 en multiplos de 2

print( '\n' )
c = 'Hola mundo'
print( 'c => {}'.format( c ) )
print( 'random.choice( c ) => {}'.format( random.choice( c ) ) )

l = [1,2,3,4,5,6,7,8,9]
print( 'l => {}'.format( l ) )
print( 'random.choice( l ) => {}'.format( random.choice( l ) ) )
random.shuffle( l )
print( 'random.shuffle( l ) => ', l )
print( 'random.sample( l, 2 ) => {}'.format( random.sample( l, 2 ) ) )