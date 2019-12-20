c = 'otro texto'
n = 22
print( 'un texto, {0} y un numero {1}'.format( c, n ) )
print( 'with key {texto} y {numero}'.format( numero=n, texto=c ) )
print( '{0:<30} alignment with 30 chars'.format( 'left' ) )
print( '{0:^30} alignment with 30 chars'.format( 'center' ) )
print( '{0:>30} alignment with 30 chars'.format( 'right' ) )
print( '{0:.15}'.format( 'truncando palabra' ) )
print( '{0:>20.12} and truncamiento'.format( 'right aligment' ) )

print( '{:4d}'.format( 10 ) )
print( '{:4d}'.format( 100 ) )
print( '{:4d}'.format( 1000 ) )

print( '{:04d}'.format( 10 ) )
print( '{:04d}'.format( 100 ) )
print( '{:04d}'.format( 1000 ) )

print( '{:7.3f}'.format( 3.1415926 ) )
print( '{:7.3f}'.format( 153.21 ) )