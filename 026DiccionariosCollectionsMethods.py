colores = { "rojo":"red", "verde":"green", "azul":"blue" }
print( 'colores = { "rojo":"red", "verde":"green", "azul":"blue" }' )
print( 'colores["rojo"] => {}'.format( colores["rojo"] ) )
print( 'colores.get("verde") => {}'.format( colores.get("verde") ) )
print( 'colores.get("negro", "no se encuentra") => {}'.format( colores.get("negro", "no se encuentra") ) )
print( '"azul" in colores => {}'.format( 'azul' in colores ) )
print( '"rosa" in colores => {}'.format( 'rosa' in colores ) )
print( 'colores.keys() => {}'.format( colores.keys() ) )
print( 'colores.values() => {}'.format( colores.values() ) )
print( 'colores.items() => {}'.format( colores.items() ) )

colores.pop( "rojo" )
print( 'colores.pop( "rojo" ) => {}'.format( colores ) )
print( 'colores.pop( "rojo", "No se ha encontrado" ) => {}'.format( colores.pop( "rojo", "No se ha encontrado" ) ) )
colores.clear()
print( 'colores.clear() => {}'.format( colores ) )