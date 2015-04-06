'''This file gives you an example of how you can unit test a class'''
 
from complex  import *
import unittest
 
class testComplex(unittest.TestCase):
 
    def setUp(self):
        self.one_plus_i = Complex(1, 1)
        self.one = Complex(1, 0)
        self.iota = Complex(0, 1)

    # identifies as helper function, because it does not have test written in its name
    def equality(self, complex_one, complex_two):
        '''return whether complex_one and complex_two are equal'''
        return (complex_one.r == complex_two.r and
                complex_one.i == complex_two.i)
     
    def testCreation(self):
        '''Test the init method'''
        self.assertEqual(self.one_plus_i.r, 1)
        self.assertEqual(self.one_plus_i.i, 1)
 
    def testAdd(self):
        # this will not work
        self.assertEqual(Complex(2,1),self.one_plus_i.add(self.one))
        # need to write a helper function to compare the two classes
        self.assertTrue(     self.equality(  Complex(2, 1),self.one_plus_i.add(self.one)  )     )
     
unittest.main()
