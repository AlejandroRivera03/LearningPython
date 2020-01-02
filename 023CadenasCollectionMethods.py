print( '"Hola Mundo".upper() => {}'.format( 'Hola Mundo'.upper() ) )
print( '"Hola Mundo".lower() => {}'.format( 'Hola Mundo'.lower() ) )
print( '"hola mundo".capitalize() => {}'.format( 'hola mundo'.capitalize() ) )
print( '"hola mundo".title() => {}'.format( 'hola mundo'.title() ) )
print( '"Hola Mundo".count("Mundo") => {}'.format( 'Hola Mundo'.count('Mundo') ) )
print( '"Hola Mundo".find("Mundo") => {} (Return the index)'.format( 'Hola Mundo'.find("Mundo") ) )
print( '"Hola Mundo Mundo Mundo".rfind("Mundo") => {} (Return the index)'.format( 'Hola Mundo Mundo Mundo'.rfind("Mundo") ) )

print( '\n' )

print( '"100".isdigit() => {}'.format( "100".isdigit() ) )
print( '"texto".isdigit() => {}'.format( "texto".isdigit() ) )
print( '"ABC123".isalnum() => {}'.format( "ABC123".isalnum() ) ) # alfanumerico
print( '"!·$%&".isalnum() => {}'.format( "!·$%&".isalnum() ) )
print( '"hola mundo".isalpha() => {}'.format( "hola mundo".isalpha() ) ) # alfanumerico
print( '"holamundo".isalpha() => {}'.format( "holamundo".isalpha() ) )

print( '\n' )

print( '"Hola mundo".islower() => {}'.format( "Hola mundo".islower() ) )
print( '"hola mundo".islower() => {}'.format( "hola mundo".islower() ) )
print( '"Hola mundo".isupper() => {}'.format( "Hola mundo".isupper() ) )
print( '"HOLA MUNDO".isupper() => {}'.format( "HOLA MUNDO".isupper() ) )
print( '"Hola Mundo".istitle() => {}'.format( "Hola Mundo".istitle() ) )
print( '"Hola mundo".istitle() => {}'.format( "Hola mundo".istitle() ) )
print( '"   ".isspace() => {}'.format( "   ".isspace() ) )
print( '"  -  ".isspace() => {}'.format( "  -  ".isspace() ) )
print( '"Hola Mundo".startswith("Hola") => {}'.format( "Hola Mundo".startswith("Hola") ) )
print( '"Hola Mundo".startswith("H") => {}'.format( "Hola Mundo".startswith("H") ) )
print( '"Hola Mundo".startswith("p") => {}'.format( "Hola Mundo".startswith("p") ) )
print( '"Hola Mundo".endswith("Mundo") => {}'.format( "Hola Mundo".endswith("Mundo") ) )
print( '"Hola Mundo".endswith("o") => {}'.format( "Hola Mundo".endswith("o") ) )
print( '"Hola Mundo".endswith("z") => {}'.format( "Hola Mundo".endswith("z") ) )

print( '\n' )

print( '"Hola-Mundo-Otra-Palabra".split("-") => {}'.format( "Hola-Mundo-Otra-Palabra".split("-") ) )
print( '" ".join("Hola Mundo") => {}'.format( " ".join("Hola Mundo") ) )
print( '"   Hola   ".strip() => "{}"'.format( "   Hola   ".strip() ) )
print( '"---Hola---".strip("-") => "{}"'.format( "---Hola---".strip("-") ) )
print( '"Hola Mundo".replace("o", "0") => {}'.format( "Hola Mundo".replace("o", "0") ) )
print( '"Hola Mundo".replace("Mundo", "Marte") => {}'.format( "Hola Mundo".replace("Mundo", "Marte") ) )
print( '"Hola Mundo Mundo Mundo Mundo Mundo".replace(" Mundo","",4) => {}'.format( "Hola Mundo Mundo Mundo Mundo Mundo".replace(" Mundo","",4) ) )