from io import open
import pickle

class Pelicula:
    def __init__( self, titulo, duracion, lanzamiento ):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print( 'Se ha creado la pelicula:', self.titulo )
    def __str__( self ):
        return '{} ({})'.format( self.titulo, self.lanzamiento )

class Cartelera:
    peliculas = []
    def __init__( self, peliculas=[] ):
        self.cargar()

    def agregar( self, p ):
        self.peliculas.append( p )
        self.guardar()

    def mostrar( self ):
        if len( self.peliculas ) == 0:
            print( 'La cartelera esta vacia' )
            return
        for p in self.peliculas:
            print( p )
    
    def cargar( self ):
        fichero = open( 'cartelera.pckl', 'ab+' )
        fichero.seek(0)
        try:
            self.peliculas = pickle.load( fichero )
        except:
            print( 'El fichero esta vacio' )
        finally:
            fichero.close()
            print( 'Se han cargado {} peliculas'.format( len( self.peliculas ) ) )
    
    def guardar( self ):
        fichero = open( 'cartelera.pckl', 'wb' )
        pickle.dump( self.peliculas, fichero )
        fichero.close()

    def __del__( self ):
        self.guardar()
        print( 'Programa finalizado y datos guardados' )

c = Cartelera()
c.mostrar()
# c.agregar( Pelicula( 'El infierno', 100, 2010 ) )
# c.agregar( Pelicula( 'Jumanji 2', 120, 2019 ) )
# c.agregar( Pelicula( 'Rapido y furioso: reto tokio', 125, 2006 ) )
# c.agregar( Pelicula( 'Titanic', 160, 1996 ) )
del( c )
# c.mostrar()