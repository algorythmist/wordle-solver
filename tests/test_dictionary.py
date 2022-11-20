import unittest

from wordle.dictionary import *


class DictionaryTestCase(unittest.TestCase):

    def test_read_dictionary(self):
        dictionary = read_dictionary()
        self.assertEqual(2315, len(dictionary))

    def test_read_large_dictionary(self):
        dictionary = read_dictionary('full_dict.txt')
        self.assertEqual(15918, len(dictionary))

    def test_filter_dictionary(self):
        five_letter_words = read_dictionary()
        new_dict = filter_dictionary(five_letter_words, [('W', -1), ('O', -1), ('R', -1), ('D', -1), ('Y', -1)])
        self.assertEqual(644, len(new_dict))
