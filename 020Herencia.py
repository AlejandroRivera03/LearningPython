class Producto:
    def __init__( self, referencia, nombre, pvp, descripcion ):
        self.referencia = referencia
        self.nombre = nombre
        self.pvp = pvp
        self.descripcion = descripcion
    
    def __str__( self ):
        return '''\
REFERENCIA\t{}
NOMBRE\t\t{}
PVP\t\t{}
DESCRIPCION\t{}'''.format( self.referencia, self.nombre, self.pvp, self.descripcion )

class Adorno( Producto ):
    pass

class Alimento( Producto ):
    productor = ''
    distribuidor = ''

    def __str__( self ):
        return '''\
REFERENCIA\t{}
NOMBRE\t\t{}
PVP\t\t{}
DESCRIPCION\t{}
PRODUCTOR\t{}
DISTRIBUIDOR\t{}'''.format( self.referencia, self.nombre, self.pvp, self.descripcion, self.productor, self.distribuidor )

class Libro( Producto ):
    isbn = ''
    autor = ''

    def __str__( self ):
        return '''\
REFERENCIA\t{}
NOMBRE\t\t{}
PVP\t\t{}
DESCRIPCION\t{}
ISBN\t\t{}
AUTOR\t\t{}'''.format( self.referencia, self.nombre, self.pvp, self.descripcion, self.isbn, self.autor )

a = Adorno( 2034, 'Vaso adornado', 15, 'Vaso de porcelana adornado con arboles' )
# print( a )

al = Alimento( 2035, 'Botella de aceite de oliva extra', 5, '250 ML' )
al.productor = 'La aceiteria'
al.distribuidor = 'Distribuciones SA de CV'
# print( al )

li = Libro( 2036, 'Cocina mediterranea', 9, 'Recetas sanas y buenas' )
li.isbn = '0-123456-789-0'
li.autor = 'Maria Juana'
# print( li )

productos = [a, al]
productos.append( li )

for p in productos:
    if( isinstance( p, Adorno ) ):
        print( p.referencia, p.nombre )
    elif( isinstance( p, Alimento ) ):
        print( p.referencia, p.nombre, p.productor )
    elif( isinstance( p, Libro ) ):
        print( p.referencia, p.nombre, p.isbn )