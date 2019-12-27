class A:
    def __init__( self ):
        print( 'Soy de clase A' )
    def a( self ):
        print( 'Este metodo lo heredo de A' )

class B:
    def __init__( self ):
        print( 'Soy de clase B' )
    def a( self ):
        print( 'Este metodo lo heredo de B' )
    def b( self ):
        print( 'Este metodo lo heredo de B' )

class C( B, A ): # Herencia multiple
    def c( self ):
        print( 'Este metodo es de C' )

c = C()
c.a() # Clase A y B tienen este metodo, imprime el metodo de B por ser heredado antes que A
c.b()
c.c()