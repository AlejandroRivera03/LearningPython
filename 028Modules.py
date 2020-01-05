# Paths donde python busca los modulos
import sys
print( sys.path )
# sys.path.insert( 1, 'path' ) Insertando un path de un modulo

# Importando un modulo y tratandolo como objeto
import module
module.saludar() # funcion
module.Saludo() # clase


from module import * # Importando todas las funciones y clases
from module import saludar # Importando una funcion en especifico
saludar()


from module import Saludo # Importando una clase en especifico
Saludo()