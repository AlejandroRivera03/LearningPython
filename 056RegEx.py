import re

# search method => check in the whole string
texto = 'En esta cadena se encuentra una palabra mágica'
palabra = 'mágica'

encontrada = re.search( palabra, texto )

if encontrada is not None:
    print( 'Se ha encontrado la palabra' )
    print( 'encontrada.start() => {}'.format( encontrada.start() ) )
    print( 'encontrada.end() => {}'.format( encontrada.end() ) )
    print( 'encontrada.span() => {}'.format( encontrada.span() ) )
    print( 'encontrada.string => {}'.format( encontrada.string ) )
else:
    print( 'No se ha encontrado la palabra' )

# match method => check if the string starts with
texto = 'Hola Mundo'
match = re.match( 'Hola', texto )
if match is not None:
    print( 'La palabra inicia' )
else:
    print( 'La palabra no inicia' )

# split method => Divide a string in an indicates char
texto = 'Vamos a dividir esta cadena'
print( re.split( ' ', texto ) )

# sub method => substitute a string in a string
texto = 'Hola amigo'
print( re.sub( 'amigo', 'amiga', texto ) )

# findall method => get all the matches in a string
texto = 'hola adios hello bye hi hola'
print( re.findall( '(hola|hello|hi)', texto ) )

# Meta chars
def buscar( patrones, texto ):
    for patron in patrones:
        print( '{} => {}'.format( patron, re.findall( patron, texto ) ) )

texto = 'hla hola hoola hooola hoooola'

print( '\nMeta-char *: 0 or more times' )
patrones = [ 'hla', 'ho*', 'ho*la', 'hu*la' ]
buscar( patrones, texto )

print( '\nMeta-char +: 1 or more times' )
patrones = [ 'ho+', 'ho+la' ]
buscar( patrones, texto )

print( '\nMeta-char ?: 0 or 1 times' )
patrones = [ 'ho?', 'ho?la' ]
buscar( patrones, texto )

print( '\nMeta-char { }: {n} times, {n,m} range of times' )
patrones = [ 'ho{0}la', 'ho{2}la', 'ho{2,4}la' ]
buscar( patrones, texto )

print( '\nMeta-char [ ]: chars set' )
texto = 'haaaala heeeeela hiiiiila hola hula'
patrones = [ 'h[ou]la', 'h[aei]*la', 'h[aei]{2,5}la', 'h[^u]la' ]
buscar( patrones, texto )

print( '\nMeta-char [ - ]: range' )
texto = 'hola h0la Hola mola m0la, M0la'
patrones = [ 'h[a-z]la', 'h[0-9]la', '[A-z]{4}', '[A-Z][A-z0-9]{3}' ]
buscar( patrones, texto )

print( '\nMeta-char \: ' )
texto = 'Este curos de Python 3 se publico en el año 2016'
patrones = [ r'\d', r'\d+', r'\D', r'\D+', r'\s', r'\S', r'\S+', r'\w+', r'\W' ]
buscar( patrones, texto )

# \d => numerico
# \D => no numerico
# \s => espacio en blanco
# \S => no espacio en blanco
# \w => alfanumerico
# \W => no alfanumerico