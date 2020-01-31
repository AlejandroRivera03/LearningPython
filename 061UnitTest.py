import unittest

def doblar(a): return a*2
def sumar(a,b): return a+b
def es_par(a): return True if a % 2 == 0 else False

class PruebasFunciones( unittest.TestCase ):

    # def setUp( self ): #it's like the constructor
    #     print( 'Preparando el contexto' )
    #     self.numeros = [1, 2, 3, 4, 5]
    
    def test_doblar( self ):
        self.assertEqual( doblar( 10 ), 20 )
        self.assertEqual( doblar( 'Ab' ), 'AbAb' )
    
    def test_sumar( self ):
        self.assertEqual( sumar( -15, 15 ), 0 )
        self.assertEqual( sumar( 'Ab', 'cd' ), 'Abcd' )
    
    def test_es_par( self ):
        self.assertEqual( es_par( 11 ), False )
        self.assertEqual( es_par( 68 ), True )

    def test_upper( self ):
        self.assertEqual( 'hola'.upper(), 'HOLA' )
    
    def test_isupper( self ):
        self.assertTrue( 'HOLA'.isupper() )
        self.assertFalse( 'hola'.isupper() )
    
    def test_split( self ):
        self.assertEqual( 'Hola mundo'.split( ' ' ), ['Hola', 'mundo'] )
    
    # def test_duplicate( self ):
    #     print( 'Realizando prueba' )
    #     r = [doblar(n) for n in self.numeros]
    #     self.assertEqual( r, [2, 4, 6, 8, 10] )
    
    # def tearDown( self ): # it's like the destructor
    #     print( 'Destruyendo el contexto' )
    #     del( self.numeros )

unittest.main()

# assertEqual(a,b) => a == b
# assertNotEqual(a,b) => a != b
# assertTrue(x) => bool(x) is True
# assertFalse(x) => bool(x) is False
# assertIs(a,b) => a is b
# assertIsNot(a,b) => a is not b
# assertIsNone(x) => x is None
# assertIsNotNone(x) => x is not None
# assertIn(a,b) => a in b
# assertNotIn(a,b) => a not in b
# assertIsInstance(a,b) => isinstance(a,b)
# assertNotIsInstance(a,b) => not is instance(a,b)