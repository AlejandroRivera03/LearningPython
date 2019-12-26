class Galleta():
    chocolate = False

    def __init__( self, sabor=None, forma=None):
        self.sabor = sabor
        self.forma = forma
        if sabor is not None and forma is not None:
            print( 'Se acaba de crear una galleta {} y {}'.format( sabor, forma ) )
    
    def chocolatear( self ):
        self.chocolate = True
    
    def tiene_chocolate( self ):
        if self.chocolate:
            print( 'Soy una galleta chocolateada' )
        else:
            print( 'Soy una galleta sin chocolate' )
    
    # special methods
    def __del__( self ):
        print( 'Se ha borrado la galleta' )

    def __str__( self ):
        return 'galleta sabor {} con forma {}'.format( self.sabor, self.forma )
    
    def __len__( self ):
        return len( self.sabor )

g = Galleta('dulce', 'redonda')
g.tiene_chocolate()
g.chocolatear()
g.tiene_chocolate()
print( str(g) )
print( len(g) )
del(g)
