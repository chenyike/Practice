import unittest
from inClassFileExample import *

class Test_FileExample(unittest.TestCase):
    fileName = ''
    
    def setUp(self):
        self.fileName = 'movies copy.txt'

    def test_count_lines(self):
        number = count_lines(['for','cit','590'])
        self.assertEqual(number, 3)
        self.assertEqual(count_lines([]), 0)

    def test_count_words(self):
        num_words = count_words(['for this', 'a', 'b Errr'])
        self.assertEqual(num_words,5)

##    def test_count_characters(self):
##        num_characters = count_character(['ab b c',  '', 'd'])
##        self.assertEqual(num_characters,5)



unittest.main()
