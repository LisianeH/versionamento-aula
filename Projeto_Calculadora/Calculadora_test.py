import unittest 
from Calculadora import somar, dividir

class Calculadora_test( unittest.TestCase ):

    def teste_somar( self ):
        self.assertEqual( somar( 2, 3 ), 5 )
        self.assertEqual( somar( -1, 1 ), 0 )
        self.assertEqual( somar( 0, 0 ), 0 )

    def teste_dividir( self ):
        self.assertEqual( dividir( 8, 4 ), 2 )
        self.assertEqual( dividir( 2, 1 ), 2 )
        self.assertEqual( dividir( 15, 5 ), 3 )

    def teste_dividir_por_zero( self ):
        with self.assertRaises( ValueError ):
            dividir( 10, 0 ) 

if __name__ == '__main___':
    unittest.main