#note that we do not do the usual from ... import ...
import dictionary 
import unittest

class Test_WC(unittest.TestCase):
    
    def setUp(self):
        #this is how we can set up the global variable
        dictionary.freq = {'the' : 40, 'shake' : 1}
    
    def test_most_frequent(self):
        result =  dictionary.most_frequent()
        self.assertEqual(('the', 40), result)


unittest.main()
