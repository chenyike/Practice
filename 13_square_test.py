import unittest
from square import *
class Test_Square(unittest.TestCase):
    def test_12_square(self):
        self.assertEqual(4,square(2),'Square did not work')
        self.assertEqual(2.25,square(1.5),'Square did not work')
        #error,func name,arg
        self.assertRaises(RuntimeError , square, 'banana')

unittest.main()  # outside the class--this tells the framework to run
