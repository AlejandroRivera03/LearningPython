n1 = float( input( "Ingresa primer numero: " ) )
n2 = float( input( "Ingresa segundo numero: " ) )

print( '¿Son iguales?', n1 == n2 )
print( '¿Son diferentes?', n1 != n2 )
print( '¿Primero mayor que el segundo?', n1 > n2 )
print( '¿Segundo mayor o igual que el primero?', n2 >= n1 )

c = input( 'Ingrese un texto: ' )
print( '¿Logitud de cadena mayor a 3 y menor que 10?', len(c) >= 3 and len(c) < 10 )

numero_magico = 12345679
numero_usuario = int( input( "Ingresa un numero entre 1 y 9: " ) )
if numero_usuario >= 1 and numero_usuario <= 9:
    numero_usuario *= 9
    numero_magico *= numero_usuario
    print( numero_magico )
else:
    print( 'Numero no valido.' )

