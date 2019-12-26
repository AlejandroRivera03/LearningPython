class Pelicula:

    def __init__( self, titulo, duracion, lanzamiento ):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print( 'Se ha creado la pelicula:', self.titulo )
    
    def __str__( self ):
        return '{} ({})'.format( self.titulo, self.lanzamiento )
    
class Catalogo:
    peliculas = []

    def __init__( self, peliculas=[] ):
        self.peliculas = peliculas
    
    def agregar( self, p ):
        self.peliculas.append( p )
    
    def mostrar( self ):
        for p in self.peliculas:
            print( p )

p = Pelicula( 'El infierno', 120, 2009 )
c = Catalogo( [p] )
c.agregar( Pelicula( 'Avengers: Endgame', 185, 2019 ) )
c.mostrar()

# Encapsulamiento de metodos y atributos

class Ejemplo:
    __atributo_privado = 'Soy un atributo inalcanzable desde fuera'

    def __metodo_privado( self ):
        print( 'Soy un metodo inalcanzable desde fuera' )
    
    def atributo_publico( self ):
        return self.__atributo_privado

    def metodo_publico( self ):
        return self.__metodo_privado()

e = Ejemplo()
# e.__atributo_privado -> retorna error
# e.__metodo_privado -> retorna error

# accediendo al metodo y atributo privado desde metodos publicos que funcionan de puente
print( e.atributo_publico() )
e.metodo_publico()