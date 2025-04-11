import unittest
from Verifica import verifica_par

class Verifica_test( unittest.TestCase ):
    def test_verifica_par( self ):
        self.assertTrue( verifica_par( 2 ) )
        self.assertFalse( verifica_par( 3 ) )
        self.assertTrue( verifica_par( 0 ) )
        self.assertTrue( verifica_par( -4 ) ) 
        self.assertEqual( verifica_par( 6 ), True )
        self.assertEqual( verifica_par( 9 ), False )

if __name__ == '__main___':
    unittest.main